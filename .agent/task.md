# 🚨 DISPATCH METADATA — read before doing anything else

| field | value |
|---|---|
| **Branch** | `agent/subtlety-dataset-search-comprehensive-discovery-sweep` |
| **Project slug** | `subtlety-dataset-search` |
| **Spec** | `task:comprehensive-discovery-sweep` |

## Required behavior

- **Push commits to `agent/subtlety-dataset-search-comprehensive-discovery-sweep` and only `agent/subtlety-dataset-search-comprehensive-discovery-sweep`.** Do NOT invent a
  shorter or "cleaner" branch name. The rounds-repo status tracker matches
  PRs by exact branch name; any other name leaves the PR orphaned in
  tracking and requires manual fixup.
- **Open the PR with `agent/subtlety-dataset-search-comprehensive-discovery-sweep` as head** against the repo's default branch
  as base.
- The branch already exists (the dispatch script created it before
  handing off to you). You're already checked out on it — just commit and
  push. No `git checkout -b` needed.

---

# Original spec

# Agent Spec — Subtlety/Perceptibility Dataset Survey: Comprehensive Discovery Sweep (wider net)

## Objective
Substantially **expand** the dataset index beyond its current chest/breast-dominated 26. The
original survey (2026-06-01) was spawned from a lung-nodule project and scoped to datasets with
*explicit* subtlety labels, which biased it toward thoracic CT / CXR / mammography. This sweep
**casts a much wider net** — by anatomy/modality and by the *kind* of detectability signal — and
lands the new datasets in the existing repo structure. "Done" = the index meaningfully covers
neuro (esp. stroke), abdominal/body, and other under-represented areas, with every new entry
profiled and cited to the same standard as the existing pages.

## The two ways the net widens

### 1. Conceptual scope — include implicit detectability proxies, not just explicit "subtlety" fields
Keep the existing tiering but treat the following as **in-scope difficulty/detectability signal**,
not just a literal numeric "subtlety 1–5" field:
- Explicit subtlety / conspicuity / perceptibility labels (Tier A — as before).
- Multi-reader / multi-rater disagreement designs (Tier B difficulty proxy — as before).
- **Miss-rate / perceptual-error / "commonly missed finding" datasets** (e.g. retrospectively-missed
  cancers, satisfaction-of-search studies).
- **Eye-tracking / gaze datasets** (process-level perceptibility signal).
- **Hard/easy or difficulty-stratified subsets**, screening interval cancers, "subtle vs obvious"
  splits.
- Datasets where the *finding itself is canonically subtle/hard-to-detect* even without a label
  (e.g. early ischemic change / hyperdense vessel sign, small ICH, subtle fractures, small PE).

### 2. Coverage — explicitly hunt the gaps
Current coverage is ~15 chest, 6 breast, only 2 neuro (BraTS tumor, ISBI-MS), 2 MSK, 1 fundus,
1 prostate, and **zero stroke / zero abdominal-lesion**. Prioritize discovery in:
- **Neuro — STROKE especially**: ischemic stroke lesion (e.g. ISLES editions, ATLAS v2.0,
  AISD/acute-ischemic NCCT), intracranial hemorrhage (e.g. RSNA ICH, CQ500, BHSD), aneurysm
  (e.g. ADAM, CADA), plus white-matter/MS/mets where detectability is the question.
- **Abdomen / body**: liver lesions (e.g. LiTS), kidney (e.g. KiTS), pancreas (e.g. MSD-Pancreas,
  PANORAMA, TCIA pancreas), and multi-organ sets (e.g. MSD/Decathlon, AMOS, AbdomenCT-1K) where a
  detectability/conspicuity or multi-reader angle exists.
- **Other under-covered**: PE on CTPA (e.g. RSNA-PE), subtle fractures, pneumothorax, spine,
  cardiac — wherever a detectability/perceptibility or reader-disagreement signal is documented.

These are *leads, not a closed list* — use them to seed discovery, then go broader.

## Discovery method
1. **Check the repo first** for any existing candidate-finder script (`scripts/`, `.github/`) and the
   `notes/` files; if a finder exists, run/extend it. Do not assume a specific script name.
2. **Primary engine is web search.** Sweep multiple channels per the original strategy intent:
   literature (Semantic Scholar / OpenAlex / Europe PMC / PubMed + citation chasing on the existing
   Tier-A papers), and open dataset repositories (TCIA, PhysioNet, Zenodo, Figshare, HuggingFace,
   grand-challenge.org, Papers With Code, Kaggle, OpenNeuro, Synapse, OASIS, ADNI-style registries).
3. For each candidate, verify it actually carries a detectability/subtlety/disagreement signal (or is
   a canonically-subtle-finding dataset) **before** adding it — don't pad the index with generic
   segmentation sets that have no perceptibility angle. If borderline, note why and place in Tier C.

## Scope (files)
- SHOULD create: one new `datasets/<name>.md` per added dataset — **match the existing page format
  exactly** (open `datasets/brats.md` and `datasets/lidc-idri.md` as templates).
- SHOULD update: `index.md` (add rows to the right tier tables; update the "N public datasets" count
  and the scope blurb to reflect the wider net), `synthesis.md`/`PROJECT_SUMMARY.md`/`README.md`
  counts and the landscape read, and `notes/follow-ups.md`.
- SHOULD add: a short `notes/search-strategy.md` (if absent) or append to `notes/follow-ups.md` — a
  log of which channels/queries were run and what they surfaced, so the next sweep compounds.
- MUST NOT touch: the existing 26 dataset pages' content (except adding cross-links), the HTML build
  scripts, or the Pages workflow. Render/extend, don't rewrite.

## Tasks
1. Dedup against the existing 26 (don't re-add LIDC, BraTS, etc.).
2. Run the multi-channel discovery, gap-regions first (neuro/stroke, then abdomen/body, then other).
3. Write a cited per-dataset page for each genuine hit, slotted into the correct tier (A/B/C).
4. Update `index.md` tables + counts, the synthesis/README landscape read, and the notes log.
5. Aim for breadth: a successful sweep should add a substantial batch (target ≥15 new datasets if the
   signal supports it), with real stroke and abdominal representation. If a region genuinely lacks
   public detectability datasets, **say so explicitly** in the notes rather than padding.

## Constraints
- Work on branch `agent/subtlety-dataset-search-discovery-sweep`
- Commit with prefix `agent:`
- Don't push to main directly; open a PR when done
- Cite every dataset (paper / repo URL); flag unconfirmed claims `[VERIFY]`
- Preserve the existing tiering definitions and page format

## Acceptance Criteria
- [ ] Real **stroke** representation added (ischemic lesion and/or hemorrhage and/or aneurysm)
- [ ] Real **abdominal/body** lesion representation added (liver/kidney/pancreas/multi-organ)
- [ ] Each new dataset has a cited page in the existing format, slotted into the correct tier
- [ ] `index.md` count + scope blurb and the synthesis/README landscape read updated to match
- [ ] `notes/` records the channels/queries run and what they surfaced (so the next sweep compounds)
- [ ] No generic no-perceptibility-signal segmentation sets padded in without justification

## Context
This is the "much more exhaustive discovery" the user asked for on 2026-06-24, now unblocked because
PR #4 (auto-refresh machinery) merged. The driving use case is the broader detectability product
framing in `nodule-detectability` — knowing what data exists *across* anatomy (not just lung) shapes
whether the detectability framing generalizes. The user specifically flagged the absence of
neuro/stroke/body datasets as the gap to close.
