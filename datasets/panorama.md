# PANORAMA (PDAC detection on CECT)

- **Tier:** C — adjacent / partial signal (canonically subtle / frequently-missed finding; reader study)
- **Modality / anatomy:** Portal-venous contrast-enhanced CT / pancreas
- **Finding type:** Pancreatic ductal adenocarcinoma (PDAC) detection + segmentation (6 PDAC-related structures)

## Subtlety / perceptibility label
No explicit subtlety field, but PDAC is the textbook subtle/missed abdominal cancer: CT sensitivity is only **58–77% for ≤2 cm tumors**, and in a missed-case series **42% of missed PDACs were <2 cm and 44% were isoattenuating** (do not stand out from normal parenchyma). PANORAMA's reader study directly benchmarks AI vs. abdominal radiologists, so detection difficulty is the explicit raison d'être.

## Label provenance
Segmentation masks + clinical info; reference standard is histopathology and ≥3-year follow-up. Annotated by radiologists, with the public Pancreas-CT (TCIA) cohort as one source. Consensus / reference-standard labels — not per-rater released for the training set `[VERIFY]` whether any reader-study per-reader data is public.

## Size
Public training/development set on Zenodo (records 13715870, 13742336, 11034011, 10999754); full study cohort "over 1,500 cases" multi-center.

## Access / licensing
Open (public training set on Zenodo + TCIA wiki). https://panorama.grand-challenge.org/ ; data: https://zenodo.org/records/13715870 ; method: https://arxiv.org/abs/2503.10068 . License CC BY 3.0 (TCIA) `[VERIFY Zenodo record license]`.

## Caveats
- No per-lesion subtlety label and (for the training set) no preserved per-reader disagreement — qualifies on the *canonically-subtle-finding* axis (PDAC miss-rate), not on explicit perceptibility annotation.
- See **CURVAS-PDACVI** for the multi-rater (5 per-rater masks) PDAC extension that reuses one PANORAMA annotation.

## Relevance to detectability
The reference public PDAC detection benchmark, anchored to a finding with hard, quantified miss-rate data — the abdominal poster child for "the finding is subtle even to experts." Pairs with CURVAS-PDACVI when preserved per-rater disagreement is needed.
