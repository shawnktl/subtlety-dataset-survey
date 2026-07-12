# ChestX-Det

- **Tier:** B — reader-disagreement / multi-rater design (blinded double-read + adjudication)
- **Modality / anatomy:** Frontal CXR (subset of NIH ChestX-ray14) / thorax
- **Finding type:** Instance-level boxes + segmentation for 10 thoracic abnormalities (Atelectasis, Calcification, Consolidation, Effusion, Emphysema, Fibrosis, Fracture, Mass, Nodule, Pneumothorax)

## Subtlety / perceptibility label
No numeric subtlety field, but a genuine multi-reader-difficulty design: **two radiologists independently and mutually-blind annotated each image, with a third (most senior) adjudicating**, explicitly capturing and resolving inter-reader localization disagreement. Several of the 10 categories (pneumothorax, small nodules, fractures) are canonically subtle, now with instance-level localization.

## Label provenance
3 board-certified radiologists; blinded double-read + 1-reader adjudication. Output is adjudicated consensus (raw per-rater files not clearly released `[VERIFY]`).

## Size
3,543 images (ChestX-Det10), drawn from NIH ChestX-ray14. An extended release reports ~3,578 images / 13 categories `[VERIFY exact count vs the 10-category version]`.

## Access / licensing
Public. GitHub: https://github.com/Deepwise-AILab/ChestX-Det10-Dataset (Kaggle mirror). Underlying images from NIH ChestX-ray14 (already covered); ChestX-Det adds the new instance annotations. Paper: https://arxiv.org/pdf/2006.10550

## Caveats
- Images are a subset of an already-covered dataset (NIH ChestX-Ray14); the novelty is the adjudicated instance annotations, not new images.
- Per-rater raw labels not clearly published `[VERIFY]`.
- Small (~3.5k).

## Relevance to detectability
Adds instance-level (box + mask) localization with a blinded-double-read + adjudication protocol on top of NIH ChestX-ray14 — turning a label-quality-critiqued classification set into a localization set with documented inter-reader disagreement on subtle findings.
