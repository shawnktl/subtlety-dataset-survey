# MSSEG-2016 (MICCAI 2016 MS Lesion Segmentation)

- **Tier:** B — reader-disagreement / multi-rater design (7 raters, per-rater masks preserved)
- **Modality / anatomy:** Brain MRI (3D FLAIR, T1 pre/post-Gd, axial dual PD-T2) / white matter
- **Finding type:** Multiple sclerosis lesions (hyperintense on FLAIR)

## Subtlety / perceptibility label
No numeric subtlety field, but the **gold-standard multi-rater case in the survey**: each of the 53 cases was manually delineated by **7 expert raters, with all 7 per-rater masks released** alongside a derived consensus ground truth — genuine, large inter-rater disagreement. Per-expert-vs-consensus Dice fluctuates 69–77%, and the challenge paper documents automatic methods still trailing human inter-expert agreement. Small/peripheral MS lesions are canonically subtle.

## Label provenance
7 independent expert human raters per case (lesions delineated on FLAIR, controlled on T2), plus a derived consensus GT. Per-rater AND consensus masks both available.

## Size
53 patients total (15 train / 38 test), 4 centers/scanners, harmonized protocol.

## Access / licensing
Public via the **Shanoir** platform; **registration + signed data-usage agreement required** (GDPR-compliant). Not a one-click download. Paper: Commowick et al., "Multiple sclerosis lesions segmentation from multiple experts: The MICCAI 2016 challenge dataset," *NeuroImage* 2021, https://www.sciencedirect.com/science/article/pii/S1053811921008624 (also *Sci Rep* 2018: https://www.nature.com/articles/s41598-018-31911-7)

## Caveats
- Access gated behind DUA / registration (not anonymous-open). EU GDPR terms apply.
- Small case count (53).

## Relevance to detectability
The strongest preserved-per-rater multi-rater dataset of any modality in this survey — 7 independent expert delineations per case directly quantify how much experts diverge on subtle MS lesions. The reference substrate for "what does human-level disagreement look like" in brain MRI, and a strong external test of whether the detectability framing maps onto MR.
