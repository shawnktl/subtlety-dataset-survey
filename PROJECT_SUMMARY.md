# Project Summary — Subtlety / Perceptibility Dataset Survey

## Scope

A browsable reference of **publicly available radiology datasets that carry a finding subtlety / perceptibility / conspicuity signal** — read broadly: explicit subtlety/conspicuity labels, usable difficulty proxies (reader disagreement, multi-rater designs, process-level eye-tracking), miss-rate / perceptual-error studies, difficulty-stratified subsets, and datasets whose *finding is canonically subtle/hard-to-detect* even without a label. **59 datasets** surveyed, tier-ranked A/B/C and given one page each under `datasets/`. Originally 26 (chest/breast-dominated); a 2026-06-24 discovery sweep added 33 across neuro (esp. stroke), abdomen/body, and other under-represented regions.

The survey deliberately distinguishes three tiers:

- **Tier A — direct subtlety/conspicuity/difficulty label (8)** (LIDC-IDRI, JSRT, CBIS-DDSM, LNDb, OPTIMAM/OMI-DB; + **AISD** clear/blurred/invisible infarct conspicuity, **CPAISD** perceptibility-defined NCCT, **RSNA-PE** per-exam QA/mimic flags). A dataset carries an explicit numeric or categorical subtlety/conspicuity/difficulty field.
- **Tier B — reader-disagreement / multi-rater design (20)** (VinDr-CXR, VinDr-Mammo, MURA, BraTS, Messidor-2, OAI, MIDRC/RICORD, PI-CAI; + **CQ500**, **ISLES 2022 / 2015-SISS**, **KiTS21**, **CURVAS**, **CURVAS-PDACVI**, **MSSEG-2016**, **WMH Challenge**, **QUBIQ**, **VerSe/Genant**, **ChestX-Det**, **CAMUS**; plus CheXthought as an A/B hybrid). No explicit subtlety field, but label noise / inter-reader disagreement encodes ambiguity — strongest when per-rater annotations are preserved (MSSEG-2016's 7 raters, QUBIQ, KiTS21, CURVAS/-PDACVI, WMH, CQ500 all release per-rater data).
- **Tier C — adjacent / partial signal (30)** (REFLACX, EGD-CXR, FG-CXR, NLST, SIIM-ACR, BCS-DBT, EMBED, INbreast, PadChest, CheXpert, NIH ChestX-Ray14, ISBI/MS; + **CT-ScanGaze** (3D gaze), **ATLAS v2.0**, **ISLES 2018**, **RSNA ICH**, **PhysioNet CT-ICH**, **BHSD**, **ADAM**, **CADA**, **BraTS-METS**, **UCSF-BMSR**, **MS3SEG**, **PANORAMA**, **LiTS**, **FUMPE**, **RSNA Cervical Spine**, **RibFrac**, **GRAZPEDWRI-DX**, **FracAtlas**). Weaker fit — process-level signal, derivable subsets, canonically-subtle findings without an explicit label, or detection challenges.

## Why

Spawned from `nodule-detectability`. The downstream consumer is the broader **detectability product/pipeline framing** (patent-lawyer interest; MAE-band vs k-NN output). The current anchor source is LIDC-IDRI's per-nodule 1–5 subtlety rating. The open question driving this survey: **how general is the detectability framing across modalities and findings, vs how nodule/CT-specific is it?**

This repo makes "what labeled data exists across modalities/findings" answerable at a glance, so the framing's generality is easy to reason about. Key conclusions, updated after the 2026-06-24 wider-net sweep:

1. The **explicit direct-subtlety landscape remains small but is no longer chest-only** — outside the original chest/breast set (LIDC, JSRT, CBIS-DDSM, LNDb, OPTIMAM), the sweep found three genuine explicit-label datasets in new regions: **AISD** (NCCT ischemic infarct graded clear/blurred/invisible — the closest neuro analogue to LIDC's 1–5 scale), **CPAISD** (a perceptibility-*defined* NCCT stroke set), and **RSNA-PE** (per-exam QA / PE-mimic difficulty flags). The MR-with-explicit-subtlety gap is partially eased on the *disagreement* axis but not the *labeled-subtlety* axis.
2. The **multi-rater / reader-disagreement signal generalizes well across anatomy** — the strongest new assets preserve per-rater annotations: **MSSEG-2016** (7 raters, brain MS), **QUBIQ** (per-rater by design), **KiTS21** (3 per-ROI, kidney), **CURVAS / CURVAS-PDACVI** (3–5 raters, abdomen/pancreas), **WMH Challenge** (extra observers), and **CQ500** (3 reads released, head CT). These are the cleanest cross-modality external-validation substrates for the detectability framing.
3. **The stroke and abdominal gaps flagged in the original survey are now closed** — 6 ischemic-stroke and 5 abdominal datasets added (both were 0). **PDAC** (PANORAMA / CURVAS-PDACVI) and **early ischemic change** (AISD / CPAISD) are the standout "canonically subtle, well-documented miss-rate" findings outside the chest.

The single highest-leverage original discovery remains **CheXthought** (Stanford AIMI). The standout new cross-anatomy additions are **AISD** (explicit graded infarct conspicuity), **CURVAS-PDACVI** (subtle PDAC + 5 preserved per-rater masks), and **MSSEG-2016** (7-rater brain-MR disagreement). See `notes/follow-ups.md` for next moves and `notes/search-strategy.md` for the discovery log.

## How the repo is used

- **`index.md`** — start here. Tier-ranked table linking every dataset page with modality, label, size, and access at a glance.
- **`datasets/<id>.md`** — one page per dataset: modality/anatomy, finding type, the subtlety/perceptibility/conspicuity label it carries, label provenance, size, access/licensing, tier, caveats (including all preserved "verify directly before relying on" flags), and a one-line relevance-to-detectability.
- **`notes/follow-ups.md`** — the top-3 follow-ups (CheXthought; JSRT+LNDb external-validation pairing; CBIS-DDSM → OPTIMAM mammography) and the major MR-subtlety gap, plus the other surveyed gaps.
- **`resources/sources.md`** — links/citations for each dataset's source page.

## Provenance

Built by restructuring the completed survey in `research-output.md` (from `nodule-detectability`'s task-rounding project). No re-research from scratch; every "verify directly before relying on" caveat from the original survey is preserved on the relevant dataset page. Datasets and labels are reported only as they appear in the source survey.

## Note on the bootstrap template

This repo was scaffolded from the generic `knowledge-base` study template, so `BOOTSTRAP.md`, `CLAUDE.md`, `scripts/`, `study/`, and `review/` describe a spaced-repetition study system rather than this dataset reference. Those files are left as-provided per the dispatch spec's MUST-NOT-touch list. The authoritative structure for this repo is `index.md` + `datasets/` + `notes/` + `resources/sources.md` + this summary.
