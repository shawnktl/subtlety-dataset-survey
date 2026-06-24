# PhysioNet CT-ICH (Hssayeni et al.)

- **Tier:** C — adjacent / partial signal (canonically subtle finding; two-reader consensus, disagreement not preserved)
- **Modality / anatomy:** Non-contrast head CT (NCCT) / brain (TBI cohort)
- **Finding type:** ICH detection + segmentation (5 subtypes: IVH, IPH, SAH, EDH, SDH) + skull fracture

## Subtlety / perceptibility label
No explicit subtlety field. Small/thin hemorrhages are canonically subtle, and the dataset provides voxel-level masks (rare for ICH); but annotation was done by two-radiologist consensus with disagreement resolved (not preserved per-rater).

## Label provenance
Each slice annotated by **2 radiologists, reconciled to consensus** (per-rater not separately released).

## Size
82 CT scans total; 36 with diagnosed ICH (~30 slices each).

## Access / licensing
Open access, **CC BY 4.0**, freely downloadable. https://physionet.org/content/ct-ich/ (current version 1.3.1).

## Caveats
- Small (82 scans).
- Consensus only — no preserved inter-rater disagreement.
- TBI-skewed cohort.

## Relevance to detectability
A small but clean, openly-licensed ICH segmentation set with voxel-level masks on a canonically subtle finding — useful as a portable hemorrhage substrate, though it carries neither an explicit subtlety label nor preserved disagreement (for that, see CQ500).
