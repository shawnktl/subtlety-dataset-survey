# MS3SEG (MS MRI Tri-Mask Dataset)

- **Tier:** C — adjacent / partial signal (explicit subtle-vs-benign discrimination labeling; consensus, not multi-rater)
- **Modality / anatomy:** Brain MRI (T1, T2, T2-FLAIR; axial + sagittal), 1.5T / white matter
- **Finding type:** MS lesions, explicitly separated from confusable normal WMH via a tri-mask scheme

## Subtlety / perceptibility label
No numeric subtlety field, but the **tri-mask scheme directly targets a perceptibility/discrimination problem**: labels distinguish (1) ventricles, (2) "normal" age-related/CSF-contaminated WMH, and (3) "abnormal" WMH = MS lesions. The dataset is built around separating genuinely subtle pathological hyperintensities from benign look-alikes — a detectability-discrimination signal, even though it's consensus-labeled.

## Label provenance
Expert delineation on axial T2-FLAIR with "expert consensus review" + automated QC. Number of raters and consensus methodology not specified `[VERIFY]`.

## Size
100 MS patients (74 F / 26 M, ages 18–55), ~2,000 annotated slices.

## Access / licensing
**Open.** Dataset CC-BY-4.0 on Figshare (https://doi.org/10.6084/m9.figshare.30393475); code MIT (github.com/Mahdi-Bashiri/MS3SEG). Paper: Bashiri et al., *Scientific Data* 2026, https://www.nature.com/articles/s41597-026-07184-5

## Caveats
- Single scanner (Toshiba 1.5T), single Iranian cohort → limited generalizability.
- Rater count / consensus process unstated `[VERIFY]`; consensus labels, no per-rater masks (for preserved disagreement, see MSSEG-2016 / WMH Challenge).

## Relevance to detectability
A rare dataset whose label scheme *is* the perceptibility question — distinguishing subtle pathological WMH from benign mimics is exactly the discrimination at the heart of MS-lesion detectability. Openly licensed, complementing the DUA-gated MSSEG sets.
