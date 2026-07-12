#!/usr/bin/env python3
"""Verify the source/access links across the survey markdown.

Stdlib-only (``urllib``). Extracts every http(s) URL from the dataset pages,
the sources file, the index, and the follow-ups notes; requests each with a
timeout + light retry and a realistic User-Agent; classifies the result as
**OK / redirect / dead / forbidden (403 bot-block)**; and writes a dated table
to ``notes/link-status.md``.

Design contract
---------------
* **A dead link is a finding, not a CI failure.** This script ALWAYS exits 0,
  even when links are dead or forbidden, so the weekly workflow never red-Xs on
  link rot. (Mirrors the Radiology Opportunities verifier, which reports the
  Sarnoff 403 bot-block instead of erroring.)
* No third-party dependencies. Python 3.9+ standard library only.

Run:  python scripts/verify_links.py
"""

from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Markdown files whose links we verify. Globs are expanded relative to REPO_ROOT.
SOURCE_GLOBS = [
    "datasets/*.md",
    "resources/sources.md",
    "index.md",
    "notes/follow-ups.md",
]

OUTPUT = REPO_ROOT / "notes" / "link-status.md"

TIMEOUT = 20  # seconds per request
RETRIES = 1   # extra attempts after the first, on transient failure
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 "
    "subtlety-dataset-survey-linkcheck/1.0 (+https://github.com/shawnktl/subtlety-dataset-survey)"
)

# Match bare http(s) URLs, trimming trailing markdown/sentence punctuation.
_URL_RE = re.compile(r"https?://[^\s<>)\]\"']+")


def extract_urls() -> dict[str, list[str]]:
    """Return {url: [source_files...]} for every http(s) URL in the corpus."""
    found: dict[str, list[str]] = {}
    for glob in SOURCE_GLOBS:
        for path in sorted(REPO_ROOT.glob(glob)):
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            rel = path.relative_to(REPO_ROOT).as_posix()
            for m in _URL_RE.finditer(text):
                url = m.group(0)
                # Trim trailing punctuation that isn't part of the URL.
                while url and url[-1] in ".,;:)]}>'\"":
                    url = url[:-1]
                if not url:
                    continue
                found.setdefault(url, [])
                if rel not in found[url]:
                    found[url].append(rel)
    return found


def _request(url: str, method: str) -> tuple[int | None, str | None]:
    """Return (status_code, final_url_after_redirect) or (None, None) on error."""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.getcode(), resp.geturl()


def check_url(url: str) -> dict:
    """Classify a single URL. Never raises."""
    last_err = ""
    for attempt in range(RETRIES + 1):
        # Try HEAD first (cheap); fall back to GET if the server rejects HEAD.
        for method in ("HEAD", "GET"):
            try:
                code, final = _request(url, method)
                redirected = bool(final and final.rstrip("/") != url.rstrip("/"))
                status = "redirect" if redirected else "OK"
                return {
                    "url": url,
                    "code": code or 200,
                    "status": status,
                    "note": (f"-> {final}" if redirected else ""),
                }
            except urllib.error.HTTPError as e:
                code = e.code
                if code in (403, 401, 429):
                    return {
                        "url": url,
                        "code": code,
                        "status": "forbidden",
                        "note": f"bot-block / auth ({code}) — verify manually in a browser",
                    }
                if code in (405, 501) and method == "HEAD":
                    # Method not allowed for HEAD — let the GET attempt run.
                    last_err = f"HEAD {code}; retrying with GET"
                    continue
                if 400 <= code < 500:
                    return {"url": url, "code": code, "status": "dead", "note": f"client error {code}"}
                # 5xx: server-side; retry-eligible.
                last_err = f"server error {code}"
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                last_err = str(getattr(e, "reason", e))
            except Exception as e:  # pragma: no cover - defensive: never crash the job
                last_err = f"{type(e).__name__}: {e}"
        if attempt < RETRIES:
            time.sleep(1.5)  # brief backoff before retry
    return {"url": url, "code": None, "status": "dead", "note": f"unreachable: {last_err}"[:160]}


def main() -> int:
    urls = extract_urls()
    print(f"Checking {len(urls)} unique URLs across the survey markdown...")

    results = []
    for url in sorted(urls):
        r = check_url(url)
        r["sources"] = urls[url]
        results.append(r)
        print(f"  [{r['status']:>9}] {r['code'] if r['code'] is not None else '---':>4}  {url}")

    counts = {"OK": 0, "redirect": 0, "forbidden": 0, "dead": 0}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    today = date.today().isoformat()
    lines: list[str] = []
    lines.append("# Link Status")
    lines.append("")
    lines.append(
        "Automated link-availability check over the survey's source/access URLs, "
        "produced by `scripts/verify_links.py`. Dead/forbidden links are **findings to "
        "triage**, not errors — a 403 is usually a bot-block, not a removed resource. "
        "Verify any flagged link directly in a browser before acting on it."
    )
    lines.append("")
    lines.append(f"**Last checked:** {today}")
    lines.append("")
    lines.append(
        f"**Summary:** {counts.get('OK', 0)} OK · {counts.get('redirect', 0)} redirect · "
        f"{counts.get('forbidden', 0)} forbidden (403/401/429) · {counts.get('dead', 0)} dead "
        f"· {len(results)} total"
    )
    lines.append("")
    lines.append("| Status | HTTP | URL | Found in | Note |")
    lines.append("|---|---|---|---|---|")

    status_order = {"dead": 0, "forbidden": 1, "redirect": 2, "OK": 3}
    for r in sorted(results, key=lambda x: (status_order.get(x["status"], 9), x["url"])):
        code = r["code"] if r["code"] is not None else "—"
        srcs = ", ".join(f"`{s}`" for s in r["sources"])
        note = r["note"].replace("|", "\\|") if r["note"] else ""
        url_cell = r["url"].replace("|", "%7C")
        lines.append(f"| {r['status']} | {code} | {url_cell} | {srcs} | {note} |")
    lines.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"\nWrote {OUTPUT.relative_to(REPO_ROOT).as_posix()} "
          f"({counts.get('dead', 0)} dead, {counts.get('forbidden', 0)} forbidden).")

    # Contract: dead links are findings, not failures. Always succeed.
    return 0


if __name__ == "__main__":
    sys.exit(main())
