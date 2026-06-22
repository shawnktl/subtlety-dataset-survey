# Subtlety / Perceptibility Dataset Index

Tier-ranked index of 26 public radiology datasets surveyed for **explicit subtlety / perceptibility / conspicuity labels** (or usable difficulty proxies). Built from the completed survey (`research-output.md` in `nodule-detectability`'s task-rounding project). See `PROJECT_SUMMARY.md` for scope and purpose, and `notes/follow-ups.md` for the highest-leverage next moves.

## Tiering

- **Tier A — Direct subtlety/perceptibility/conspicuity labels.** A dataset carries an explicit numeric or categorical subtlety/conspicuity field.
- **Tier B — Reader-disagreement / multi-rater designs.** No explicit subtlety field, but multi-reader label noise / disagreement is usable as a difficulty proxy.
- **Tier C — Adjacent / partial signal.** Weaker fit — process-level (eye-tracking) signal, derivable subsets, or no perceptibility axis at all (listed for completeness).

---

## Tier A — Direct subtlety / conspicuity labels

| Dataset | Modality / anatomy | Subtlety label | Size | Access | Page |
|---|---|---|---|---|---|
| LIDC-IDRI | Thoracic CT / lung nodules | Per-nodule subtlety 1–5, up to 4 readers | 1,018 cases, ~2,600+ nodules | Open (TCIA) | [lidc-idri](datasets/lidc-idri.md) |
| JSRT | CXR (digitized film) / lung nodules | 5 subtlety levels, consensus | 247 CXRs | Open (registration) | [jsrt](datasets/jsrt.md) |
| CBIS-DDSM | Screen-film mammography / masses + calc | Per-lesion subtlety 1–5 | ~2,620 cases | Open (TCIA) | [cbis-ddsm](datasets/cbis-ddsm.md) |
| LNDb | Thoracic CT / lung nodules | LIDC-style subtlety, multi-reader | 294 CT scans | Open (Zenodo / GC) | [lndb](datasets/lndb.md) |
| OPTIMAM (OMI-DB) | FFDM/DBT/MRI / breast lesions | Per-lesion conspicuity | 1.3M studies, ~7M images | Restricted (DUA) | [optimam-omi-db](datasets/optimam-omi-db.md) |

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

## Tier C — Adjacent / partial signal

| Dataset | Modality / anatomy | Why adjacent | Size | Access | Page |
|---|---|---|---|---|---|
| REFLACX | CXR / eye-tracking + reports | Behavioral (gaze) proxy; 5 readers | 2,616 CXRs | Open (PhysioNet) | [reflacx](datasets/reflacx.md) |
| EGD-CXR | CXR / eye-tracking + dictation | Single-reader gaze proxy | 1,083 CXRs | Open (PhysioNet) | [egd-cxr](datasets/egd-cxr.md) |
| FG-CXR | CXR / gaze + report captions | Fine-grained gaze/diagnosis alignment | n/a | Per paper (verify) | [fg-cxr](datasets/fg-cxr.md) |
| NLST | LDCT / lung screening | Derivable missed-on-prior subset only | ~54k participants | Open (DUA) | [nlst](datasets/nlst.md) |
| SIIM-ACR Pneumothorax | CXR / pneumothorax | No subtlety label; difficulty inferred | 12,047 images | Open (Kaggle) | [siim-acr-pneumothorax](datasets/siim-acr-pneumothorax.md) |
| BCS-DBT | DBT / breast | No perceptibility annotation | 22,032 volumes | Open (TCIA) | [bcs-dbt](datasets/bcs-dbt.md) |
| EMBED | FFDM + DBT / breast | No surfaced conspicuity field (verify schema) | 3.4M images | AWS Open + DUA | [embed](datasets/embed.md) |
| INbreast | FFDM / breast | Small, no subtlety axis | 410 images | Restricted | [inbreast](datasets/inbreast.md) |
| PadChest | CXR / 174 findings | Binary presence/absence | 160k+ images | Open (registration) | [padchest](datasets/padchest.md) |
| CheXpert | CXR / 14 observations | Labeler uncertainty (upstream of perceptibility) | 224,316 images | Open (Stanford AIMI) | [chexpert](datasets/chexpert.md) |
| NIH ChestX-Ray14 | CXR / 14 findings | No subtlety axis; label-quality critiqued | ~112k images | Open (NIH) | [nih-chestxray14](datasets/nih-chestxray14.md) |
| ISBI/MS multi-rater | Brain MRI / MS lesions | Multi-rater MR variability | n/a | Per paper | [isbi-ms-multirater](datasets/isbi-ms-multirater.md) |

---

## At-a-glance counts

- **Tier A (direct label):** 5 — LIDC-IDRI, JSRT, CBIS-DDSM, LNDb, OPTIMAM/OMI-DB
- **Tier A/B hybrid:** 1 — CheXthought
- **Tier B (difficulty proxy):** 8 — VinDr-CXR, VinDr-Mammo, MURA, BraTS, Messidor-2, OAI, MIDRC/RICORD, PI-CAI
- **Tier C (adjacent):** 12 — REFLACX, EGD-CXR, FG-CXR, NLST, SIIM-ACR Pneumothorax, BCS-DBT, EMBED, INbreast, PadChest, CheXpert, NIH ChestX-Ray14, ISBI/MS multi-rater
- **Total surveyed:** 26
