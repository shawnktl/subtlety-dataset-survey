# VinDr-CXR

- **Tier:** B — reader-disagreement / multi-rater design (difficulty proxy)
- **Modality / anatomy:** CXR / 22 local findings, 6 global diagnoses
- **Finding type:** Thoracic findings (localized + global)

## Subtlety / perceptibility label
No explicit subtlety field, but inter-reader variance per finding is computable. 18,000 CXRs annotated by 17 experienced radiologists; each finding localized with bounding box.

## Label provenance
**Training set: 3 readers per case.** Test set: consensus of 5 readers. Disagreements adjudicated by 2 reviewers.

## Size
~100k retrospectively collected; 18k manually annotated.

## Access / licensing
Open via PhysioNet (credentialed). https://physionet.org/content/vindr-cxr/1.0.0/

## Caveats
- Reader-disagreement signal preserved in training set (3 independent reads).
- No explicit subtlety field.

## Relevance to detectability
Multi-rater design preserves disagreement signal; large enough for modeling.
