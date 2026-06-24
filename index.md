# Subtlety / Perceptibility Dataset Index

Tier-ranked index of 59 public radiology datasets surveyed for **subtlety / perceptibility / conspicuity signal** — read broadly: explicit subtlety/conspicuity labels, multi-reader disagreement designs, miss-rate / perceptual-error studies, eye-tracking/gaze datasets, difficulty-stratified subsets, and datasets whose *finding is canonically subtle/hard-to-detect* (early ischemic change, small ICH, subtle fractures, small PE, small mets, PDAC). Originally a chest/breast-dominated set of 26 (built from the survey in `nodule-detectability`'s task-rounding project); a 2026-06-24 discovery sweep widened the net to cover neuro (esp. stroke), abdomen/body, and other under-represented regions. See `PROJECT_SUMMARY.md` for scope, `notes/follow-ups.md` for next moves, and `notes/search-strategy.md` for the discovery method/log.

## Tiering

- **Tier A — Direct subtlety/perceptibility/conspicuity (or per-exam difficulty/quality) labels.** A dataset carries an explicit numeric or categorical subtlety/conspicuity/difficulty field.
- **Tier B — Reader-disagreement / multi-rater designs.** No explicit subtlety field, but multi-reader label noise / disagreement is usable as a difficulty proxy (strongest when per-rater annotations are preserved).
- **Tier C — Adjacent / partial signal.** Weaker fit — process-level (eye-tracking) signal, derivable subsets, canonically-subtle findings without an explicit label, or detection challenges (listed for coverage).

---

## Tier A — Direct subtlety / conspicuity / difficulty labels

| Dataset | Modality / anatomy | Subtlety label | Size | Access | Page |
|---|---|---|---|---|---|
| LIDC-IDRI | Thoracic CT / lung nodules | Per-nodule subtlety 1–5, up to 4 readers | 1,018 cases, ~2,600+ nodules | Open (TCIA) | [lidc-idri](datasets/lidc-idri.md) |
| JSRT | CXR (digitized film) / lung nodules | 5 subtlety levels, consensus | 247 CXRs | Open (registration) | [jsrt](datasets/jsrt.md) |
| CBIS-DDSM | Screen-film mammography / masses + calc | Per-lesion subtlety 1–5 | ~2,620 cases | Open (TCIA) | [cbis-ddsm](datasets/cbis-ddsm.md) |
| LNDb | Thoracic CT / lung nodules | LIDC-style subtlety, multi-reader | 294 CT scans | Open (Zenodo / GC) | [lndb](datasets/lndb.md) |
| OPTIMAM (OMI-DB) | FFDM/DBT/MRI / breast lesions | Per-lesion conspicuity | 1.3M studies, ~7M images | Restricted (DUA) | [optimam-omi-db](datasets/optimam-omi-db.md) |
| AISD | NCCT / acute ischemic infarct | Per-lesion conspicuity: clear / blurred / invisible | 397 NCCT (paired DWI) | Open (GitHub) | [aisd](datasets/aisd.md) |
| CPAISD | NCCT / hyperacute ischemic core+penumbra | Perceptibility-defined ("non-revealing on NCCT") | 112 patients | Open (Zenodo) | [cpaisd](datasets/cpaisd.md) |
| RSNA-PE (RSPECT) | CTPA / pulmonary embolism | Per-exam QA / difficulty / PE-mimic flags | 9,446 exams | Open (Kaggle/AWS) | [rsna-pe](datasets/rsna-pe.md) |

## Tier A/B hybrid — direct difficulty operationalization

| Dataset | Modality / anatomy | Signal | Size | Access | Page |
|---|---|---|---|---|---|
| CheXthought | CXR / general thoracic | Chain-of-thought + visual attention + multi-reader disagreement | 50,312 CXRs, 103k traces | Stanford AIMI (non-commercial free; $70k/yr commercial) | [chexthought](datasets/chexthought.md) |

## Tier B — Reader-disagreement / multi-rater designs (difficulty proxy)

| Dataset | Modality / anatomy | Multi-rater signal | Size | Access | Page |
|---|---|---|---|---|---|
| VinDr-CXR | CXR / 22 findings | 3 readers/case (train), 5-reader consensus (test) | 18k annotated | Open (PhysioNet) | [vindr-cxr](datasets/vindr-cxr.md) |
| VinDr-Mammo | FFDM / breast lesions | Double-read + arbitration | 5,000 exams | Open (PhysioNet) | [vindr-mammo](datasets/vindr-mammo.md) |
| MURA | MSK X-ray / 7 regions | 6-reader test-set label vector | 14,863 studies | Open (Stanford AIMI) | [mura](datasets/mura.md) |
| BraTS | Brain MRI / glioma | 1–4 raters, inter-rater DSC 0.74–0.85 | Thousands | Open (Synapse) | [brats](datasets/brats.md) |
| Messidor-2 | Fundus / DR grading | 3-expert adjudication panel | 1,748 (Messidor-2) | Open (registration) | [messidor-2](datasets/messidor-2.md) |
| OAI | Knee X-ray + 3T MRI / OA | 2 readers + arbitration | 4,796 participants | Open (DUA) | [oai](datasets/oai.md) |
| MIDRC / RICORD | CXR (+CT) / COVID severity | 3 physicians/image | Tens of thousands | Open (DUA) | [midrc-ricord](datasets/midrc-ricord.md) |
| PI-CAI | Prostate mpMRI / csPCa | Indirect (PI-RADS vs histology) | 10,000+ exams | Open (DUA) | [pi-cai](datasets/pi-cai.md) |
| CQ500 | Head NCCT / ICH, fracture, shift | 3 radiologists/scan, per-rater reads released | 491 scans | Open (CC BY-NC-SA) | [cq500](datasets/cq500.md) |
| ISLES 2022 | Brain MRI (DWI/ADC/FLAIR) / ischemic stroke | Punctiform-infarct inclusion + inter-rater study; multi-vendor | 250 public | Open (Zenodo CC-BY) | [isles-2022](datasets/isles-2022.md) |
| ISLES 2015 (SISS) | Multi-spectral MRI / sub-acute infarct | Two independent expert ground-truth sets | 64 cases | Open (challenge/Zenodo) | [isles-2015-siss](datasets/isles-2015-siss.md) |
| KiTS21 | CECT / kidney tumor + cyst | 3 independent per-ROI annotations preserved | 300 public | Open (CC BY-NC-SA) | [kits21](datasets/kits21.md) |
| CURVAS | Abdominal CT / pancreas, kidney, liver | 3 expert per-rater masks preserved (calibration/uncertainty) | 90 scans | Open (Zenodo/GC) | [curvas](datasets/curvas.md) |
| CURVAS-PDACVI | CECT / PDAC + vasculature | 5 per-rater masks preserved on a subtle finding | 125 scans (40 train public) | Open (CC BY) | [curvas-pdacvi](datasets/curvas-pdacvi.md) |
| MSSEG-2016 | Brain MRI / MS lesions | 7 expert raters, all per-rater masks released | 53 patients | Open (Shanoir DUA) | [msseg-2016](datasets/msseg-2016.md) |
| WMH Challenge | Brain MRI (FLAIR/T1) / WMH | 2 additional observers' per-rater masks (train) | 170 subjects | Open (CC BY-NC) | [wmh-challenge](datasets/wmh-challenge.md) |
| QUBIQ | MRI/CT multi-organ (brain subtasks) | Per-rater masks by design (3–7 raters/task) | Small per task | Open (GC registration) | [qubiq](datasets/qubiq.md) |
| VerSe (Genant) | Spine CT / vertebral fractures | Genant grade 0–3 + multi-reader re-grading | 160 series / 1,725 vertebrae | Open (CC BY-SA) | [verse](datasets/verse.md) |
| ChestX-Det | CXR / 10 thoracic findings | Blinded double-read + adjudication, instance-level | 3,543 images | Open (GitHub) | [chestx-det](datasets/chestx-det.md) |
| CAMUS | Echocardiography / cardiac chambers | Image-quality grade + inter-/intra-observer fold | 500 patients | Open (registration) | [camus](datasets/camus.md) |

## Tier C — Adjacent / partial signal

| Dataset | Modality / anatomy | Why adjacent | Size | Access | Page |
|---|---|---|---|---|---|
| REFLACX | CXR / eye-tracking + reports | Behavioral (gaze) proxy; 5 readers | 2,616 CXRs | Open (PhysioNet) | [reflacx](datasets/reflacx.md) |
| EGD-CXR | CXR / eye-tracking + dictation | Single-reader gaze proxy | 1,083 CXRs | Open (PhysioNet) | [egd-cxr](datasets/egd-cxr.md) |
| FG-CXR | CXR / gaze + report captions | Fine-grained gaze/diagnosis alignment | n/a | Per paper (verify) | [fg-cxr](datasets/fg-cxr.md) |
| CT-ScanGaze | Body CT (3D) / radiologist gaze | First volumetric gaze/scanpath proxy | 909 CT volumes | Open (HF, CC BY-NC-SA) | [ct-scangaze](datasets/ct-scangaze.md) |
| NLST | LDCT / lung screening | Derivable missed-on-prior subset only | ~54k participants | Open (DUA) | [nlst](datasets/nlst.md) |
| SIIM-ACR Pneumothorax | CXR / pneumothorax | No subtlety label; difficulty inferred | 12,047 images | Open (Kaggle) | [siim-acr-pneumothorax](datasets/siim-acr-pneumothorax.md) |
| BCS-DBT | DBT / breast | No perceptibility annotation | 22,032 volumes | Open (TCIA) | [bcs-dbt](datasets/bcs-dbt.md) |
| EMBED | FFDM + DBT / breast | No surfaced conspicuity field (verify schema) | 3.4M images | AWS Open + DUA | [embed](datasets/embed.md) |
| INbreast | FFDM / breast | Small, no subtlety axis | 410 images | Restricted | [inbreast](datasets/inbreast.md) |
| PadChest | CXR / 174 findings | Binary presence/absence | 160k+ images | Open (registration) | [padchest](datasets/padchest.md) |
| CheXpert | CXR / 14 observations | Labeler uncertainty (upstream of perceptibility) | 224,316 images | Open (Stanford AIMI) | [chexpert](datasets/chexpert.md) |
| NIH ChestX-Ray14 | CXR / 14 findings | No subtlety axis; label-quality critiqued | ~112k images | Open (NIH) | [nih-chestxray14](datasets/nih-chestxray14.md) |
| ISBI/MS multi-rater | Brain MRI / MS lesions | Multi-rater MR variability | n/a | Per paper | [isbi-ms-multirater](datasets/isbi-ms-multirater.md) |
| ATLAS v2.0 | Brain MRI / chronic stroke | Documented small-lesion difficulty; consensus masks | 1,271 scans | Open (DUA) | [atlas-v2](datasets/atlas-v2.md) |
| ISLES 2018 | CT perfusion / acute infarct core | CTP-vs-DWI modality-mismatch difficulty | 103 cases | Open (Zenodo) | [isles-2018](datasets/isles-2018.md) |
| RSNA ICH | Head NCCT / hemorrhage | Canonically subtle finding; reconciled single label | 25,272 exams | Open (Kaggle/AWS) | [rsna-ich](datasets/rsna-ich.md) |
| PhysioNet CT-ICH | Head NCCT / hemorrhage | Voxel masks; 2-reader consensus (not preserved) | 82 scans | Open (CC BY) | [physionet-ct-ich](datasets/physionet-ct-ich.md) |
| BHSD | Head NCCT / hemorrhage subtypes | Subtype voxel masks; canonically subtle | ~2,192 scans | Open (GitHub) | [bhsd](datasets/bhsd.md) |
| ADAM | TOF-MRA / unruptured aneurysm | Small-aneurysm detection challenge | 113 train | Open (GC registration) | [adam](datasets/adam.md) |
| CADA | 3D-DSA / cerebral aneurysm | Tiny-target detection imbalance | 109 train / 127 aneurysms | Open (GC registration) | [cada](datasets/cada.md) |
| BraTS-METS | Brain MRI / metastases | Small-met segmentation; consensus | 402 public / 3,076 lesions | Open (Synapse) | [brats-mets](datasets/brats-mets.md) |
| UCSF-BMSR | Brain MRI / metastases | Large small-met corpus; subtraction imgs | 560 MRIs / 5,136 mets | Open (AWS) | [ucsf-bmsr](datasets/ucsf-bmsr.md) |
| MS3SEG | Brain MRI / MS lesions | Tri-mask subtle-vs-benign WMH discrimination | 100 patients | Open (CC BY) | [ms3seg](datasets/ms3seg.md) |
| PANORAMA | CECT / pancreatic PDAC | Canonically missed cancer (miss-rate); reader study | 1,500+ (public train) | Open (Zenodo/TCIA) | [panorama](datasets/panorama.md) |
| LiTS | CT / liver tumor | Small/low-contrast lesions; no perceptibility label | 200 scans | Open (CodaLab) | [lits](datasets/lits.md) |
| FUMPE | CTPA / pulmonary embolism | 67% subsegmental clots; no explicit label | 35 patients / 3,438 ROIs | Open (CC BY) | [fumpe](datasets/fumpe.md) |
| RSNA Cervical Spine | Cervical CT / fracture | Canonically missed trauma finding | 3,112 studies | Open (Kaggle/AWS) | [rsna-cervical-spine](datasets/rsna-cervical-spine.md) |
| RibFrac | Chest CT / rib fractures | Subtype labels; annotators flag mask ambiguity | 660 scans / ~5,000 fx | Open (CC BY-NC) | [ribfrac](datasets/ribfrac.md) |
| GRAZPEDWRI-DX | Pediatric wrist X-ray / fracture | Occult-fracture secondary-sign labels | 20,327 images | Open (CC BY) | [grazpedwri-dx](datasets/grazpedwri-dx.md) |
| FracAtlas | MSK X-ray / fracture | Adjudicated reader-disagreement trail | 4,083 images | Open (CC BY) | [fracatlas](datasets/fracatlas.md) |

---

## At-a-glance counts

- **Tier A (direct label):** 8 — LIDC-IDRI, JSRT, CBIS-DDSM, LNDb, OPTIMAM/OMI-DB, AISD, CPAISD, RSNA-PE
- **Tier A/B hybrid:** 1 — CheXthought
- **Tier B (difficulty proxy):** 20 — VinDr-CXR, VinDr-Mammo, MURA, BraTS, Messidor-2, OAI, MIDRC/RICORD, PI-CAI, CQ500, ISLES 2022, ISLES 2015 (SISS), KiTS21, CURVAS, CURVAS-PDACVI, MSSEG-2016, WMH Challenge, QUBIQ, VerSe (Genant), ChestX-Det, CAMUS
- **Tier C (adjacent):** 30 — REFLACX, EGD-CXR, FG-CXR, CT-ScanGaze, NLST, SIIM-ACR Pneumothorax, BCS-DBT, EMBED, INbreast, PadChest, CheXpert, NIH ChestX-Ray14, ISBI/MS multi-rater, ATLAS v2.0, ISLES 2018, RSNA ICH, PhysioNet CT-ICH, BHSD, ADAM, CADA, BraTS-METS, UCSF-BMSR, MS3SEG, PANORAMA, LiTS, FUMPE, RSNA Cervical Spine, RibFrac, GRAZPEDWRI-DX, FracAtlas
- **Total surveyed:** 59

## Coverage by region (after the 2026-06-24 sweep)

- **Neuro — stroke (ischemic):** AISD, CPAISD, ISLES 2022, ISLES 2015 (SISS), ISLES 2018, ATLAS v2.0 — **6 ischemic-stroke datasets** (was 0).
- **Neuro — hemorrhage / aneurysm:** CQ500, RSNA ICH, PhysioNet CT-ICH, BHSD (hemorrhage); ADAM, CADA (aneurysm) — 6.
- **Neuro — other:** BraTS, MSSEG-2016, WMH Challenge, QUBIQ, BraTS-METS, UCSF-BMSR, MS3SEG, ISBI/MS.
- **Abdomen / body:** KiTS21 (kidney), LiTS (liver), PANORAMA + CURVAS-PDACVI (pancreas/PDAC), CURVAS (multi-organ) — **5 abdominal datasets** (was 0).
- **MSK / spine:** MURA, OAI, VerSe (Genant), RibFrac, GRAZPEDWRI-DX, FracAtlas, RSNA Cervical Spine.
- **Thorax (PE / cardiac):** RSNA-PE, FUMPE (PE); CAMUS (cardiac); + the existing chest/breast CXR & mammography set.
