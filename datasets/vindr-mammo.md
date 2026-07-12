# VinDr-Mammo

- **Tier:** B — reader-disagreement / multi-rater design (difficulty proxy)
- **Modality / anatomy:** FFDM / masses, calcifications, asymmetries, distortions
- **Finding type:** Breast lesions

## Subtlety / perceptibility label
No per-finding subtlety field; multi-reader arbitration as a difficulty proxy. BI-RADS assessment + density + lesion-level bounding boxes.

## Label provenance
5,000 four-view exams, **double-read with arbitration by a third reader.**

## Size
5,000 exams (20k images).

## Access / licensing
Open via PhysioNet (credentialed). https://physionet.org/content/vindr-mammo/1.0.0/

## Caveats
- **Verify before relying on:** arbitration means only the resolved label is published — original per-reader divergence may or may not be preserved. Documentation describes "double read with arbitration" but it's unclear whether the two pre-arbitration labels are released or only the consensus. Verify on the PhysioNet schema before relying on it as a multi-rater dataset.

## Relevance to detectability
Multi-reader with arbitration; not a per-finding subtlety field but a usable difficulty proxy.
