# BHSD (Brain Hemorrhage Segmentation Dataset)

- **Tier:** C — adjacent / partial signal (canonically subtle finding; voxel-level multi-class ICH)
- **Modality / anatomy:** 3D non-contrast CT (NCCT) / brain
- **Finding type:** Multi-class ICH segmentation (5 subtypes: EDH, IPH, IVH, SAH, SDH)

## Subtlety / perceptibility label
No explicit subtlety field and no preserved per-rater disagreement. Voxel-level multi-class ICH; small subtype lesions (thin SDH, subtle SAH) are canonically hard to delineate — qualifies on the canonically-subtle-finding axis only.

## Label provenance
Expert pixel-level annotations on the 192-volume subset; slice-level labels on the larger set. `[VERIFY]` exact rater count / consensus protocol (thin in the paper).

## Size
192 volumes with voxel-level annotations + 2,200 volumes with slice-level annotations (~2,192 3D CT scans, 24–40 slices each, 512×512).

## Access / licensing
Open via GitHub: https://github.com/White65534/BHSD . Paper: BHSD, MLMI 2023, https://arxiv.org/abs/2308.11298

## Caveats
- Annotation-protocol / rater details thin `[VERIFY]`.
- Source images drawn partly from existing public ICH data.

## Relevance to detectability
One of the few datasets offering *subtype-resolved voxel-level* ICH masks, letting difficulty be examined per hemorrhage subtype (e.g. subtle SAH vs obvious IPH) — a finer-grained handle on hemorrhage detectability than slice-level sets, though without an explicit perceptibility label.
