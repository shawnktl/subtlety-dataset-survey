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

# Agent Spec — Subtlety/Perceptibility Dataset Survey Repo

## Objective
Turn the completed 26-dataset survey (in this project's `research-output.md`) into a
dedicated, browsable reference repo so the dataset landscape is organized at the
repo level rather than living in a single markdown file. "Done" = a `knowledge-base`
repo populated with one page per dataset, a tier-ranked index, access/licensing notes,
and a crosswalk to the detectability framing — delivered as a PR on
`shawnktl/subtlety-dataset-survey`.

## Source of truth
The authoritative content is `projects/subtlety-dataset-search/research-output.md` in
the task-rounding repo. The dispatching step copies the project's spec to the target
repo as `.agent/task.md`; the agent should also be given (or fetch) the
`research-output.md` content as the input corpus. Do NOT re-research from scratch —
restructure and lightly verify what's already there. Preserve every "verify directly
before relying on" caveat already flagged in the survey.

## Scope
**SHOULD create / populate:**
- `datasets/<dataset-id>.md` — one page per dataset (26 total). Each page: name, modality,
  finding type, the subtlety/perceptibility/conspicuity label it carries, label provenance,
  size, access conditions/licensing, tier (A/B/C), and a one-line "relevance to detectability."
- `index.md` (or `study/topics.md` per the bootstrap convention) — tier-ranked table linking
  to each dataset page. Tier A = direct subtlety/conspicuity labels (LIDC-IDRI, JSRT, CBIS-DDSM,
  LNDb, OPTIMAM/OMI-DB); Tier B/C below.
- `notes/follow-ups.md` — the top-3 follow-ups (CheXthought; JSRT+LNDb external-validation
  pairing; CBIS-DDSM → OPTIMAM mammography) and the major gap (MR-with-subtlety-labels).
- `resources/sources.md` — links/citations for each dataset's source page.
- `PROJECT_SUMMARY.md` — scope (publicly available datasets annotating finding subtlety/
  perceptibility/conspicuity), why (broader detectability product/pipeline framing from
  `nodule-detectability`), and how the repo is used.

**MUST NOT touch:**
- `BOOTSTRAP.md`, `CLAUDE.md`, `scripts/` — provided by the knowledge-base bootstrap; leave as-is.

## Tasks
1. Read `BOOTSTRAP.md` / `CLAUDE.md` to understand the knowledge-base layout.
2. Parse `research-output.md` into the 26 per-dataset pages under `datasets/`.
3. Build the tier-ranked `index.md` linking every dataset page.
4. Write `notes/follow-ups.md` (top-3 + the MR gap) and `resources/sources.md`.
5. Fill `PROJECT_SUMMARY.md`.
6. Carry forward every "verify before relying on" caveat verbatim onto the relevant dataset page.
7. Open a PR from the work branch.

## Constraints
- Work on branch `agent/subtlety-dataset-search`.
- Commit with prefix `agent:`.
- Open a PR when done; do not push to `main` directly.
- Do not invent datasets or labels not present in the source survey.

## Acceptance Criteria
- [ ] One `datasets/<id>.md` page exists per dataset in the survey (≈26), each with tier + access + relevance fields.
- [ ] `index.md` ranks datasets by tier and links every page.
- [ ] `notes/follow-ups.md` captures the top-3 follow-ups and the MR-subtlety gap.
- [ ] All prior "verify directly" caveats are preserved.
- [ ] `BOOTSTRAP.md`, `CLAUDE.md`, `scripts/` unchanged.
- [ ] A PR is open from `agent/subtlety-dataset-search`.

## Context
Spawned from `nodule-detectability`. The downstream consumer is the broader
detectability product framing (patent-lawyer interest, MAE-band vs k-NN output). The
repo's value is making "what labeled data exists across modalities/findings" answerable
at a glance, so the framing's generality (or nodule-specificity) is easy to reason about.
