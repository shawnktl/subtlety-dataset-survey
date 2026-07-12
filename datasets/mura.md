# MURA

- **Tier:** B — reader-disagreement / multi-rater design (test-set only)
- **Modality / anatomy:** Plain-film MSK X-rays / 7 anatomic regions (elbow, finger, forearm, hand, humerus, shoulder, wrist)
- **Finding type:** Normal vs abnormal MSK

## Subtlety / perceptibility label
No severity/subtlety axis. Binary normal vs abnormal; the 6-rater test-set label vector supports disagreement analysis.

## Label provenance
14,863 studies, normal vs abnormal labels. Test set (207 studies) labeled by **6 board-certified Stanford radiologists** with majority-of-3 gold standard, leaving the full 6-rater label vector available for disagreement analysis.

## Size
14,863 studies / ~40k images.

## Access / licensing
Open via Stanford AIMI / MURA competition page. https://stanfordmlgroup.github.io/competitions/mura/

## Caveats
- Multi-reader signal is only on the 207-study test set, not training.
- Binary (normal/abnormal), no severity/subtlety axis.

## Relevance to detectability
Test-set only — useful for benchmarking difficulty in the MSK domain where subtlety data is otherwise scarce.
