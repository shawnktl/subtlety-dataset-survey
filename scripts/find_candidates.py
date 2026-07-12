#!/usr/bin/env python3
"""Multi-channel, fetch-only candidate finder for new subtlety/perceptibility datasets.

Stdlib-only (``urllib`` + ``json``). Reads its query set and anchor list from
``notes/search-strategy.md`` (data-driven, NOT hardcoded), queries several keyless
open scholarly + dataset-repository APIs, does forward/backward citation chasing from
the Tier-A anchor datasets, dedups hits against the existing ``datasets/`` corpus, and
writes a ranked ``notes/candidates.md``.

Channels queried (>= 5; degrade gracefully if any is unreachable):
  Scholarly:   Semantic Scholar Graph API (search + citation chasing),
               OpenAlex, Europe PMC
  Repos:       Zenodo, Figshare, HuggingFace datasets
  Manual-only: PhysioNet, TCIA, grand-challenge, Papers With Code, OpenNeuro, Kaggle
               (documented in notes/search-strategy.md for the agent's manual pass)

Design contract
---------------
* **Fetch + report ONLY.** It never edits dataset content. Curation is human/agent.
* **Never hard-fails.** Rate limits (HTTP 429, esp. unauthenticated Semantic Scholar)
  and transient errors are caught with backoff; the script ALWAYS exits 0 and always
  writes a candidates file (even if some channels returned nothing).
* No third-party dependencies. Python 3.9+ standard library only.

Run:  python scripts/find_candidates.py
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STRATEGY = REPO_ROOT / "notes" / "search-strategy.md"
OUTPUT = REPO_ROOT / "notes" / "candidates.md"

TIMEOUT = 25
USER_AGENT = (
    "subtlety-dataset-survey-candidate-finder/1.0 "
    "(+https://github.com/shawnktl/subtlety-dataset-survey; mailto:shawn.kt.lyo@gmail.com)"
)
PER_QUERY_LIMIT = 12      # max hits to pull per query per channel
MAX_QUERIES_SCHOLARLY = 12  # cap scholarly queries to keep run time + rate limits sane

DEFAULT_QUERIES = [
    "radiology dataset lesion subtlety annotation",
    "medical imaging perceptibility dataset",
    "lesion conspicuity dataset radiology",
    "observer performance study dataset radiology",
    "multi-reader multi-case dataset radiology annotation",
]
DEFAULT_ANCHORS = [
    ("LIDC-IDRI", "10.1118/1.3528204"),
    ("CBIS-DDSM", "10.1038/sdata.2017.177"),
    ("LNDb", "10.1038/s41597-024-03345-6"),
]


# ---------------------------------------------------------------------------
# HTTP helper (never raises; returns parsed JSON or None)
# ---------------------------------------------------------------------------

def fetch_json(url: str, *, data: bytes | None = None, headers: dict | None = None,
               retries: int = 3) -> dict | list | None:
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    backoff = 2.0
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, headers=hdrs,
                                     method="POST" if data else "GET")
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
                return json.loads(raw)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                print(f"      rate-limited (429); backing off {backoff:.0f}s")
                time.sleep(backoff)
                backoff *= 2
                continue
            print(f"      HTTP {e.code} for {url[:90]}")
            return None
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as e:
            if attempt < retries - 1:
                time.sleep(backoff)
                backoff *= 2
                continue
            print(f"      failed: {getattr(e, 'reason', e)}")
            return None
        except Exception as e:  # pragma: no cover - defensive
            print(f"      unexpected {type(e).__name__}: {e}")
            return None
    return None


# ---------------------------------------------------------------------------
# Strategy-file parsing (data-driven queries + anchors)
# ---------------------------------------------------------------------------

def _extract_fenced(text: str, lang: str) -> list[str]:
    m = re.search(r"```" + re.escape(lang) + r"\s*\n(.*?)```", text, re.DOTALL)
    if not m:
        return []
    lines = []
    for line in m.group(1).splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        lines.append(s)
    return lines


def load_strategy() -> tuple[list[str], list[tuple[str, str]], str]:
    """Return (queries, anchors, source_note)."""
    if not STRATEGY.exists():
        return DEFAULT_QUERIES, DEFAULT_ANCHORS, "search-strategy.md missing — used built-in defaults"
    text = STRATEGY.read_text(encoding="utf-8")
    queries = _extract_fenced(text, "queries") or DEFAULT_QUERIES
    anchors_raw = _extract_fenced(text, "anchors")
    anchors: list[tuple[str, str]] = []
    for line in anchors_raw:
        if "|" in line:
            name, ident = (p.strip() for p in line.split("|", 1))
            if name and ident:
                anchors.append((name, ident))
    if not anchors:
        anchors = DEFAULT_ANCHORS
    note = ("queries + anchors read from notes/search-strategy.md"
            if queries is not DEFAULT_QUERIES else "used built-in default queries")
    return queries, anchors, note


# ---------------------------------------------------------------------------
# Dedup corpus (existing datasets/ + sources)
# ---------------------------------------------------------------------------

def build_dedup_index() -> tuple[set[str], set[str], set[str]]:
    """Return (lower dataset-name tokens, DOIs, URL host+paths) seen in the corpus."""
    names: set[str] = set()
    dois: set[str] = set()
    urls: set[str] = set()
    doi_re = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.I)
    url_re = re.compile(r"https?://([^\s<>)\]\"']+)")

    for src in sorted((REPO_ROOT / "datasets").glob("*.md")):
        names.add(src.stem.lower())
        text = src.read_text(encoding="utf-8")
        # First heading is the canonical name.
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            names.add(m.group(1).strip().lower())
        for d in doi_re.findall(text):
            dois.add(d.rstrip(".").lower())
        for u in url_re.findall(text):
            urls.add(u.rstrip(".,;:)/").lower())

    sources = REPO_ROOT / "resources" / "sources.md"
    if sources.exists():
        text = sources.read_text(encoding="utf-8")
        for d in doi_re.findall(text):
            dois.add(d.rstrip(".").lower())
        for u in url_re.findall(text):
            urls.add(u.rstrip(".,;:)/").lower())
        # Bold dataset names: **Name:**
        for m in re.finditer(r"\*\*([^*:]+):?\*\*", text):
            names.add(m.group(1).strip().lower())

    return names, dois, urls


def is_duplicate(title: str, doi: str | None, url: str | None,
                 names: set[str], dois: set[str], urls: set[str]) -> str | None:
    """Return the matching reason if this hit duplicates the corpus, else None."""
    if doi and doi.rstrip(".").lower() in dois:
        return f"DOI already in corpus ({doi})"
    t = (title or "").lower()
    for name in names:
        if len(name) >= 4 and name in t:
            return f"name match: '{name}'"
    if url:
        host_path = re.sub(r"^https?://", "", url).rstrip(".,;:)/").lower()
        if host_path in urls:
            return f"URL already in corpus"
    return None


# ---------------------------------------------------------------------------
# Channels
# ---------------------------------------------------------------------------

def ch_semantic_scholar(query: str) -> list[dict]:
    fields = "title,year,externalIds,url,abstract,openAccessPdf"
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?"
           + urllib.parse.urlencode({"query": query, "limit": PER_QUERY_LIMIT, "fields": fields}))
    data = fetch_json(url)
    out = []
    if isinstance(data, dict):
        for p in data.get("data", []) or []:
            ext = p.get("externalIds") or {}
            out.append({
                "title": p.get("title", ""),
                "year": p.get("year"),
                "doi": ext.get("DOI"),
                "url": p.get("url") or (p.get("openAccessPdf") or {}).get("url"),
                "channel": "Semantic Scholar",
                "why": f"search: '{query}'",
            })
    return out


def ch_semantic_scholar_citations(name: str, ident: str) -> list[dict]:
    """Forward + backward citation chasing from an anchor dataset paper."""
    # Resolve identifier to a paperId.
    if ident.lower().startswith("arxiv:"):
        pid = "arXiv:" + ident.split(":", 1)[1]
    elif ident.startswith("10."):
        pid = "DOI:" + ident
    else:
        pid = ident
    out = []
    for direction, endpoint in (("references", "references"), ("citations", "citations")):
        fields = "title,year,externalIds,url"
        url = (f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(pid, safe=':')}/"
               f"{endpoint}?" + urllib.parse.urlencode({"limit": PER_QUERY_LIMIT, "fields": fields}))
        data = fetch_json(url)
        time.sleep(1.0)  # be polite to the throttled unauthenticated endpoint
        if not isinstance(data, dict):
            continue
        for entry in data.get("data", []) or []:
            p = entry.get("citedPaper") or entry.get("citingPaper") or {}
            ext = p.get("externalIds") or {}
            out.append({
                "title": p.get("title", ""),
                "year": p.get("year"),
                "doi": ext.get("DOI"),
                "url": p.get("url"),
                "channel": "Semantic Scholar (citation chase)",
                "why": f"{direction} of anchor {name}",
            })
    return out


def ch_openalex(query: str) -> list[dict]:
    url = ("https://api.openalex.org/works?"
           + urllib.parse.urlencode({"search": query, "per-page": PER_QUERY_LIMIT,
                                     "mailto": "shawn.kt.lyo@gmail.com"}))
    data = fetch_json(url)
    out = []
    if isinstance(data, dict):
        for w in data.get("results", []) or []:
            doi = (w.get("doi") or "").replace("https://doi.org/", "") or None
            out.append({
                "title": w.get("title") or "",
                "year": w.get("publication_year"),
                "doi": doi,
                "url": w.get("id"),
                "channel": "OpenAlex",
                "why": f"search: '{query}'",
            })
    return out


def ch_europepmc(query: str) -> list[dict]:
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
           + urllib.parse.urlencode({"query": query, "format": "json", "pageSize": PER_QUERY_LIMIT}))
    data = fetch_json(url)
    out = []
    if isinstance(data, dict):
        for r in (data.get("resultList") or {}).get("result", []) or []:
            doi = r.get("doi")
            pmcid = r.get("pmcid")
            link = (f"https://europepmc.org/article/{r.get('source')}/{r.get('id')}"
                    if r.get("id") else None)
            out.append({
                "title": r.get("title", ""),
                "year": r.get("pubYear"),
                "doi": doi,
                "url": link or (f"https://europepmc.org/articles/{pmcid}" if pmcid else None),
                "channel": "Europe PMC",
                "why": f"search: '{query}'",
            })
    return out


def ch_zenodo(query: str) -> list[dict]:
    url = ("https://zenodo.org/api/records?"
           + urllib.parse.urlencode({"q": query, "size": PER_QUERY_LIMIT, "type": "dataset"}))
    data = fetch_json(url)
    out = []
    if isinstance(data, dict):
        for h in (data.get("hits") or {}).get("hits", []) or []:
            meta = h.get("metadata") or {}
            out.append({
                "title": meta.get("title", ""),
                "year": (meta.get("publication_date") or "")[:4] or None,
                "doi": meta.get("doi") or h.get("doi"),
                "url": h.get("links", {}).get("self_html") or h.get("links", {}).get("self"),
                "channel": "Zenodo",
                "why": f"dataset search: '{query}'",
            })
    return out


def ch_figshare(query: str) -> list[dict]:
    url = "https://api.figshare.com/v2/articles/search"
    body = json.dumps({"search_for": query, "page_size": PER_QUERY_LIMIT}).encode("utf-8")
    data = fetch_json(url, data=body, headers={"Content-Type": "application/json"})
    out = []
    if isinstance(data, list):
        for a in data:
            out.append({
                "title": a.get("title", ""),
                "year": (a.get("published_date") or "")[:4] or None,
                "doi": a.get("doi") or None,
                "url": a.get("url_public_html") or a.get("url"),
                "channel": "Figshare",
                "why": f"search: '{query}'",
            })
    return out


def ch_huggingface(query: str) -> list[dict]:
    url = ("https://huggingface.co/api/datasets?"
           + urllib.parse.urlencode({"search": query, "limit": PER_QUERY_LIMIT}))
    data = fetch_json(url)
    out = []
    if isinstance(data, list):
        for d in data:
            ds_id = d.get("id") or d.get("modelId") or ""
            out.append({
                "title": ds_id,
                "year": (d.get("lastModified") or "")[:4] or None,
                "doi": None,
                "url": f"https://huggingface.co/datasets/{ds_id}" if ds_id else None,
                "channel": "HuggingFace",
                "why": f"dataset search: '{query}'",
            })
    return out


# ---------------------------------------------------------------------------
# Relevance heuristic for ranking
# ---------------------------------------------------------------------------

_RELEVANCE_TERMS = [
    "subtlety", "subtle", "perceptib", "conspicuity", "conspicuous", "detectab",
    "reader study", "observer performance", "multi-reader", "multireader",
    "inter-rater", "interobserver", "inter-observer", "disagreement",
    "difficulty", "missed", "hard case", "eye-tracking", "eye tracking", "gaze",
    "annotation", "dataset", "benchmark",
]


def relevance_score(hit: dict) -> int:
    t = (hit.get("title") or "").lower()
    score = sum(2 for term in _RELEVANCE_TERMS if term in t)
    # Citation-chase hits from anchors get a small bump (graph-proximity signal).
    if "citation chase" in hit.get("channel", "").lower():
        score += 1
    yr = hit.get("year")
    try:
        if yr and int(yr) >= 2022:
            score += 2  # recency: newly-published is what we want to surface
    except (ValueError, TypeError):
        pass
    return score


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    queries, anchors, strat_note = load_strategy()
    queries = queries[:MAX_QUERIES_SCHOLARLY]
    print(f"Strategy: {strat_note}")
    print(f"Queries: {len(queries)} | Anchors: {len(anchors)}")

    names, dois, urls = build_dedup_index()
    print(f"Dedup corpus: {len(names)} names, {len(dois)} DOIs, {len(urls)} URLs")

    channel_fns = [
        ("Semantic Scholar", ch_semantic_scholar),
        ("OpenAlex", ch_openalex),
        ("Europe PMC", ch_europepmc),
        ("Zenodo", ch_zenodo),
        ("Figshare", ch_figshare),
        ("HuggingFace", ch_huggingface),
    ]

    raw_hits: list[dict] = []
    channel_stats: dict[str, int] = {}
    channel_errors: list[str] = []

    # ---- per-query scholarly + repo searches ----
    for query in queries:
        print(f"\n[query] {query}")
        for cname, fn in channel_fns:
            try:
                hits = fn(query)
            except Exception as e:  # pragma: no cover - defensive
                hits = []
                channel_errors.append(f"{cname}: {type(e).__name__}: {e}")
            channel_stats[cname] = channel_stats.get(cname, 0) + len(hits)
            raw_hits.extend(hits)
            print(f"    {cname}: {len(hits)} hits")
            time.sleep(0.5)  # gentle pacing across channels

    # ---- citation chasing from anchors (Semantic Scholar) ----
    print("\n[citation chasing]")
    for name, ident in anchors:
        try:
            hits = ch_semantic_scholar_citations(name, ident)
        except Exception as e:  # pragma: no cover
            hits = []
            channel_errors.append(f"citation-chase {name}: {type(e).__name__}: {e}")
        channel_stats["Semantic Scholar (citation chase)"] = (
            channel_stats.get("Semantic Scholar (citation chase)", 0) + len(hits))
        raw_hits.extend(hits)
        print(f"    {name}: {len(hits)} ref/cite hits")

    # ---- dedup + dedup against corpus ----
    seen_keys: set[str] = set()
    candidates: list[dict] = []
    dup_count = 0
    for h in raw_hits:
        title = (h.get("title") or "").strip()
        if not title:
            continue
        key = (h.get("doi") or "").lower() or title.lower()
        if key in seen_keys:
            continue
        seen_keys.add(key)
        dup_reason = is_duplicate(title, h.get("doi"), h.get("url"), names, dois, urls)
        if dup_reason:
            dup_count += 1
            continue
        h["score"] = relevance_score(h)
        candidates.append(h)

    candidates.sort(key=lambda x: (-x["score"], -(int(x["year"]) if str(x.get("year") or "").isdigit() else 0)))

    print(f"\nRaw hits: {len(raw_hits)} | unique: {len(seen_keys)} | "
          f"deduped-vs-corpus: {dup_count} | candidates: {len(candidates)}")

    # ---- write report ----
    today = date.today().isoformat()
    n_channels = len([c for c in channel_stats if channel_stats[c] is not None])
    lines: list[str] = []
    lines.append("# Candidate Datasets / Papers")
    lines.append("")
    lines.append(
        "Auto-generated by `scripts/find_candidates.py` — a **fetch-only** scan across "
        "multiple open scholarly + dataset-repository channels for newly-published "
        "subtlety / perceptibility / conspicuity datasets (and difficulty-proxy reader "
        "studies). **These are leads, not curated entries.** An agent triages them per "
        "`notes/refresh-agent.md`: confirm each is a real, accessible *dataset* (most "
        "reader-study papers release nothing), dedup against `datasets/`, then curate the "
        "survivors into dataset pages. Hits already in the corpus are filtered out."
    )
    lines.append("")
    lines.append(f"**Generated:** {today}")
    lines.append("")
    lines.append(
        f"**Run summary:** {len(raw_hits)} raw hits across {len(channel_stats)} channels · "
        f"{dup_count} filtered as already-in-corpus · **{len(candidates)} candidates** below. "
        f"Strategy source: {strat_note}."
    )
    lines.append("")
    lines.append("**Per-channel hit counts:**")
    lines.append("")
    lines.append("| Channel | Raw hits |")
    lines.append("|---|---|")
    for cname in sorted(channel_stats):
        lines.append(f"| {cname} | {channel_stats[cname]} |")
    lines.append("")
    if channel_errors:
        lines.append("**Channel errors / limitations this run:**")
        lines.append("")
        for err in channel_errors[:20]:
            lines.append(f"- {err}")
        lines.append("")

    lines.append("## Ranked candidates")
    lines.append("")
    if candidates:
        lines.append("| # | Score | Year | Candidate | Channel | Why flagged | Link |")
        lines.append("|---|---|---|---|---|---|---|")
        for i, c in enumerate(candidates[:120], 1):
            title = (c.get("title") or "").replace("|", "\\|")[:160]
            why = (c.get("why") or "").replace("|", "\\|")
            link = c.get("url") or (f"https://doi.org/{c['doi']}" if c.get("doi") else "")
            link_cell = link.replace("|", "%7C") if link else "—"
            yr = c.get("year") or "—"
            lines.append(f"| {i} | {c['score']} | {yr} | {title} | {c['channel']} | {why} | {link_cell} |")
    else:
        lines.append(
            "_No new candidates surfaced this run._ This can mean a genuinely quiet week, "
            "or that network access to the channels was limited in the run environment "
            "(see channel hit counts above — all-zero counts indicate the latter). "
            "Run the manual web pass in `notes/search-strategy.md` to cover the channels "
            "the script can't reach."
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        "_Next: an agent follows `notes/refresh-agent.md` to triage these, runs the manual "
        "channels (PhysioNet, TCIA, grand-challenge, Papers With Code, OpenNeuro, Kaggle), "
        "curates confirmed datasets (≤8/run, ≤2/modality), and appends what worked to the "
        "effectiveness log in `notes/search-strategy.md`._"
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"\nWrote {OUTPUT.relative_to(REPO_ROOT).as_posix()} with {len(candidates)} candidates.")

    # Contract: partial failure is fine. Always succeed.
    return 0


if __name__ == "__main__":
    sys.exit(main())
