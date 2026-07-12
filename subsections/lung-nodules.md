# Lung-Nodule (Segmented) Subsection — External-Validation Menu

A purpose-built slice of the survey: **every dataset already in this survey that contains
lung nodules with segmentation masks** (voxel/pixel masks or radiologist contours — *not*
bounding-box-only or classification-only labels). This is the candidate set for **external
validation** of the LIDC-trained `nodule-detectability` classifier, where segmentation-derived
detectability needs comparably *segmented* nodules to test generalization.

**Inclusion rule:** a dataset qualifies only if lung-nodule **segmentation masks/contours** are
confirmed available. Datasets with lung nodules but only bounding boxes, center coordinates, or
presence/absence labels are listed under **Excluded** with a stated reason. Every claim here was
checked against the dataset's own page and primary source; anything unconfirmed is flagged
`[VERIFY]` and must be confirmed directly before relying on it.

**Method note:** the source survey scan surfaced five lung-nodule datasets (LIDC-IDRI, LNDb, JSRT,
NLST, ChestX-Det). Segmentation availability was verified per dataset — two qualify, three are
excluded (see reasons). No datasets were fabricated; candidates not currently in the survey are
listed separately as follow-ups.

---

## Qualifying datasets (segmented lung nodules)

| Dataset | Segmentation type | Subtlety / perceptibility label | Modality & count | Access & license | External-validation fit |
|---|---|---|---|---|---|
| [LIDC-IDRI](../datasets/lidc-idri.md) | Per-reader nodule **contours** (boundary outlines on every slice, up to 4 radiologists) → convertible to 3D voxel masks (pylidc / dcmqi; DICOM-SEG re-encoding exists) | **Yes** — per-nodule subtlety **1 ("extremely subtle") – 5 ("obvious")**, up to 4 readers, per-reader signal preserved | Thoracic CT; 1,018 cases, ~2,600+ characterized nodules (contours for nodules ≥3 mm) | Open via TCIA; CC BY 3.0 `[VERIFY exact license tag]` | **Anchor / training source, not a true external set** — this is the data the model learns from. Defines the subtlety-label schema and comparability standard for every other entry; use held-out LIDC for *internal* validation only. |
| [LNDb](../datasets/lndb.md) | Per-nodule **voxel/contour masks** for nodules ≥3 mm (LNDb Sub-Challenge B "Nodule Segmentation"; segmented per LIDC-IDRI criteria) | **Yes** — LIDC-style per-nodule ratings including **subtlety** (+ margin, lobulation, spiculation, texture, calcification, sphericity, internal structure, malignancy) | Thoracic CT; 294 scans (CHUSJ Porto, 2016–2018); v4 (2024) adds report-mined annotations | Open via Zenodo + grand-challenge.org (LNDb Challenge); redistribution/license terms `[VERIFY Zenodo record license]` | **Strongest external-validation fit in the survey** — same modality (CT) and same LIDC-style subtlety scheme, explicitly built as a complementary external set to LIDC. Direct drop-in test for an LIDC-trained detectability pipeline. Caveats: single-center (scanner/population domain shift), smaller (294), uneven multi-reader coverage `[VERIFY per-nodule reader coverage]`, and segmentation interobserver Jaccard ≈0.567 (mask-boundary noise). |

**Count: 2 qualifying datasets.**

### Why these two and nothing else

The segmentation-comparable external-validation menu is genuinely thin. LIDC-IDRI defines the
label schema (and is the training anchor, so it can't validate generalization against itself);
**LNDb is effectively the only survey dataset that is both segmented *and* subtlety-labeled *and*
external to LIDC** — which is exactly why the `notes/follow-ups.md` "JSRT + LNDb pairing" move
ranks it first for the CT arm. JSRT provides the cross-*modality* (CXR) subtlety test but not a
segmentation-comparable one (see Excluded).

---

## Excluded lung-nodule datasets (with reason)

| Dataset | Lung nodules? | Segmentation masks? | Reason for exclusion |
|---|---|---|---|
| [JSRT](../datasets/jsrt.md) | Yes (CXR) | **No** — nodule **center (X,Y) coordinates + size only** | The publicly distributed nodule annotation is location + size, not a per-nodule mask. The associated SCR (Segmentation in Chest Radiographs) masks segment **lung fields / heart / clavicles, not nodules.** Retains a valuable 5-level (consensus) CXR subtlety label, so it stays the cross-modality *subtlety* test — just not a *segmentation* one. |
| [NLST](../datasets/nlst.md) | Yes (LDCT screening) | **No** — screening outcomes only; no native nodule masks or perceptibility labels | No packaged segmentation. A "missed-on-prior" subset is *derivable* but must be reconstructed by case linkage. NLST-*derived* pixel-level segmentation sets exist externally (e.g., NLSTseg `[VERIFY]`) but are separate datasets **not in this survey**. |
| [ChestX-Det](../datasets/chestx-det.md) | Yes ("Nodule" among 10 CXR classes) | **Bbox-only in the confirmed public release** | The confirmed downloadable release (ChestX-Det10, GitHub) provides **bounding boxes** for the Nodule class (annotation format `[x1,y1,x2,y2]`), not masks. An extended release with polygon/segmentation annotations is referenced in the literature, but downloadable Nodule-category **masks are not confirmed** `[VERIFY extended-release segmentation availability]`. Also CXR (2D), not CT. Excluded per the "no bbox-only" rule. |

**Count: 3 excluded (JSRT, NLST, ChestX-Det).**

---

## Candidate segmentation sources *not yet in this survey*

Flagged as follow-ups, **not** entries — none are currently surveyed, so details below are
unverified pointers, not survey claims. Add + verify each before use.

- **LUNA16** — LIDC-derived detection subset (888 CTs with slice thickness ≤2.5 mm; nodule
  **centroids + diameters** for nodules accepted by ≥3/4 readers). Provides *detection*
  annotations, not native masks — any segmentation is **inherited from LIDC**, so it adds no new
  mask source beyond LIDC. `[VERIFY]`
- **DLCSD** (Duke Lung Cancer Screening Dataset) — NLST/Duke-derived screening CT; lung-nodule
  segmentation availability and license `[VERIFY]`. Not in this survey.
- **NLSTseg** — pixel-level lung-cancer segmentation derived from NLST LDCT images; availability,
  count, and license `[VERIFY]`. Not in this survey.

If any of these is confirmed to carry downloadable lung-nodule masks, add a `datasets/<id>.md`
page to the survey first, then promote it into the Qualifying table above.

---

## Open `[VERIFY]` flags on this page

- LIDC-IDRI exact license tag (CC BY 3.0 assumed from TCIA).
- LNDb Zenodo record license / redistribution terms; per-nodule multi-reader coverage.
- ChestX-Det extended-release segmentation availability for the Nodule category.
- LUNA16 / DLCSD / NLSTseg — all details unverified (out-of-survey candidates).

*See `../notes/follow-ups.md` §2 (JSRT + LNDb external-validation pairing) for the companion
next-move on the CT/CXR subtlety-transfer test.*
