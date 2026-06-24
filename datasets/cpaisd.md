# CPAISD (Core-Penumbra Acute Ischemic Stroke Dataset)

- **Tier:** A — direct subtlety/perceptibility/conspicuity label (perceptibility-defined dataset)
- **Modality / anatomy:** Non-contrast CT (NCCT) / brain — hyperacute ischemic core & penumbra
- **Finding type:** Hyperacute ischemic core and penumbra (slice-level segmentation)

## Subtlety / perceptibility label
**The dataset is defined by perceptibility.** Its premise: for the absolute majority of cases the NCCT findings are *non-revealing* — a trained radiologist could **not** locate the ischemic area on NCCT alone. The annotator delineated core/penumbra only by cross-referencing CT-perfusion maps. By construction this is a "the finding is effectively invisible on the image" dataset — a perceptibility floor case.

## Label provenance
Single radiologist (10 yr experience) marked all sections, cross-referencing CT-perfusion maps to localize core and penumbra. No consensus / multi-rater methodology described.

## Size
112 patients (8,376 training slices / 980 validation / 809 test).

## Access / licensing
Open access. Zenodo: https://zenodo.org/records/10892316 ; code/weights: https://github.com/sb-ai-lab/early_hyperacute_stroke_dataset. Paper: Tuchinov et al., "CPAISD: Core-Penumbra Acute Ischemic Stroke Dataset," arXiv:2404.02518 (2024).

## Caveats
- Single rater — no inter-rater disagreement.
- The perceptibility signal is real and explicit at the *dataset* level (NCCT non-revealing), but the ground truth is perfusion-derived, so it labels what is *there*, not a per-region perceptibility grade like AISD's clear/blurred/invisible.
- Small patient count (112).

## Relevance to detectability
A near-pure "detectability floor" dataset: the labeled finding is, for most cases, invisible on the supplied NCCT. Useful as the extreme end of the subtlety spectrum — what does a model/reader do when the signal is genuinely below the perceptual threshold of the modality?
