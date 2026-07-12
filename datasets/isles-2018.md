# ISLES 2018

- **Tier:** C — adjacent / partial signal (canonically hard finding; modality-mismatch difficulty, segmentation-only)
- **Modality / anatomy:** CT Perfusion (CTP source + derived maps), DWI-MRI–derived ground truth / brain — acute infarct core
- **Finding type:** Acute ischemic infarct core (segmentation from CTP)

## Subtlety / perceptibility label
No explicit subtlety field. The infarct core on CTP is canonically hard to delineate, and the ground truth comes from **DWI-MRI acquired a median 37 min after the CTP** (because the core is more reliably seen on DWI than CTP). The modality-mismatch — label from MRI, image is CT — is precisely a detectability gap, but it is inferred, not labeled. Multi-center (4 centers) adds scanner variability.

## Label provenance
Core lesions manually outlined on DWI-MRI by experts; transferred as ground truth for CTP. `[VERIFY]` rater count (likely single expert per case).

## Size
103 cases; 94 labeled training images from 63 patients / 62 testing images from 40 patients.

## Access / licensing
Public; bundled on Zenodo with the 2015/2017 editions. https://zenodo.org/records/17736412 ; challenge: http://www.isles-challenge.org/ISLES2018/ ; paper: Hakim et al., *Stroke* 2021, https://pmc.ncbi.nlm.nih.gov/articles/PMC8240494/

## Caveats
- No multi-rater disagreement published; no explicit subtlety label.
- Difficulty signal is the CTP-vs-DWI modality gap, inferred not labeled.

## Relevance to detectability
The CT-perfusion ischemic-core edition of ISLES, where the ground truth is deliberately drawn from a *more sensitive* modality (DWI) than the input (CTP) — a clean built-in illustration of a perceptibility gap between modalities, useful for asking how much a model can recover a finding that is barely visible on the supplied image.
