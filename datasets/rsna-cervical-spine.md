# RSNA 2022 Cervical Spine Fracture Detection

- **Tier:** C — adjacent / partial signal (canonically missed finding / detection challenge)
- **Modality / anatomy:** CT / cervical spine (C1–C7)
- **Finding type:** Cervical spine fractures (presence + vertebral level + location)

## Subtlety / perceptibility label
No explicit subtlety field. Cervical spine fractures on CT are canonically high-stakes and easily missed in trauma; the dataset is a fracture-detection challenge. Difficulty is inherent to the finding, not a labeled perceptibility axis.

## Label provenance
Spine specialists from ASNR and ASSR. Study-level labels for all cases (fractured level from the original report, or "no fracture"), plus image-level bounding boxes on ~16% of positive cases. `[VERIFY]` exact per-case rater count / consensus protocol.

## Size
Full dataset 3,112 annotated CT studies (public training subset 2,019; test 1,093 with 847 fractures); >1,400 fractured studies; 12 institutions / 9 countries.

## Access / licensing
Public, non-commercial (research/education); no redistribution / re-identification. Kaggle: https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection ; AWS Open Data; RSNA MIRA. Paper: https://pubs.rsna.org/doi/full/10.1148/ryai.230034

## Caveats
- Cite "2,019 vs 3,112" carefully (public-train vs full).
- Only ~16% of positives have boxes.
- No subtlety grade; per-rater labels not exposed.

## Relevance to detectability
A large multi-institution benchmark for a canonically missed trauma finding — useful for the "easily-overlooked high-stakes finding" framing, though it offers a difficulty region rather than an explicit perceptibility label (for graded spine subtlety, see VerSe's Genant layer).
