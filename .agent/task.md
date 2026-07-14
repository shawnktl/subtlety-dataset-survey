# 🚨 DISPATCH METADATA — read before doing anything else

| field | value |
|---|---|
| **Branch** | `agent/subtlety-dataset-search-lung-nodule-subsection` |
| **Project slug** | `subtlety-dataset-search` |
| **Spec** | `task:lung-nodule-subsection` |

## Required behavior

- **Push commits to `agent/subtlety-dataset-search-lung-nodule-subsection` and only `agent/subtlety-dataset-search-lung-nodule-subsection`.** Do NOT invent a
  shorter or "cleaner" branch name. The rounds-repo status tracker matches
  PRs by exact branch name; any other name leaves the PR orphaned in
  tracking and requires manual fixup.
- **Open the PR with `agent/subtlety-dataset-search-lung-nodule-subsection` as head** against the repo's default branch
  as base.
- The branch already exists (the dispatch script created it before
  handing off to you). You're already checked out on it — just commit and
  push. No `git checkout -b` needed.

---

# Original spec

# Agent Task — Lung-Nodule (Segmented) Subsection for External Validation

## Objective

Add a dedicated **lung-nodule subsection** to the subtlety-dataset survey repo
(`shawnktl/subtlety-dataset-survey`) that collects **every dataset in the survey containing
segmented lung nodules** — the datasets usable for **external validation** of the
`nodule-detectability` classifier. "Done" = a curated subsection page (markdown + rendered into
the existing `docs/` site) listing each qualifying dataset with the segmentation/label details
that determine whether it can serve as an external-validation set.

This directly serves `nodule-detectability`, where external validation is now the primary
scientific priority.

## Scope

**SHOULD touch (in `shawnktl/subtlety-dataset-survey`):**
- Add `datasets/` cross-links / a new `lung-nodules.md` (or `subsections/lung-nodules.md`) subsection page.
- Update `index.md` to link the new subsection.
- Rebuild the `docs/` site via the existing `scripts/build_site.py` (stdlib, deterministic — verify byte-identical rebuild).

**MUST NOT touch:**
- The auto-refresh infra / cron; unrelated datasets' pages.
- Do not fabricate datasets, segmentation availability, or licensing — every claim must be verifiable; flag anything uncertain with `[VERIFY]`.

## What qualifies for the subsection

A dataset belongs in the lung-nodule subsection if it contains **lung nodules with segmentation
masks** (not just bounding boxes or classification labels), since external validation of a
segmentation-derived detectability pipeline needs comparable segmentations. For each, capture:

- **Segmentation type** — voxel/pixel masks vs. contours vs. bbox-only (note if only bbox — it's a weaker fit).
- **Subtlety / perceptibility label** — present? (e.g. LIDC radiologist subtlety ratings) or absent.
- **Modality & count** — CT (expected majority); number of nodules/cases.
- **Access & license** — open / registered / restricted; redistribution terms.
- **External-validation fit** — a one-line verdict on how usable it is for validating the LIDC-trained detectability model (label comparability, domain shift caveats).

Start from the datasets already in the survey (LIDC-IDRI, LNDb, and others), then confirm
segmentation availability per dataset. Known strong candidates to check first: **LIDC-IDRI**
(masks + subtlety), **LNDb**, **NLST-derived segmentations**, **LUNA16** (LIDC-derived), **DLCSD**,
and any others in the index with lung-nodule segmentations — verify each rather than assuming.

## Tasks

1. Scan the existing survey for lung-nodule datasets; determine segmentation availability for each (verify, don't assume).
2. Write the subsection page with the per-dataset fields above and an external-validation-fit verdict.
3. Link it from `index.md`; rebuild `docs/` with `scripts/build_site.py` (byte-identical verify).
4. Preserve/propagate all `[VERIFY]` caveats; note any lung-nodule datasets excluded and why (e.g. bbox-only).

## Constraints

- Work on branch `agent/subtlety-dataset-search-lung-nodule-subsection`; commit prefix `agent:`; open a PR, don't push to master/main.
- No fabricated datasets/labels/licenses; `[VERIFY]` anything unconfirmed.
- Deterministic site rebuild (byte-identical on re-run).

## Acceptance Criteria

- [ ] A lung-nodule subsection page lists every survey dataset with segmented lung nodules, with segmentation type / subtlety-label / modality+count / access+license / external-validation-fit per dataset
- [ ] `index.md` links the subsection; `docs/` rebuilt deterministically via `build_site.py`
- [ ] Bbox-only or non-segmented lung datasets are explicitly excluded with reason
- [ ] No fabricated content; `[VERIFY]` flags preserved for anything unconfirmed
- [ ] PR opened on `shawnktl/subtlety-dataset-survey`

## Context

Consumer: `nodule-detectability` external validation (LIDC-trained detectability classifier
needs comparable segmented lung-nodule datasets to test generalization). The survey already
holds a 59-dataset cross-modality index; this carves out the lung-nodule-with-segmentation slice
as a purpose-built validation menu. Dispatch with
`python dispatch-agents.py --dispatch subtlety-dataset-search --spec task:lung-nodule-subsection`.
