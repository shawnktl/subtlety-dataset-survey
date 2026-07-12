# CURVAS (MultiRater MultiOrgan Abdominal CT)

- **Tier:** B — reader-disagreement / multi-rater design (per-rater masks preserved)
- **Modality / anatomy:** Contrast-enhanced abdominal CT / pancreas, kidney, liver
- **Finding type:** Multi-organ segmentation (organ boundaries)

## Subtlety / perceptibility label
No lesion/conspicuity label — qualifies purely on the disagreement axis, and strongly so. CURVAS is built explicitly around inter-rater disagreement and model calibration: each scan has **three independent expert-radiologist segmentations preserved as separate files**, and the associated MICCAI 2024 challenge is the first to benchmark segmentation accuracy *and* calibration *under* multi-rater uncertainty rather than fusing labels. Pancreas boundary disagreement is the canonical hard case.

## Label provenance
3 expert radiologists per case; per-rater annotations preserved (not consensus-only).

## Size
90 contrast-enhanced CT scans (University Hospital Erlangen, Aug–Oct 2023).

## Access / licensing
Open. Nature *Scientific Data* descriptor s41597-025-06473-9 (2025): https://www.nature.com/articles/s41597-025-06473-9 ; data via Zenodo / curvas.grand-challenge.org; challenge results: https://arxiv.org/abs/2505.08685 . License `[VERIFY exact tag — CC BY vs CC BY-NC-SA across sources]`.

## Caveats
- This is the dataset **behind the CURVAS challenge** — the Nature data descriptor and the challenge describe the same 90-scan cohort; one record, not two.
- Organ segmentation only — no lesion / perceptibility label; qualifies solely on the multi-rater disagreement axis.
- See **CURVAS-PDACVI** for the larger-rater-count PDAC extension.

## Relevance to detectability
A purpose-built multi-rater-disagreement / calibration substrate for abdominal CT — exactly the "how much do experts diverge, and is the model calibrated to that?" signal the detectability framing needs, on organs (esp. pancreas) where boundary perception genuinely differs reader-to-reader.
