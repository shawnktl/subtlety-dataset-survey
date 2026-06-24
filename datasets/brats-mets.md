# BraTS-METS (2023)

- **Tier:** C — adjacent / partial signal (canonically subtle small-lesion finding; consensus labels)
- **Modality / anatomy:** Brain multiparametric MRI (T1, T2, FLAIR, T1-post-Gd) / brain — metastases
- **Finding type:** Untreated brain metastases (pre-treatment), small-lesion segmentation

## Subtlety / perceptibility label
No explicit subtlety field. Small brain metastases are canonically subtle and easily missed; the set covers **3,076 lesions across 402 public studies**, many small. Annotation is a layered human pipeline rather than independent per-rater masks, so the signal is canonical subtlety, not preserved disagreement.

## Label provenance
Stepwise: UNet pre-segmentation → annotator → 1–2 board-certified neuroradiologists → single senior neuroradiologist QC. Pool of ~150 annotators + 50 attendings (ASNR). Final single consensus per case.

## Size
402 public training studies (3,076 lesions); +31 validation (139 lesions), +59 test (218 lesions) held out.

## Access / licensing
Public training set on **Synapse** (registration / Synapse account + challenge data terms). Validation/test labels withheld. Paper: Moawad et al., "BraTS-METS Challenge 2023," arXiv:2306.00838, https://arxiv.org/abs/2306.00838

## Caveats
- Only training labels public; consensus annotation (no per-rater disagreement masks).
- Registration required.

## Relevance to detectability
Extends the BraTS family into the small-metastasis regime — the canonical "don't miss the tiny enhancing lesion" detectability problem in brain MRI. Useful as a difficulty-stratifiable (by lesion size/count) mets corpus, paired with UCSF-BMSR for scale.
