# PI-CAI

- **Tier:** C — adjacent / indirect signal (best modern prostate MRI dataset)
- **Modality / anatomy:** Multiparametric prostate MRI (T2W + ADC + DWI) / clinically significant prostate cancer
- **Finding type:** Clinically significant prostate cancer lesions

## Subtlety / perceptibility label
No explicit subtlety label per lesion. PI-RADS-style ambiguities (DCE enhancement criteria, etc.) exist but aren't surfaced as a per-lesion confidence field.

## Label provenance
Expert-derived lesion delineations on ~80% of cases. Histopathology + Gleason/ISUP as ground truth. Builds on PROSTATEx; superseded it.

## Size
10,000+ exams.

## Access / licensing
Open via Grand Challenge (challenge data) + DUA-gated. https://pi-cai.grand-challenge.org/

## Caveats
- No explicit subtlety label per lesion.
- Disagreement signal is indirect (PI-RADS vs histology).

## Relevance to detectability
Best available modern prostate MRI dataset, but disagreement signal is indirect.
