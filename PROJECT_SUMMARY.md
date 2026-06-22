# Project Summary — Subtlety / Perceptibility Dataset Survey

## Scope

A browsable reference of **publicly available radiology datasets that annotate finding subtlety / perceptibility / conspicuity** — or that carry a usable difficulty proxy (reader disagreement, multi-rater designs, process-level eye-tracking signal). 26 datasets surveyed, tier-ranked A/B/C and given one page each under `datasets/`.

The survey deliberately distinguishes three tiers:

- **Tier A — direct subtlety/conspicuity label** (LIDC-IDRI, JSRT, CBIS-DDSM, LNDb, OPTIMAM/OMI-DB). A dataset carries an explicit numeric or categorical subtlety/conspicuity field.
- **Tier B — reader-disagreement / multi-rater design** (VinDr-CXR, VinDr-Mammo, MURA, BraTS, Messidor-2, OAI, MIDRC/RICORD, PI-CAI; plus CheXthought as an A/B hybrid). No explicit subtlety field, but label noise / inter-reader disagreement encodes ambiguity.
- **Tier C — adjacent / partial signal** (REFLACX, EGD-CXR, FG-CXR, NLST, SIIM-ACR, BCS-DBT, EMBED, INbreast, PadChest, CheXpert, NIH ChestX-Ray14, ISBI/MS). Weaker fit — process-level signal, derivable subsets, or no perceptibility axis at all.

## Why

Spawned from `nodule-detectability`. The downstream consumer is the broader **detectability product/pipeline framing** (patent-lawyer interest; MAE-band vs k-NN output). The current anchor source is LIDC-IDRI's per-nodule 1–5 subtlety rating. The open question driving this survey: **how general is the detectability framing across modalities and findings, vs how nodule/CT-specific is it?**

This repo makes "what labeled data exists across modalities/findings" answerable at a glance, so the framing's generality is easy to reason about. Two key conclusions surfaced:

1. The direct-subtlety landscape is **small** — outside LIDC, only JSRT, CBIS-DDSM, LNDb, and OPTIMAM carry a direct subtlety/conspicuity label.
2. There is a clear **MR-with-explicit-subtlety-labels gap** (no public dataset found), which is the sharpest "may be CT-specific" risk for the broader framing. See `notes/follow-ups.md`.

The single highest-leverage new discovery is **CheXthought** (Stanford AIMI) — chain-of-thought reasoning + visual attention + multi-reader disagreement at 50k-CXR / 501-radiologist scale, which operationalizes perceptibility as behavior.

## How the repo is used

- **`index.md`** — start here. Tier-ranked table linking every dataset page with modality, label, size, and access at a glance.
- **`datasets/<id>.md`** — one page per dataset: modality/anatomy, finding type, the subtlety/perceptibility/conspicuity label it carries, label provenance, size, access/licensing, tier, caveats (including all preserved "verify directly before relying on" flags), and a one-line relevance-to-detectability.
- **`notes/follow-ups.md`** — the top-3 follow-ups (CheXthought; JSRT+LNDb external-validation pairing; CBIS-DDSM → OPTIMAM mammography) and the major MR-subtlety gap, plus the other surveyed gaps.
- **`resources/sources.md`** — links/citations for each dataset's source page.

## Provenance

Built by restructuring the completed survey in `research-output.md` (from `nodule-detectability`'s task-rounding project). No re-research from scratch; every "verify directly before relying on" caveat from the original survey is preserved on the relevant dataset page. Datasets and labels are reported only as they appear in the source survey.

## Note on the bootstrap template

This repo was scaffolded from the generic `knowledge-base` study template, so `BOOTSTRAP.md`, `CLAUDE.md`, `scripts/`, `study/`, and `review/` describe a spaced-repetition study system rather than this dataset reference. Those files are left as-provided per the dispatch spec's MUST-NOT-touch list. The authoritative structure for this repo is `index.md` + `datasets/` + `notes/` + `resources/sources.md` + this summary.
