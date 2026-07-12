# WMH Segmentation Challenge (2017)

- **Tier:** B — reader-disagreement / multi-rater design (additional observers' per-rater masks preserved)
- **Modality / anatomy:** Brain MRI (FLAIR + T1) / white matter
- **Finding type:** White matter hyperintensities of presumed vascular origin

## Subtlety / perceptibility label
No numeric subtlety field, but WMH are canonically subtle, small, low-contrast foci — and **all 60 training cases carry independent manual masks from two additional observers (O3 and O4) beyond the reference standard, released alongside the data**, so per-rater disagreement is preserved. Reported inter-observer Dice ~0.79–0.80, and top automatic methods perform on par with individual human observers — i.e. the disagreement signal is real and quantified.

## Label provenance
Reference standard delineated under expert supervision (UMC Utrecht / NUHS Singapore / VU Amsterdam); two *additional* independent observers (O3, O4) manually segmented all training cases. Per-rater masks released, not just consensus.

## Size
60 training subjects (3 scanners) + 110 test subjects (5 scanners) = 170 total. FLAIR + T1 + ground-truth mask per subject.

## Access / licensing
Fully open, **no registration**. CC-BY-NC-4.0. Hosted on DataverseNL (8.2 GB zip; includes training data, test data, reference + additional-observer annotations). Challenge: https://wmh.isi.uu.nl/ ; data: https://doi.org/10.34894/AECRSD ; paper: Kuijf et al., *IEEE TMI* 2019, https://pubmed.ncbi.nlm.nih.gov/30908194/

## Caveats
- Additional-observer masks cover the **training set only** (test masks held by organizers).
- License is non-commercial.

## Relevance to detectability
A small-vessel-disease analogue to the MS multi-rater sets: extra independent observer masks on canonically subtle WMH foci give a clean per-rater-disagreement difficulty proxy on brain MRI, with the bonus that it is one-click open (no DUA).
