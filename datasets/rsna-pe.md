# RSNA-PE (RSNA-STR Pulmonary Embolism CT / "RSPECT")

- **Tier:** A — direct difficulty/quality label (per-exam QA / perceptibility flags)
- **Modality / anatomy:** CT pulmonary angiography (CTPA) / pulmonary arteries — thorax
- **Finding type:** Acute & chronic pulmonary embolism, with laterality, central/saddle location, RV/LV ratio (right-heart strain)

## Subtlety / perceptibility label
Carries an explicit **per-exam QA / difficulty / mimic label layer** (verified against the RSPECT paper): **QA-Motion**, **QA-Contrast** (insufficient arterial opacification to assess for PE), **Flow Artifact** (laminar-flow pseudo-defect — a PE mimic), **True Filling Defect (not PE)**, and **Indeterminate** (annotated with one or more QA labels). These are genuine annotation-quality / perceptibility / PE-mimic flags — a rare explicit "is this image even readable, and is the defect real or a mimic" axis. Separately, a bounding-box augmentation found 67.7% of newly-discovered previously-unlabeled emboli were subsegmental, confirming small/subsegmental PE is canonically subtle and frequently missed.

## Label provenance
>80 thoracic radiologists via the Society of Thoracic Radiology produced study-level (9 diagnostic + QA labels) and image-level ("PE present on image") annotations; distributed single-pass labeling (not a fixed multi-rater-per-case consensus). The augmentation added bounding boxes on 445 positive studies via 4 board-certified radiologists + 1 cardiothoracic adjudicator.

## Size
>12,000 CTPA studies contributed (5 international centers). Released challenge set: 9,446 exams / 2,322,685 images (train 7,279 / test 2,167).

## Access / licensing
Public, non-commercial (academic/education); no redistribution / re-identification, attribution required. Kaggle + RSNA MIRA portal (mira.rsna.org); AWS Open Data mirror. https://registry.opendata.aws/rsna-pulmonary-embolism-detection/ ; paper: https://pubs.rsna.org/doi/full/10.1148/ryai.2021200254

## Caveats
- QA flags are study-level annotation-quality / mimic labels, not a continuous per-finding conspicuity score. Image-level label is binary.
- Distributed single-pass labeling — not designed around per-case reader disagreement.
- The 67.7%-subsegmental figure is from the 445-study augmentation subset, not the whole corpus.

## Relevance to detectability
The QA/mimic flags operationalize a distinct axis from "subtlety of a present finding": *image readability* and *false-positive mimics* (flow artifact vs true clot). Combined with the canonically subtle subsegmental-PE finding, it's the strongest body-CT detectability asset and the closest thing to an explicit difficulty label outside chest radiography and LIDC.
