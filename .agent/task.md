# 🚨 DISPATCH METADATA — read before doing anything else

| field | value |
|---|---|
| **Branch** | `agent/subtlety-dataset-search` |
| **Project slug** | `subtlety-dataset-search` |
| **Spec** | `agent` |

## Required behavior

- **Push commits to `agent/subtlety-dataset-search` and only `agent/subtlety-dataset-search`.** Do NOT invent a
  shorter or "cleaner" branch name. The rounds-repo status tracker matches
  PRs by exact branch name; any other name leaves the PR orphaned in
  tracking and requires manual fixup.
- **Open the PR with `agent/subtlety-dataset-search` as head** against the repo's default branch
  as base.
- The branch already exists (the dispatch script created it before
  handing off to you). You're already checked out on it — just commit and
  push. No `git checkout -b` needed.

---

# Original spec

# Agent Spec — Subtlety Dataset Survey: Browsable HTML View (GitHub Pages)

## Objective
Turn the existing markdown survey repo (`shawnktl/subtlety-dataset-survey`) into a
**browsable static HTML site publishable via GitHub Pages**. "Done" = a generated
`docs/` site that renders the tier index and every per-dataset page as navigable HTML,
plus GitHub Pages serving it, so the survey is explorable in a browser rather than only
as raw markdown. This is the **HTML-view-only** scope — an automated weekly refresh
cadence is explicitly out of scope for this pass (a later spec).

## Scope
**SHOULD touch / create:**
- A build script (e.g. `scripts/build_site.py`) that converts the repo's markdown
  (`index.md`, `datasets/*.md`, `notes/*.md`, `resources/*.md`, `PROJECT_SUMMARY.md`)
  into a static HTML site under `docs/`.
- `docs/` output (the generated site): `docs/index.html` (landing = tier index), one
  HTML page per dataset, a styled template/CSS, and cross-page navigation.
- A short README section documenting how to rebuild the site and the Pages URL.
- A workflow file `.github/workflows/pages.yml` ONLY if needed to publish `docs/` to
  GitHub Pages on push (build-and-deploy of the already-committed site is fine; do NOT
  add scheduled/cron refresh logic — that's the deferred auto-refresh spec).

**MUST NOT touch:**
- The substance of the survey content in `datasets/`, `index.md`, `notes/`,
  `resources/` — render it, don't rewrite it. Preserve every "verify directly before
  relying on" caveat verbatim in the rendered output.
- `.agent/`, `BOOTSTRAP.md`, `CLAUDE.md`.

## Tasks
1. Inventory the markdown sources and the tier structure in `index.md` so the site's
   landing page and navigation mirror the existing tier ranking (Tier A direct-label
   datasets first, etc.).
2. Write `scripts/build_site.py` — a small, dependency-light markdown→HTML build
   (standard-library or a single well-known lib pinned in a `requirements.txt`). It must
   render headings, lists, tables, links, inline code, and bold/italic.
3. Produce a clean, readable template with a persistent nav (tier index / dataset list)
   and a per-dataset page layout (labels, access/licensing, detectability-framing
   crosswalk). Keep styling simple and legible — this is a reference resource.
4. Generate the full `docs/` site and commit it.
5. Add `.github/workflows/pages.yml` to deploy `docs/` to GitHub Pages (if the simpler
   "Pages from `docs/` folder" setting can't be assumed). Confirm the published URL.
6. Update `README.md` with: how to rebuild (`python scripts/build_site.py`) and the
   live Pages URL.

## Constraints
- Work on branch `agent/subtlety-dataset-search`.
- Commit with prefix `agent:`.
- Don't push to main/master directly — open a PR.
- HTML view only. No scheduled/automated content-refresh logic this pass.

## Acceptance Criteria
- [ ] `scripts/build_site.py` regenerates the full site deterministically from the markdown.
- [ ] `docs/index.html` is the tier-ranked landing page; every dataset has its own HTML page.
- [ ] Navigation lets you move between the index and any dataset page without editing URLs.
- [ ] All survey content and caveats are preserved (rendered, not rewritten).
- [ ] GitHub Pages serves the site; the URL is recorded in the README.
- [ ] A PR is opened from `agent/subtlety-dataset-search`.

## Context
The repo was populated from the 26-dataset survey (CT, CXR, mammography FFDM+DBT, MR,
fundus, MSK, PE imaging) in PR #2. The user wants this to become an easily explorable,
shareable, publicly accessible resource — in the spirit of the Radiology Opportunities
Tracker. This spec is the first step (browsable HTML view) so the user can see how it
looks before committing to the eventual automated weekly refresh cadence.
