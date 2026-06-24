#!/usr/bin/env python3
"""Build a browsable static HTML site from the survey markdown.

Dependency-light: Python standard library only. Converts the repo's markdown
sources into a navigable site under ``docs/``:

    docs/index.html                 tier-ranked landing page (from index.md)
    docs/datasets/<id>.html         one page per dataset
    docs/notes/follow-ups.html      follow-ups page
    docs/resources/sources.html     sources page
    docs/project-summary.html       PROJECT_SUMMARY.md
    docs/style.css                  shared stylesheet

Run:  python scripts/build_site.py

The build is deterministic: re-running with unchanged sources produces an
identical ``docs/`` tree (no timestamps or other nondeterminism are emitted).

Design notes
------------
* The markdown converter is intentionally small and tailored to the prose
  shape used in this repo (headings, paragraphs, unordered/ordered lists,
  pipe tables, blockquotes, inline bold/italic/code, links, and bare-URL
  autolinking). It is NOT a general-purpose CommonMark implementation.
* The survey CONTENT is rendered, never rewritten. Every "verify directly
  before relying on" caveat in the markdown is reproduced verbatim in the HTML.
* Intra-repo ``*.md`` links are rewritten to the corresponding ``*.html`` so
  navigation works in the generated site.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
SITE_TITLE = "Subtlety / Perceptibility Dataset Survey"


# ---------------------------------------------------------------------------
# Inline markdown -> HTML
# ---------------------------------------------------------------------------

_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_BOLD_RE = re.compile(r"\*\*([^*]+?)\*\*")
_ITALIC_RE = re.compile(r"(?<![\*\w])\*([^*\s][^*]*?)\*(?!\w)")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
# Bare URL autolink: avoid trailing punctuation; stop at whitespace / a few delimiters.
_BARE_URL_RE = re.compile(r"(?<![\"\(=])\bhttps?://[^\s<)\]]+")


def _link_md_to_html(href: str) -> str:
    """Rewrite intra-repo markdown links so they resolve in the HTML site."""
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return href
    # e.g. "datasets/lidc-idri.md" -> "datasets/lidc-idri.html"
    if href.endswith(".md"):
        # PROJECT_SUMMARY.md is emitted as project-summary.html
        if href in ("PROJECT_SUMMARY.md", "./PROJECT_SUMMARY.md"):
            return "project-summary.html"
        return href[:-3] + ".html"
    return href


def render_inline(text: str) -> str:
    """Convert inline markdown to HTML, escaping along the way.

    Code spans and links are extracted as placeholders first so their
    contents are not mangled by the emphasis/autolink passes; everything
    else is HTML-escaped.
    """
    placeholders: list[str] = []

    def stash(rendered: str) -> str:
        placeholders.append(rendered)
        return f"\x00{len(placeholders) - 1}\x00"

    # 1. Inline code spans (escaped, never further processed).
    def _code(m: re.Match) -> str:
        return stash(f"<code>{html.escape(m.group(1))}</code>")

    text = _INLINE_CODE_RE.sub(_code, text)

    # 2. Markdown links [text](href).
    def _mdlink(m: re.Match) -> str:
        label = html.escape(m.group(1))
        href = html.escape(_link_md_to_html(m.group(2)), quote=True)
        return stash(f'<a href="{href}">{label}</a>')

    text = _MD_LINK_RE.sub(_mdlink, text)

    # 3. Bare URL autolinks.
    def _bare(m: re.Match) -> str:
        url = m.group(0)
        trailing = ""
        # Don't swallow sentence punctuation that follows a URL.
        while url and url[-1] in ".,;:":
            trailing = url[-1] + trailing
            url = url[:-1]
        safe = html.escape(url, quote=True)
        return stash(f'<a href="{safe}">{html.escape(url)}</a>') + trailing

    text = _BARE_URL_RE.sub(_bare, text)

    # 4. Escape remaining literal text (placeholders use \x00 sentinels).
    parts = re.split(r"(\x00\d+\x00)", text)
    out = []
    for part in parts:
        if re.fullmatch(r"\x00\d+\x00", part):
            out.append(part)
        else:
            out.append(html.escape(part))
    text = "".join(out)

    # 5. Emphasis on the escaped text.
    text = _BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = _ITALIC_RE.sub(r"<em>\1</em>", text)

    # 6. Restore placeholders.
    def _restore(m: re.Match) -> str:
        return placeholders[int(m.group(1))]

    text = re.sub(r"\x00(\d+)\x00", _restore, text)
    return text


# ---------------------------------------------------------------------------
# Block markdown -> HTML
# ---------------------------------------------------------------------------

def _split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def _is_table_divider(line: str) -> bool:
    cells = _split_table_row(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{1,}:?", c) for c in cells)


def render_markdown(md: str) -> str:
    """Render a markdown document body to an HTML fragment."""
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Blank line.
        if not stripped:
            i += 1
            continue

        # Horizontal rule.
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            out.append("<hr>")
            i += 1
            continue

        # Heading.
        m = re.match(r"(#{1,6})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{render_inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue

        # Table: a header row immediately followed by a divider row.
        if "|" in line and i + 1 < n and _is_table_divider(lines[i + 1]):
            header = _split_table_row(line)
            i += 2  # skip header + divider
            body_rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                body_rows.append(_split_table_row(lines[i]))
                i += 1
            out.append(_render_table(header, body_rows))
            continue

        # Blockquote (possibly multi-line).
        if stripped.startswith(">"):
            quote_lines = []
            while i < n and lines[i].strip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = render_inline(" ".join(l.strip() for l in quote_lines if l.strip()))
            out.append(f"<blockquote><p>{inner}</p></blockquote>")
            continue

        # Unordered list.
        if re.match(r"[-*+]\s+", stripped):
            items, i = _consume_list(lines, i, ordered=False)
            out.append("<ul>\n" + "\n".join(items) + "\n</ul>")
            continue

        # Ordered list.
        if re.match(r"\d+\.\s+", stripped):
            items, i = _consume_list(lines, i, ordered=True)
            out.append("<ol>\n" + "\n".join(items) + "\n</ol>")
            continue

        # Paragraph: gather until blank line / block boundary.
        para = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (
                not nxt
                or re.match(r"#{1,6}\s+", nxt)
                or re.fullmatch(r"-{3,}|\*{3,}|_{3,}", nxt)
                or nxt.startswith(">")
                or re.match(r"[-*+]\s+", nxt)
                or re.match(r"\d+\.\s+", nxt)
                or ("|" in lines[i] and i + 1 < n and _is_table_divider(lines[i + 1]))
            ):
                break
            para.append(nxt)
            i += 1
        out.append(f"<p>{render_inline(' '.join(para))}</p>")

    return "\n".join(out)


def _consume_list(lines: list[str], i: int, ordered: bool) -> tuple[list[str], int]:
    pattern = r"\d+\.\s+(.*)$" if ordered else r"[-*+]\s+(.*)$"
    items: list[str] = []
    n = len(lines)
    while i < n:
        stripped = lines[i].strip()
        m = re.match(pattern, stripped)
        if not m:
            break
        items.append(f"  <li>{render_inline(m.group(1).strip())}</li>")
        i += 1
    return items, i


def _render_table(header: list[str], rows: list[list[str]]) -> str:
    parts = ["<div class=\"table-wrap\">", "<table>", "<thead>", "<tr>"]
    for cell in header:
        parts.append(f"<th>{render_inline(cell)}</th>")
    parts.append("</tr>")
    parts.append("</thead>")
    parts.append("<tbody>")
    for row in rows:
        parts.append("<tr>")
        # Pad/truncate to header width for robustness.
        for idx in range(len(header)):
            cell = row[idx] if idx < len(row) else ""
            parts.append(f"<td>{render_inline(cell)}</td>")
        parts.append("</tr>")
    parts.append("</tbody>")
    parts.append("</table>")
    parts.append("</div>")
    return "\n".join(parts)


def first_heading(md: str) -> str | None:
    for line in md.replace("\r\n", "\n").split("\n"):
        m = re.match(r"#\s+(.*)$", line.strip())
        if m:
            return m.group(1).strip()
    return None


# ---------------------------------------------------------------------------
# Page template
# ---------------------------------------------------------------------------

def nav_html(depth: int, active: str) -> str:
    """Persistent top navigation. ``depth`` = directory depth from docs/ root."""
    prefix = "../" * depth
    links = [
        ("index", "Index", f"{prefix}index.html"),
        ("datasets", "Datasets", f"{prefix}index.html#datasets"),
        ("notes", "Follow-ups", f"{prefix}notes/follow-ups.html"),
        ("sources", "Sources", f"{prefix}resources/sources.html"),
        ("summary", "Project summary", f"{prefix}project-summary.html"),
    ]
    items = []
    for key, label, href in links:
        cls = ' class="active"' if key == active else ""
        items.append(f'<a{cls} href="{href}">{label}</a>')
    home = f'{prefix}index.html'
    return (
        '<header class="site-nav">\n'
        f'  <a class="brand" href="{home}">Subtlety / Perceptibility Dataset Survey</a>\n'
        '  <nav>\n    ' + "\n    ".join(items) + "\n  </nav>\n"
        "</header>"
    )


def page(title: str, body: str, depth: int, active: str, subtitle: str = "") -> str:
    prefix = "../" * depth
    sub = f'<p class="subtitle">{html.escape(subtitle)}</p>' if subtitle else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Subtlety Dataset Survey</title>
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
{nav_html(depth, active)}
<main>
{sub}
{body}
</main>
<footer class="site-footer">
  <p>Generated from the markdown survey by <code>scripts/build_site.py</code>.
  Content is rendered, not rewritten — verify every dataset's caveats against its primary source before relying on it.</p>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Stylesheet (static; emitted verbatim so the build stays deterministic)
# ---------------------------------------------------------------------------

CSS = """:root {
  --bg: #f7f8fa;
  --surface: #ffffff;
  --ink: #1c2530;
  --muted: #5b6675;
  --accent: #1d6fb8;
  --accent-dark: #14517f;
  --border: #d9dee5;
  --code-bg: #eef1f5;
  --quote-bg: #f0f4f8;
  --maxw: 960px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.6;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; color: var(--accent-dark); }

.site-nav {
  position: sticky;
  top: 0;
  z-index: 10;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0.6rem 1.2rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1.4rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.site-nav .brand {
  font-weight: 700;
  color: var(--ink);
  font-size: 0.98rem;
  margin-right: auto;
}
.site-nav nav { display: flex; flex-wrap: wrap; gap: 0.3rem 1.1rem; }
.site-nav nav a { color: var(--muted); font-size: 0.92rem; font-weight: 500; }
.site-nav nav a.active { color: var(--accent); font-weight: 700; }

main {
  max-width: var(--maxw);
  margin: 0 auto;
  padding: 1.8rem 1.2rem 3rem;
}
.subtitle { color: var(--muted); margin-top: -0.3rem; font-size: 0.95rem; }

h1 { font-size: 1.85rem; line-height: 1.2; margin: 0.4rem 0 1rem; }
h2 { font-size: 1.3rem; margin: 2rem 0 0.6rem; padding-bottom: 0.25rem; border-bottom: 1px solid var(--border); }
h3 { font-size: 1.08rem; margin: 1.5rem 0 0.4rem; }
h4 { font-size: 0.98rem; margin: 1.2rem 0 0.3rem; color: var(--muted); }

p { margin: 0.7rem 0; }
ul, ol { margin: 0.7rem 0; padding-left: 1.5rem; }
li { margin: 0.3rem 0; }

code {
  background: var(--code-bg);
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.88em;
}

blockquote {
  margin: 1rem 0;
  padding: 0.6rem 1rem;
  background: var(--quote-bg);
  border-left: 4px solid var(--accent);
  border-radius: 0 6px 6px 0;
}
blockquote p { margin: 0; }

hr { border: none; border-top: 1px solid var(--border); margin: 1.8rem 0; }

.table-wrap { overflow-x: auto; margin: 1rem 0; }
table {
  border-collapse: collapse;
  width: 100%;
  background: var(--surface);
  font-size: 0.92rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
}
th, td {
  text-align: left;
  padding: 0.55rem 0.7rem;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}
thead th {
  background: var(--quote-bg);
  font-weight: 700;
  color: var(--ink);
  white-space: nowrap;
}
tbody tr:last-child td { border-bottom: none; }
tbody tr:hover { background: #fafbfc; }

.tier-badge {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.1rem 0.5rem;
  border-radius: 999px;
  color: #fff;
}
.tier-A { background: #1d6fb8; }
.tier-B { background: #2e8b57; }
.tier-C { background: #9a6b2f; }

.site-footer {
  max-width: var(--maxw);
  margin: 0 auto;
  padding: 1.5rem 1.2rem 2.5rem;
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: 0.85rem;
}

@media (max-width: 600px) {
  .site-nav { padding: 0.5rem 0.8rem; }
  .site-nav .brand { font-size: 0.9rem; width: 100%; margin-bottom: 0.2rem; }
  main { padding: 1.2rem 0.9rem 2.5rem; }
  h1 { font-size: 1.5rem; }
}
"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Normalize to "\n" line endings so the output is byte-identical across OSes.
    path.write_text(content, encoding="utf-8", newline="\n")


def _rmtree_robust(path: Path) -> None:
    """Remove a tree, tolerating Windows/OneDrive read-only flags & transient locks."""
    import os
    import shutil
    import stat
    import time

    def _onexc(func, p, exc):
        # Clear read-only and retry once; covers the common Windows case.
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except OSError:
            pass

    for _ in range(5):
        try:
            shutil.rmtree(path, onexc=_onexc)
        except OSError:
            pass
        if not path.exists():
            return
        time.sleep(0.3)  # let a transient lock (e.g. OneDrive sync) release
    # Final attempt: let any remaining error surface.
    shutil.rmtree(path, onexc=_onexc)


def build() -> None:
    if DOCS.exists():
        # Wipe and regenerate so the output is a pure function of the sources
        # (deterministic: no stale files linger). Robust against OneDrive locks.
        _rmtree_robust(DOCS)
    DOCS.mkdir(parents=True)

    # Shared stylesheet.
    write(DOCS / "style.css", CSS)

    written: list[str] = ["style.css"]

    # ---- Landing page (index.md) --------------------------------------
    index_md = read(REPO_ROOT / "index.md")
    index_body = render_markdown(index_md)
    # Anchor target for the nav "Datasets" link (jumps to the first tier table).
    index_body = index_body.replace(
        "<h2>Tier A", '<h2 id="datasets">Tier A', 1
    )
    write(
        DOCS / "index.html",
        page(
            "Index",
            index_body,
            depth=0,
            active="index",
            subtitle="Tier-ranked index of 59 public radiology datasets with subtlety / perceptibility / conspicuity signal.",
        ),
    )
    written.append("index.html")

    # ---- Dataset pages ------------------------------------------------
    dataset_files = sorted((REPO_ROOT / "datasets").glob("*.md"))
    for src in dataset_files:
        md = read(src)
        title = first_heading(md) or src.stem
        body = render_markdown(md)
        out_rel = f"datasets/{src.stem}.html"
        write(DOCS / out_rel, page(title, body, depth=1, active="datasets"))
        written.append(out_rel)

    # ---- Notes / follow-ups ------------------------------------------
    notes_src = REPO_ROOT / "notes" / "follow-ups.md"
    if notes_src.exists():
        md = read(notes_src)
        title = first_heading(md) or "Follow-ups"
        write(
            DOCS / "notes" / "follow-ups.html",
            page(title, render_markdown(md), depth=1, active="notes"),
        )
        written.append("notes/follow-ups.html")

    # ---- Resources / sources -----------------------------------------
    sources_src = REPO_ROOT / "resources" / "sources.md"
    if sources_src.exists():
        md = read(sources_src)
        title = first_heading(md) or "Sources"
        write(
            DOCS / "resources" / "sources.html",
            page(title, render_markdown(md), depth=1, active="sources"),
        )
        written.append("resources/sources.html")

    # ---- Project summary ---------------------------------------------
    summary_src = REPO_ROOT / "PROJECT_SUMMARY.md"
    if summary_src.exists():
        md = read(summary_src)
        title = first_heading(md) or "Project Summary"
        write(
            DOCS / "project-summary.html",
            page(title, render_markdown(md), depth=0, active="summary"),
        )
        written.append("project-summary.html")

    # ---- .nojekyll so GitHub Pages serves the files as-is ------------
    write(DOCS / ".nojekyll", "")
    written.append(".nojekyll")

    for rel in written:
        print(f"  wrote docs/{rel}")
    print(f"\nBuilt {len(written)} files into {DOCS}")


if __name__ == "__main__":
    build()
