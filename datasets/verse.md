# VerSe (VerSe'19 Fracture-Grading layer)

- **Tier:** B — ordinal subtlety axis (Genant grade) + documented multi-reader re-grading
- **Modality / anatomy:** Multi-detector CT / whole spine
- **Finding type:** Osteoporotic / compression vertebral fractures with Genant semiquantitative grade (0–3) + morphologic type (wedge / biconcave / crush)

## Subtlety / perceptibility label
The **Genant grade is itself an ordinal subtlety axis**: mild (grade 1, 20–25% height loss) fractures sit right at the perceptibility threshold, and osteoporotic vertebral compression fractures are the textbook "missed on CT" finding. The grading task is documented as high-disagreement, and a published **8-rater study (3 students / 3 residents / 2 attendings) re-graded this exact corpus** with Genant — direct reader-disagreement evidence on the same public images.

## Label provenance
Two neuroradiologists (5 and 17 yr) performed **consensus** grading in the base release. The released grades are consensus (not per-rater); the multi-rater signal lives in the downstream re-grading study (Eur Radiol, DOI 10.1007/s00330-026-12393-y).

## Size
VerSe'19: 160 CT series / 141 patients; 1,725 vertebrae graded (≈289 fracture-positive). (The broader VerSe segmentation benchmark spans 374 scans / 355 patients across VerSe'19 + VerSe'20.)

## Access / licensing
Fully public, CC BY-SA 4.0. OSF (VerSe'19): https://osf.io/nqjyw/ ; GitHub: https://github.com/anjany/verse ; grading paper: Löffler et al., *Radiology: AI* 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC8082364/

## Caveats
- Released grades are consensus-only; per-rater disagreement is in the separate re-grading study, not in the released data.
- Fracture-positive vertebrae are a minority (≈289/1,725).
- Genant grades ship with **VerSe'19** specifically; whether VerSe'20 includes grading is `[VERIFY]` (grading appears to be a VerSe'19 addition only).

## Relevance to detectability
The only public spine dataset with an explicit ordinal severity/subtlety grade (Genant) on a canonically missed finding, plus a published multi-reader re-grading on the identical images — a ready-made difficulty + disagreement pairing for vertebral fractures.
