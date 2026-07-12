# ATLAS v2.0

- **Tier:** C — adjacent / partial signal (documented small-lesion difficulty gradient; segmentation-only)
- **Modality / anatomy:** T1-weighted MRI / brain — chronic stroke lesion
- **Finding type:** Chronic stroke lesion (segmentation)

## Subtlety / perceptibility label
No explicit subtlety label, but the authors document a **difficulty gradient**: methods "performed the worst on small, followed by medium, lesions," and the paper suggests a future challenge focused on small-lesion detection. Large (1,271 scans), heterogeneous, multi-cohort — high variability. The signal is a documented small-lesion difficulty, not a per-lesion label.

## Label provenance
Trained team using ITK-SNAP under a standardized protocol; **single consensus mask per subject**, each QC-checked by two trained members. No multiple independent per-case masks in this release (an inter-rater subset is explicitly deferred to a future release).

## Size
1,271 T1w MRIs total → 655 public train (with masks) + 300 public test (masks hidden) + 316 hidden generalizability set.

## Access / licensing
Open with a Data Use Agreement. Preprocessed via INDI/NITRC; raw native-space via ICPSR/ADDEP (DOI 10.3886/ICPSR36684.v4). https://atlas.grand-challenge.org/ ; https://www.icpsr.umich.edu/web/ICPSR/studies/36684 ; paper: Liew et al., *Scientific Data* 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC9203460/

## Caveats
- Single-rater consensus design → **no preserved inter-rater disagreement** in the public release (explicitly a future-release goal).
- Chronic lesions are generally less subtle than acute; subtlety signal is limited to the documented small-lesion difficulty, not a per-lesion label.
- Requires DUA.

## Relevance to detectability
The largest public stroke-lesion MRI set, with an author-documented "small lesions are hardest" difficulty gradient — useful as a scale benchmark and a difficulty-stratifiable (by lesion size) corpus, though it carries no explicit perceptibility label.
