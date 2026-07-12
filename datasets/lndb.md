# LNDb — Lung Nodule Database

- **Tier:** A — direct subtlety/perceptibility/conspicuity label
- **Modality / anatomy:** Thoracic CT / pulmonary nodules
- **Finding type:** Lung nodules

## Subtlety / perceptibility label
LIDC-style per-nodule ratings including **subtlety**, plus calcification, internal structure, lobulation, malignancy, margin, sphericity, spiculation, texture.

## Label provenance
Multi-reader: 5 radiologists (≥4 yrs experience) participated; each scan read by ≥1 radiologist.

## Size
294 CT scans (CHUSJ, Porto, Portugal, 2016–2018). v4 (2024) extends with annotations mined from clinical reports.

## Access / licensing
Open via Zenodo and grand-challenge.org (LNDb Challenge). https://lndb.grand-challenge.org/

## Caveats
- Smaller than LIDC; designed as a complementary external dataset.
- Multi-reader coverage is uneven (not all scans read by all 5).
- **Verify before relying on:** "each scan read by ≥1 radiologist" implies uneven multi-reader coverage. Verify per-nodule multi-reader coverage before using LNDb as a multi-rater dataset.

## Relevance to detectability
Direct subtlety label, natural external-validation pairing with LIDC (same modality, same labeling scheme — closest match for running an LIDC-trained pipeline).
