# AISD (Acute Ischemic Stroke Dataset)

- **Tier:** A — direct subtlety/perceptibility/conspicuity label
- **Modality / anatomy:** Non-contrast CT (NCCT) / brain — acute ischemic infarct
- **Finding type:** Acute ischemic infarct (segmentation on NCCT)

## Subtlety / perceptibility label
Carries **explicit per-lesion conspicuity labels** baked into the mask categories: remote infarct (1), **clear acute infarct (2)**, **blurred acute infarct (3)**, and **invisible acute infarct (4)** — an explicit detectability stratification, with paired DWI-MRI (≤24 h) as the reference standard. Early ischemic change on NCCT is canonically the hardest finding in stroke imaging, and this is one of the very few public datasets that operationalizes that with a graded "how perceptible is it on the image you're given" label.

## Label provenance
Manually contoured on NCCT by a physician using the same-window DWI-MRI as reference; senior physician double-review for QA. Single annotator + senior QA (not independent multi-rater).

## Size
397 NCCT scans (345 train/val / 52 test), each paired with DWI within 24 h.

## Access / licensing
Free for academic / non-commercial use. GitHub repo with Google Drive + Baidu downloads: https://github.com/GriffinLiang/AISD (mirror: https://github.com/radreports/AISD-ischemic-stroke-). Paper: Liang et al., "Symmetry-Enhanced Attention Network for Acute Ischemic Infarct Segmentation with Non-Contrast CT," MICCAI 2021.

## Caveats
- The clear/blurred/invisible conspicuity labels are the explicit perceptibility signal — but they are single-annotator judgments (DWI-anchored), not multi-reader consensus; inter-rater disagreement is not provided.
- Download partly via Baidu (access friction outside China).

## Relevance to detectability
The closest analogue to LIDC's 1–5 subtlety scale outside the chest: an explicit graded conspicuity label (clear → blurred → invisible) on a canonically subtle finding (early ischemic change), with a DWI ground truth fixing what is *actually* there. The single best stroke fit for the detectability framing.
