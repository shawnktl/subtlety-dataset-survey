# Follow-ups — highest-leverage next moves

From the survey's recommendations, in priority order. See `index.md` for the full tiered landscape and each dataset's page for caveats.

---

## 1. CheXthought (Stanford AIMI) — pursue first

By far the most directly aligned new asset for the broader detectability framing. Chain-of-thought reasoning + visual attention + multi-reader disagreement at 50k-CXR / 501-radiologist scale operationalizes "perceptibility" as a *behavior*, not just a label.

Concrete moves:
- Verify dataset availability and license terms directly on the Stanford AIMI portal (https://stanfordaimi.azurewebsites.net/).
- If non-commercial download is open: pull a sample, inspect the per-image inter-reader disagreement distribution, and assess whether the LIDC-trained detectability framing (MAE-band / k-NN) maps onto a comparable CXR-difficulty model.
- If commercial use is in scope (patent-lawyer thread): note the $70k/yr/dataset licensing cost in any product framing.

**Verify before relying on:** referenced details come from the arXiv preprint (arXiv:2604.26288) and a third-party blog. Confirm directly on the Stanford AIMI portal that the dataset is downloadable and that the chain-of-thought + visual attention components are included in the public release (not held back for commercial license).

---

## 2. JSRT + LNDb pairing — natural external-validation route

JSRT (CXR, 5-level subtlety, ~250 cases) and LNDb (CT, LIDC-style subtlety, 294 cases) together provide the cleanest cross-modality external-validation pair for a subtlety classifier trained on LIDC. Both have direct subtlety labels — no proxy required.

Concrete move: Run the existing LIDC-trained pipeline on LNDb first (closest match — same modality, same labeling scheme); then port to JSRT as a modality-transfer test.

**Verify before relying on (LNDb):** "each scan read by ≥1 radiologist" implies uneven multi-reader coverage. Verify before using LNDb as a multi-rater dataset.

---

## 3. CBIS-DDSM → OPTIMAM — second modality (mammography) with subtlety labels in hand

CBIS-DDSM has the actual 1–5 subtlety field; VinDr-Mammo doesn't (but has multi-reader arbitration as proxy). To test whether the detectability framing generalizes to mammography:
- Start with CBIS-DDSM (direct subtlety, easier mapping) for a feasibility check.
- If results look promising, OPTIMAM is the natural next step for scale — but the DUA / licensing friction is meaningful and should be entered into deliberately.

**Verify before relying on (OPTIMAM):** whether conspicuity annotations cover the DBT subset (~4,500 women) uniformly is not stated in public materials.

---

## Major gap — MR with explicit subtlety/conspicuity labels

**None located.** A purpose-built subtlety-rated MR dataset (any anatomy) does not appear to exist publicly. Best available signal is multi-rater segmentation variability:
- **BraTS** (brain glioma) — inter-rater DSC 0.74–0.85.
- **OAI** knee MRI — KL/MOAKS grading disagreement; BML grade-1 lesions hard to distinguish from partial-volume artifact.
- **ISBI/MS multi-rater** MS lesion segmentation — documented intra/inter-rater variability.

This gap is the clearest "the detectability framing may be nodule/CT-specific" risk for the broader product framing — there is no off-the-shelf MR subtlety ground truth to validate against.

---

## Other gaps (from the survey)

- **Cross-modality "missed-on-prior" labeling:** no packaged dataset surfaces a per-finding "missed on prior study" label. NLST missed-cancer subset is closest but requires reconstruction.
- **Pediatric imaging:** no subtlety-labeled pediatric dataset surfaced.
- **Abdominal cross-sectional (CT/MR):** DeepLesion is the closest adult CT dataset but has no per-lesion subtlety.
- **Vascular / acute stroke or PE:** RSNA PE has QA flags but no per-PE conspicuity rating; stroke datasets have segmentation difficulty but no perceptibility label.
- **Dental, ultrasound, nuclear medicine:** effectively no subtlety-labeled public data found.

---

## Optional / opportunistic

- REFLACX as a "perceptibility-as-behavior" exploratory dataset — gaze dwell on subtle findings is intriguing as a feature.
- Reach out to LNDb authors (CHUSJ / FCT project) about whether per-reader divergence on subtlety ratings is preserved in the data release.
