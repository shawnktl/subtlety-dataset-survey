# CURVAS-PDACVI

- **Tier:** B — reader-disagreement / multi-rater design (5 per-rater annotations preserved) on a canonically subtle finding
- **Modality / anatomy:** Portal-venous contrast-enhanced CT / pancreas — PDAC + peripancreatic vasculature
- **Finding type:** Pancreatic ductal adenocarcinoma (PDAC) segmentation + vascular involvement (portal vein, SMV/SMA, hepatic artery, celiac trunk)

## Subtlety / perceptibility label
Combines **both** survey axes. The finding (PDAC) is canonically subtle — CT sensitivity is only 58–77% for ≤2 cm tumors, and ~44% of missed PDACs are isoattenuating (do not stand out from normal parenchyma). And the labels preserve genuine multi-rater disagreement: **5 annotations per case** (1 from PANORAMA + 4 additional radiologists across three hospitals), each stored as a separate file (`annotation_1..5.nii.gz`).

## Label provenance
5 raters per case; per-rater annotations preserved as separate files (explicit).

## Size
125 CT scans (40 train / 5 val / 85 test).

## Access / licensing
Open. CC BY 4.0. Training set (4.6 GB) downloadable now; val/test withheld until challenge completion. https://zenodo.org/records/15401568 ; https://sycaimedical.com/curvaspdacvi/

## Caveats
- Most of the data (85 test scans) is withheld pending challenge close — only the 40 training scans currently have full per-rater access.
- Newer / smaller dataset.

## Relevance to detectability
Arguably the single best-fit new record in this sweep: it spans subtlety (PDAC, a textbook missed cancer) *and* preserved inter-rater disagreement (5 raters), on an abdominal organ. The detectability framing's "subtle finding + reader divergence" pairing made explicit in body CT.
