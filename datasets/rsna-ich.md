# RSNA 2019 Intracranial Hemorrhage Detection (RSNA ICH)

- **Tier:** C — adjacent / partial signal (canonically subtle finding + large multi-expert effort; reconciled single label)
- **Modality / anatomy:** Non-contrast head CT (NCCT) / brain
- **Finding type:** Acute intracranial hemorrhage + 5 subtypes (EDH, IPH, IVH, SAH, SDH); slice-level binary labels

## Subtlety / perceptibility label
No explicit subtlety field. Small/early ICH (especially thin SDH, subtle SAH) is canonically easily missed on NCCT, and the construction paper explicitly discusses reader disagreement on subtle hemorrhages as a labeling challenge — but the released labels are reconciled to a single label per slice (no per-rater disagreement matrix published).

## Label provenance
~60 volunteer radiologists (American Society of Neuroradiology), each blind to other readers. Most exams received a single expert read with adjudication/multi-read on a subset; released labels are the reconciled ground truth (not per-rater). `[VERIFY]` exact per-exam reader count (most exams single-read, unlike CQ500's 3-per-exam).

## Size
25,272 CT examinations (~870,301 slices).

## Access / licensing
Open. Kaggle competition data + AWS Registry of Open Data; research/non-commercial competition terms. https://www.kaggle.com/c/rsna-intracranial-hemorrhage-detection ; https://registry.opendata.aws/rsna-intracranial-hemorrhage-detection/ ; paper: https://pubs.rsna.org/doi/10.1148/ryai.2020190211

## Caveats
- Slice-level subtype labels only, no segmentation masks.
- Per-rater labels not released (no disagreement signal preserved).
- Test-set labels withheld.

## Relevance to detectability
The largest public ICH corpus and the standard head-CT hemorrhage benchmark. For the detectability framing it provides scale on a canonically subtle finding, but — unlike CQ500 — its labels are reconciled, so it supplies a difficulty *region* rather than a disagreement *signal*.
