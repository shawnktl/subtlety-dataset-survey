# KiTS21 (2021 Kidney Tumor Segmentation Challenge)

- **Tier:** B — reader-disagreement / multi-rater design (three independent per-ROI annotations preserved)
- **Modality / anatomy:** Corticomedullary-phase contrast-enhanced CT / kidneys — renal masses
- **Finding type:** Renal tumor + renal cyst (with kidney segmentation)

## Subtlety / perceptibility label
No numeric subtlety field, but the strongest abdominal disagreement signal in the survey: KiTS21 introduced a **novel multi-annotation protocol collecting three independent annotations per region of interest** (kidney, tumor, cyst), each delineation done transparently via a public web tool. Because three independent delineations exist per ROI, inter-rater variability is captured rather than fused away — and renal cyst-vs-tumor boundaries and small-mass margins are exactly where readers disagree.

## Label provenance
3 independent expert annotators per ROI. The released `aggregated_*` masks combine the three, but the **three separate delineations are themselves released**, so per-rater disagreement is recoverable. `[VERIFY]` the canonical aggregation method (majority-vote vs sampling).

## Size
300 publicly released training cases; 100 held-out (non-public) test cases.

## Access / licensing
Open; training data public. kits-challenge.org / GitHub (neheller/kits21). https://kits-challenge.org/kits21/ ; paper: https://arxiv.org/abs/2307.01984 . License CC BY-NC-SA per challenge terms `[VERIFY exact tag]`.

## Caveats
- Test set private; the per-rater structure is in training cases only.
- `[VERIFY]` exact label-aggregation method and license tag.

## Relevance to detectability
The cleanest preserved-per-rater multi-annotation set in the body region: three independent delineations per ROI make it a direct kidney analogue of the chest multi-rater label-vector datasets (VinDr-CXR, MURA), usable to derive a region-level difficulty/ambiguity proxy from genuine inter-expert disagreement.
