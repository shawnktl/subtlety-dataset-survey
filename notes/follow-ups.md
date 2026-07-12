# Follow-ups — highest-leverage next moves

From the survey's recommendations, in priority order. See `index.md` for the full tiered landscape and each dataset's page for caveats.

---

## 0. New highest-leverage assets from the 2026-06-24 wider-net sweep

The sweep (+33 datasets → 59) closed the stroke and abdominal gaps and surfaced three standout cross-anatomy assets that now rank alongside CheXthought for the detectability framing:

- **AISD** (NCCT acute ischemic infarct, `datasets/aisd.md`) — the closest neuro analogue to LIDC's 1–5 scale: an **explicit graded conspicuity label** (clear / blurred / invisible) on a canonically subtle finding, with paired DWI as ground truth. *Concrete move:* test whether the LIDC-trained MAE-band / k-NN detectability framing transfers to the clear/blurred/invisible strata — the cleanest non-chest Tier-A validation available.
- **CURVAS-PDACVI** (CECT pancreas/PDAC, `datasets/curvas-pdacvi.md`) — spans **both** axes: a subtle finding (PDAC, 58–77% CT sensitivity at ≤2 cm) *and* 5 preserved per-rater masks. *Concrete move:* use as the abdominal test of whether per-rater disagreement predicts detectability the way subtlety does in LIDC.
- **MSSEG-2016** (brain MS MRI, `datasets/msseg-2016.md`) — **7 expert raters, all per-rater masks released**; the strongest preserved-disagreement substrate in the survey. *Concrete move:* the best off-the-shelf MR external-validation set for "does inter-rater divergence behave like a subtlety signal on MR?" — partially addresses the MR gap below (on the disagreement axis, not the labeled-subtlety axis). DUA-gated; **WMH Challenge** (`datasets/wmh-challenge.md`) and **QUBIQ** (`datasets/qubiq.md`) are one-click-open per-rater alternatives.

`[VERIFY]` flags on these pages (label-aggregation method, license tags, rater counts) should be confirmed directly before relying on them — see each dataset page.

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

**Update (2026-06-24 sweep):** still no *explicit per-lesion subtlety label* on MR — the gap stands on the labeled-subtlety axis. But the *disagreement* axis on MR is now well-covered with preserved per-rater data: **MSSEG-2016** (7 raters), **WMH Challenge** (extra observers), **QUBIQ** (per-rater by design), **BraTS-METS** / **UCSF-BMSR** (small-met regime). The MR validation route is now via disagreement, not labels.

---

## Other gaps (from the survey) — with 2026-06-24 status

- **Cross-modality "missed-on-prior" labeling:** no packaged dataset surfaces a per-finding "missed on prior study" label. NLST missed-cancer subset is closest but requires reconstruction. *(Still open.)*
- **Pediatric imaging:** GRAZPEDWRI-DX (pediatric wrist fracture) added, with occult-fracture secondary-sign labels — but it carries no explicit subtlety grade. *(Largely still open.)*
- **Abdominal cross-sectional (CT/MR):** ~~DeepLesion is the closest...~~ **CLOSED** — KiTS21, LiTS, PANORAMA, CURVAS, CURVAS-PDACVI added; PDAC (PANORAMA/CURVAS-PDACVI) gives a canonically-subtle finding with quantified miss-rate, and KiTS21/CURVAS give preserved per-rater disagreement. DeepLesion/AMOS/AbdomenCT-1K were evaluated and excluded (no perceptibility signal).
- **Vascular / acute stroke or PE:** **LARGELY CLOSED** — stroke now has 6 ischemic + 4 hemorrhage + 2 aneurysm datasets, incl. **AISD** (explicit conspicuity labels) and **CQ500** (3 reads released). **RSNA-PE** promoted to Tier A on its per-exam QA/mimic flags; FUMPE adds subsegmental-PE masks. Still no per-PE *conspicuity rating*.
- **Dental, ultrasound, nuclear medicine:** ultrasound now has **CAMUS** (echo, image-quality grade + observer-variability fold); dental and nuclear medicine still effectively absent.

---

## Optional / opportunistic

- REFLACX as a "perceptibility-as-behavior" exploratory dataset — gaze dwell on subtle findings is intriguing as a feature.
- Reach out to LNDb authors (CHUSJ / FCT project) about whether per-reader divergence on subtlety ratings is preserved in the data release.
