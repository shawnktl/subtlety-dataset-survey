# QUBIQ (Uncertainty Quantification for Biomedical Image Segmentation)

- **Tier:** B — reader-disagreement / multi-rater design (per-rater masks released by design)
- **Modality / anatomy:** Multi-modality / multi-organ — MRI (brain growth, brain tumor, prostate) + CT (kidney)
- **Finding type:** Mixed segmentation tasks; the survey-relevant subtasks are brain growth (MRI) and brain tumor (MRI)

## Subtlety / perceptibility label
No numeric subtlety field, but QUBIQ is **purpose-built around inter-rater uncertainty** — the entire challenge exists to model annotation disagreement, and **individual per-rater segmentations are released** (the FAQ explicitly references e.g. "Rater 3 in sub-task 02 of brain tumor"). Brain growth = 7 raters; brain tumor = 3 raters.

## Label provenance
Per-rater masks from multiple experts per task: brain growth (7 raters), brain tumor (3 raters), prostate (6 raters), kidney (3 raters). Per-rater, not consensus.

## Size
Brain growth: 34 train + 5 test. Brain tumor: 28 train + 4 test. (Prostate 33+15; kidney 20+4.) Small per task.

## Access / licensing
Public via Grand Challenge (qubiq21.grand-challenge.org); **registration ("Join") required**. https://qubiq21.grand-challenge.org/ ; paper: Menze et al., "QUBIQ," arXiv:2405.18435, https://arxiv.org/abs/2405.18435 . Dataset license `[VERIFY]`.

## Caveats
- Small case counts per task; only the brain subtasks are directly in-scope here.
- License unconfirmed `[VERIFY]`.

## Relevance to detectability
The most explicit "disagreement *is* the label" dataset in the survey — every task ships per-rater masks specifically so models can learn the uncertainty distribution. A direct testbed for treating inter-rater divergence as a difficulty/perceptibility signal, spanning brain MRI (and prostate/kidney beyond).
