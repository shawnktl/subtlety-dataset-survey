# FUMPE

- **Tier:** C — adjacent / partial signal (canonically subtle finding; no explicit perceptibility label)
- **Modality / anatomy:** CT pulmonary angiography (CTPA) / pulmonary arteries
- **Finding type:** Pulmonary embolism (segmented clot regions)

## Subtlety / perceptibility label
No explicit subtlety field. 2,304 of 3,438 annotated PE regions (67%) are peripheral/subsegmental — the canonically subtle, frequently-missed location. Authors frame it as a challenging CAD benchmark; includes per-case Qanadli obstruction scores (0–31), which are severity, not perceptibility.

## Label provenance
Two radiologists — a primary delineated PE in every slice; the senior department head re-examined and approved all segmentations (review/approval, not independent dual annotation with formal arbitration).

## Size
35 subjects; 8,792 slices; 3,438 PE ROIs (1,134 main / 2,304 peripheral).

## Access / licensing
Public, open. Figshare, CC BY 4.0: https://doi.org/10.6084/m9.figshare.c.4107803 (Kaggle mirror exists). DICOM + MAT masks. Paper: https://www.nature.com/articles/sdata2018180

## Caveats
- Small (35 patients); all PE-positive (no negative controls).
- One-delineates / one-approves, so reader disagreement is not quantified.

## Relevance to detectability
A segmentation-level PE set heavily weighted toward subsegmental clots — the subtle end of the PE spectrum — complementing RSNA-PE's scale and QA flags with voxel-level masks, though without an explicit perceptibility label.
