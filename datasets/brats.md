# BraTS

- **Tier:** B — reader-disagreement / multi-rater design (difficulty proxy)
- **Modality / anatomy:** Multi-sequence brain MRI / glioma tumor subregions
- **Finding type:** Glioma segmentation subregions

## Subtlety / perceptibility label
No explicit subtlety label. Multi-rater segmentation variance as proxy for region-level perceptibility. Inter-rater DSC reported at 0.74–0.85, encoding genuine segmentation ambiguity.

## Label provenance
1–4 raters per case for manual segmentation. 2024 BraTS extended to post-treatment glioma.

## Size
Thousands of cases across challenge years (2012–2025).

## Access / licensing
Open via the BraTS challenge / Synapse. https://www.synapse.org/brats

## Caveats
- Per-rater segmentations are usually consolidated to a single ground truth in distributed data; the disagreement-as-signal is mostly reported in the challenge papers, not always preserved per-voxel.
- No explicit subtlety label.

## Relevance to detectability
Multi-rater segmentation variance as proxy for region-level perceptibility. The closest thing to a "difficulty" signal in brain MRI.
