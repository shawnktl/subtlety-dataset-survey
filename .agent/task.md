# 🚨 DISPATCH METADATA — read before doing anything else

| field | value |
|---|---|
| **Branch** | `agent/subtlety-dataset-search-weekly-auto-refresh` |
| **Project slug** | `subtlety-dataset-search` |
| **Spec** | `task:weekly-auto-refresh` |

## Required behavior

- **Push commits to `agent/subtlety-dataset-search-weekly-auto-refresh` and only `agent/subtlety-dataset-search-weekly-auto-refresh`.** Do NOT invent a
  shorter or "cleaner" branch name. The rounds-repo status tracker matches
  PRs by exact branch name; any other name leaves the PR orphaned in
  tracking and requires manual fixup.
- **Open the PR with `agent/subtlety-dataset-search-weekly-auto-refresh` as head** against the repo's default branch
  as base.
- The branch already exists (the dispatch script created it before
  handing off to you). You're already checked out on it — just commit and
  push. No `git checkout -b` needed.

---

# Original spec

# Agent Spec — Subtlety Dataset Survey: Weekly Auto-Refresh

## Objective
Keep the survey current with minimal manual effort. Add (1) a **scheduled GitHub
Action** that runs unattended every week to verify dataset links, rebuild the HTML
site, and open a PR with any changes + a change-log; (2) an **extensive, multi-channel
discovery system** for finding newly-published subtlety/perceptibility/conspicuity
datasets — driven by a scriptable candidate finder (Semantic Scholar + OpenAlex +
Europe PMC + open dataset repositories + citation chasing) feeding a **living
search-strategy document that evolves and records which methods actually work**; and
(3) a documented **agent playbook** for the judgment-heavy curation the runner can't do.
"Done" = a working weekly cron that opens PRs on its own for link/availability drift, a
candidate-finder that casts a wide net across many sources, and a self-improving search
strategy + playbook for turning candidates into curated dataset pages.

Model: the **Radiology Opportunities Tracker** (`shawnktl/radiology-opportunities`)
weekly-refresh — a verifier-only Action for the automatable part + an agent-driven
"search for new" pass for the judgment part. Reuse its hard-won lessons (esp. the
PR-creation permission gotcha below).

## Prerequisite — DISPATCH ORDER
This depends on `scripts/build_site.py` + `docs/` from the **HTML-view PR (#3)**.
**Dispatch this only after PR #3 is merged to master**, so the refresh workflow can
call the existing site builder rather than rebuilding it. If dispatched before merge,
the workflow has no `build_site.py` to invoke.

## Scope
**SHOULD create:**
- `.github/workflows/weekly-refresh.yml` — `schedule:` weekly (Sunday cron) **plus**
  `workflow_dispatch:` (manual trigger). Steps: checkout → setup-python →
  `verify_links.py` → `build_site.py` → open a PR via `peter-evans/create-pull-request`.
- `scripts/verify_links.py` — **stdlib-only** (`urllib`) link checker. Parse the
  dataset/source/access URLs out of `datasets/*.md`, `resources/sources.md`, etc.;
  HEAD/GET each with a timeout + light retry; classify **OK / redirect / dead /
  forbidden (403 bot-block)**. Write a dated report to `notes/link-status.md`. It must
  **never hard-fail the job** on individual dead links — a dead link is a finding to
  report, not a CI failure (mirror how the opportunities verifier flags the Sarnoff
  403 bot-block instead of erroring).
- `scripts/find_candidates.py` — an **automatable, multi-channel candidate finder**
  (fetch-only; the curation stays human/agent). Queries several **keyless/open scholarly
  + dataset APIs** with the query set from `notes/search-strategy.md`, dedups hits
  against existing `datasets/` (by DOI / dataset name / source URL), and writes a ranked
  `notes/candidates.md` (candidate papers + datasets, with link, source channel, and
  why-flagged). At minimum query: **Semantic Scholar Graph API** (`/paper/search` +
  `/paper/{id}/references` and `/citations` for backward/forward citation chasing from
  the anchor datasets — LIDC-IDRI, JSRT, CBIS-DDSM, LNDb, CheXthought), **OpenAlex**
  (works search + cites/cited-by), and **Europe PMC**. Also probe dataset repositories
  with public search APIs where keyless: **Zenodo**, **Figshare**, **HuggingFace
  datasets**, **PhysioNet** (listing), **TCIA** (collections API), **grand-challenge.org**,
  **Papers With Code datasets**, **OpenNeuro**, **Kaggle** (if a token is available).
  Handle rate limits gracefully (Semantic Scholar throttles unauthenticated calls — add
  backoff; don't fail the job). This runs in the weekly workflow as an additional
  fetch-only step; it never edits dataset content.
- `notes/search-strategy.md` — the **living, evolving search-methods document** (this is
  the thing the user wants to grow over time). It holds: (a) the **channel list** (every
  API/source above + how to query each); (b) **query templates / keyword sets** —
  subtlety, perceptibility, conspicuity, detectability, "reader study", "observer
  performance", "multi-reader", "lesion conspicuity", BI-RADS subtlety, "annotation of
  difficulty", "hard/easy cases", per-modality variants, etc.; (c) the **citation-chasing
  procedure** (forward + backward from the Tier-A anchor datasets); (d) a dated
  **effectiveness log** — each refresh run appends which channels/queries yielded *real*
  new datasets vs. noise, dead ends found, and any new method discovered, so the
  strategy measurably improves run over run. Treat this as version-controlled and
  cumulative — **never overwrite the log, always append**; promote methods that work and
  retire ones that don't.
- `notes/refresh-agent.md` — the **discovery playbook** that *uses* the above: run
  `find_candidates.py`, triage `notes/candidates.md`, apply `search-strategy.md` (run a
  manual web pass for channels the script can't reach), **dedup against existing
  `datasets/`**, curate confirmed new datasets into the per-dataset page template,
  preserve the **"verify directly before relying on"** caveat convention, respect an
  **entry cap** (≤8 new datasets / run, ≤2 per modality), open its own PR, **and update
  `notes/search-strategy.md`'s effectiveness log + method list** with what worked this
  pass. This is invoked by pointing an agent at it — NOT run by the cron.

**SHOULD touch:**
- `README.md` — document the refresh cadence, how to trigger manually
  (`gh workflow run weekly-refresh.yml`), the one-flip permission fix below, and the
  discovery playbook.

**MUST NOT:**
- Have the unattended workflow **invent or rewrite dataset descriptions**. The Action
  verifies links + rebuilds the site + reports drift only. All new-dataset curation
  and any content edits go through the agent playbook with human review.
- Touch `.agent/`, `BOOTSTRAP.md`, `CLAUDE.md`, or the substance of existing dataset
  pages (the verifier appends a status report; it doesn't edit dataset content).

## Tasks
1. **`verify_links.py`** — extract source/access URLs from the markdown; request each
   (timeout + retry, realistic User-Agent to reduce false 403s); classify OK / redirect
   / dead / forbidden; write `notes/link-status.md` as a dated table. Exit 0 even when
   links are dead (findings, not failures).
2. **`find_candidates.py`** — implement the multi-channel candidate finder (scope above):
   Semantic Scholar Graph API search + citation chasing, OpenAlex, Europe PMC, and the
   keyless dataset-repository APIs; dedup against existing `datasets/`; write ranked
   `notes/candidates.md`. Read queries from `notes/search-strategy.md` so the query set
   is data-driven, not hardcoded. Backoff on rate limits; exit 0 on partial failure.
3. **`notes/search-strategy.md`** — seed the living strategy doc: channel list with
   per-source query recipes, the keyword/query-template sets, the citation-chasing
   procedure from the Tier-A anchors, and an (initially empty) dated **effectiveness log**
   section with a clear "append-only" instruction. This is the artifact meant to grow.
4. **`weekly-refresh.yml`** — checkout → `actions/setup-python` → run `verify_links.py`
   → run `find_candidates.py` → run `build_site.py` → `peter-evans/create-pull-request`
   opening a PR with the regenerated `docs/`, updated `notes/link-status.md`, refreshed
   `notes/candidates.md`, and a change summary in the PR body. `schedule` (weekly Sunday)
   + `workflow_dispatch`. Idempotent: a no-op week (nothing changed) should not open an
   empty PR. (The cron surfaces *candidates*; an agent later curates them — the cron does
   not auto-add dataset pages.)
5. **PR-creation permission** — this is the failure mode that silently broke the
   opportunities tracker for 5 weeks: `peter-evans/create-pull-request` errors with
   *"GitHub Actions is not permitted to create or approve pull requests"* unless the repo
   setting **Settings → Actions → General → Workflow permissions → "Allow GitHub Actions
   to create and approve pull requests"** is ON. `dispatch-agents.py` auto-enables this
   for repos it creates — **confirm it's set on `shawnktl/subtlety-dataset-survey`**
   (`gh api repos/shawnktl/subtlety-dataset-survey/actions/permissions/workflow`); if
   not, document + apply the one-flip fix:
   `gh api -X PUT repos/shawnktl/subtlety-dataset-survey/actions/permissions/workflow -F can_approve_pull_request_reviews=true`.
   **Validate by actually running the workflow once** (`workflow_dispatch`) and confirming
   it opens a PR — don't assume.
6. **`notes/refresh-agent.md`** — write the discovery playbook (scope above): run +
   triage candidates, apply + extend the search strategy, curate confirmed datasets, and
   append to the effectiveness log.
7. **`README.md`** — document cadence, manual trigger, permission fix, the candidate
   finder, the living search-strategy doc, and the playbook.

## Constraints
- Work on branch `agent/subtlety-dataset-search-weekly-auto-refresh` (the dispatcher
  creates this; do NOT reuse the HTML-view branch). Commit with the `agent:` prefix.
  Open a PR. Don't push to master.
- Pin actions to current major versions. Note the **Node 20 deprecation** (GitHub
  deprecates Sept 16, 2026) — prefer the latest action majors.
- Keep everything stdlib-only where feasible; if a dep is unavoidable, pin it in
  `requirements.txt` and install it in the workflow.

## Acceptance Criteria
- [ ] `weekly-refresh.yml` runs on cron + manual dispatch; a manual test run is all-green.
- [ ] `verify_links.py` produces `notes/link-status.md` and exits 0 even with dead links.
- [ ] `find_candidates.py` queries **≥5 channels** (must include Semantic Scholar +
      OpenAlex + Europe PMC + ≥2 dataset repositories), does forward/backward citation
      chasing from the Tier-A anchors, dedups against `datasets/`, and writes a ranked
      `notes/candidates.md`. Handles rate limits without failing the job.
- [ ] `notes/search-strategy.md` exists with the channel list, query templates, the
      citation-chasing procedure, and an append-only effectiveness log section.
- [ ] The workflow opens a PR with regenerated `docs/` + link-status + candidates +
      change-log when something changed, and is a clean no-op when nothing changed.
- [ ] PR-creation permission confirmed ON — the manual test run **actually opened a PR**.
- [ ] `notes/refresh-agent.md` documents the discovery pass (run/triage candidates, apply
      + extend the strategy, dedup, template, caveat convention, entry caps, open its PR,
      update the effectiveness log).
- [ ] `README.md` documents cadence, manual trigger, permission fix, candidate finder,
      search-strategy doc, and the playbook.

## Context
The survey is curated (26 datasets, tiered: CT, CXR, mammography FFDM+DBT, MR, fundus,
MSK, PE). Two kinds of staleness need different treatment: **link rot / access changes**
(deterministic → fully automatable) and **missing newly-published datasets** (needs web
search + curation judgment → not safe to fully automate).

The original survey was a single-pass effort, so its discovery net was relatively narrow.
The user wants the discovery to be **much more extensive and to keep improving**: cast a
wide net across many channels — **Semantic Scholar** (search + citation graph), OpenAlex,
Europe PMC, and the open dataset repositories (Zenodo, Figshare, HuggingFace, PhysioNet,
TCIA, grand-challenge, Papers With Code, OpenNeuro, Kaggle) — and **document good
database-search methods in a living strategy file that evolves**, recording which channels
and queries actually surface real new datasets so the search gets better each run. The
split that makes this tractable: a scriptable **candidate finder** does the wide,
repeatable *fetching* automatically each week; the **agent playbook** does the *curation*
and *feeds back* what worked into the strategy doc. This pushes the resource toward the
"ongoing discovery surface" direction (in the spirit of the Radiology Opportunities
Tracker) without pretending a CI runner can do curation it can't.

The single most important reuse from that project: confirm the workflow PR-creation
permission is ON, or the cron will run green every week and silently fail at the final
PR step.
