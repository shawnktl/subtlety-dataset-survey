# UCSF-BMSR (Brain Metastases Stereotactic Radiosurgery)

- **Tier:** C — adjacent / partial signal (canonically subtle small-lesion finding; consensus labels)
- **Modality / anatomy:** Brain MRI (T1 post-contrast, T1 pre-contrast, FLAIR, subtraction) / brain — metastases
- **Finding type:** Enhancing brain metastases (small-lesion detection)

## Subtlety / perceptibility label
No explicit subtlety field. A large-scale small-met detection corpus — **5,136 annotated brain metastases**, many sub-centimeter, the canonically hard "don't-miss-the-tiny-one" regime. It includes subtraction images precisely because subtle enhancing mets are hard to perceive. No multi-rater disagreement released.

## Label provenance
Expert voxelwise annotations of enhancing mets (UCSF); consensus/expert, not per-rater.

## Size
560 brain MRIs from 412 patients; 5,136 metastases.

## Access / licensing
**Public and freely available for non-commercial use; no DUA gating reported.** Mirrored on AWS Registry of Open Data: https://registry.opendata.aws/ucsf-bmsr/ . Paper: Rudie et al., *Radiology: AI* 2024, https://pubs.rsna.org/doi/full/10.1148/ryai.230126

## Caveats
- Single-institution; consensus annotation (no per-rater masks).
- Non-commercial.

## Relevance to detectability
The largest openly-mirrored small-brain-metastasis corpus — the inclusion of subtraction sequences is itself an acknowledgement that the finding sits at the perceptual threshold. A scale complement to BraTS-METS for studying tiny-lesion detectability on MR.
