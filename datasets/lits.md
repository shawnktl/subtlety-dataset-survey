# LiTS (Liver Tumor Segmentation Benchmark)

- **Tier:** C — adjacent / partial signal (canonically subtle finding; no perceptibility/disagreement annotation)
- **Modality / anatomy:** Portal-venous CT / liver + liver tumors/metastases
- **Finding type:** Liver lesions (primary + metastatic), heterogeneous size/appearance

## Subtlety / perceptibility label
No explicit subtlety field and no preserved per-rater disagreement. Small/low-contrast liver lesions and metastases are canonically easily missed, and LiTS lesions span a wide difficulty range, so it qualifies — weakly — on the canonically-subtle-finding axis only.

## Label provenance
Manual segmentation by trained radiologists across several international clinical sites; consensus / single ground truth, not multi-rater. `[VERIFY]` rater count.

## Size
130 training + 70 test CT scans (200 total).

## Access / licensing
Open (CodaLab / academic torrents). https://www.sciencedirect.com/science/article/pii/S1361841522003085 . License reported as CC BY-NC-SA / CC BY-NC-ND (inconsistent across sources) `[VERIFY]`.

## Caveats
- Generic lesion-segmentation set with no perceptibility / disagreement annotation.
- Borderline — included as low-priority Tier C purely on the "small liver lesions are subtle" rationale.

## Relevance to detectability
The standard public liver-lesion segmentation benchmark; useful as a difficulty-stratifiable (by lesion size/contrast) liver corpus, but it carries no explicit perceptibility signal — listed for liver coverage and as a difficulty-derivation candidate, not as a labeled-subtlety asset.
