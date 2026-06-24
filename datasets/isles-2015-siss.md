# ISLES 2015 (SISS)

- **Tier:** B — reader-disagreement / multi-rater design (two independent ground-truth sets)
- **Modality / anatomy:** Multi-spectral MRI (T1w, T2w, DWI, FLAIR) / brain — sub-acute ischemic stroke lesion
- **Finding type:** Sub-acute ischemic infarct (segmentation)

## Subtlety / perceptibility label
No numeric subtlety field, but the SISS sub-challenge released **two independent expert ground-truth segmentation sets** (not merged into one consensus mask), so inter-rater disagreement is preserved in the data. Sub-acute infarcts are canonically subtle on any single sequence — defined only by concomitant signal across FLAIR + DWI — and the two-center origin adds scanner variability.

## Label provenance
Manual segmentation by an experienced MD; two separate ground-truth sets provided per case.

## Size
64 sub-acute cases (28 train / 36 test) for the SISS sub-challenge. (The SPES sub-challenge is a separate perfusion-estimation task.)

## Access / licensing
Public via the challenge site and a Zenodo bundle of the 2015–2018 editions. https://www.isles-challenge.org/ISLES2015/ ; Zenodo bundle: https://zenodo.org/records/17736412 ; paper: Maier et al., *Medical Image Analysis* 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5099118/

## Caveats
- The "two ground-truth sets" are the real multi-rater signal, but per-rater voxel-level disagreement is not published as a difficulty score — disagreement is inferable, not labeled. `[VERIFY]` whether both rater masks are distributed in the public release vs. only used for scoring.
- Test masks historically withheld.

## Relevance to detectability
One of the few stroke datasets that ships *two* independent expert tracings rather than a single fused ground truth — a built-in inter-rater-variability substrate on a canonically subtle finding. Pairs naturally with ISLES 2022 for a cross-edition difficulty comparison.
