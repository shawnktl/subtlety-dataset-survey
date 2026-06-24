# ISLES 2022

- **Tier:** B — reader-disagreement / multi-rater design (difficulty proxy) + deliberate subtle-lesion inclusion
- **Modality / anatomy:** Multi-modal MRI (DWI b=1000, ADC, FLAIR) / brain — acute & sub-acute ischemic stroke lesion
- **Finding type:** Ischemic infarct lesion (segmentation)

## Subtlety / perceptibility label
No numeric subtlety field, but two genuine difficulty signals: (1) the dataset **intentionally includes "punctiform infarcts"** from embolic patterns, explicitly flagged in the data paper as time-consuming to annotate and frequently overlooked by algorithms — a deliberate small/subtle-lesion difficulty inclusion; and (2) a documented inter-rater study (two expert neuroradiologists, 16+ and 10+ yr, on 10 cases) quantifying disagreement. Multi-vendor / multi-field-strength (Philips 3T; Siemens 3T and 1.5T) across 3 centers adds real scanner variability.

## Label provenance
Hybrid pipeline: 3D U-Net pre-segmentation → trained medical students edit → neuroradiology resident revision → final approval by 1 of 3 senior neuroradiologists (>10 yr each). Inter-rater analysis on 10 cases. Released ground truth = single expert-approved mask (not independent per-rater masks).

## Size
400 cases total; 250 training (public) / 150 test (withheld).

## Access / licensing
Open — training set (n=250) under CC-BY-4.0 on Zenodo (DOI 10.5281/zenodo.7153326). Challenge: https://isles22.grand-challenge.org/ ; data paper: Hernandez Petzsche et al., *Scientific Data* 2022, https://www.nature.com/articles/s41597-022-01875-5

## Caveats
- Inter-rater agreement was measured on only 10 cases and is not distributed as per-case disagreement labels; the final release is consensus-style single masks, so reader disagreement is *documented* but not *preserved per-case*.
- The subtlety signal (punctiform infarcts) is described in the paper, not provided as a per-lesion label.

## Relevance to detectability
The flagship modern ischemic-stroke MRI benchmark, and the most useful ISLES edition for detectability: its authors deliberately retained the small/subtle punctiform lesions most pipelines drop, and measured inter-reader agreement explicitly. The closest stroke-MRI analogue to a difficulty-stratified subset.
