# RibFrac

- **Tier:** C — adjacent / partial signal (canonically missed finding + subtype labels; ambiguous masks)
- **Modality / anatomy:** Chest-abdomen CT / ribs
- **Finding type:** Traumatic rib fractures — buckle, nondisplaced, displaced, segmental (instance segmentation + classification)

## Subtlety / perceptibility label
No explicit subtlety field, but rib fractures (especially nondisplaced/buckle) are among the most commonly missed CT/CXR findings; the dataset separates these subtle subtypes, and the authors note the masks are "noisy" because fracture boundaries are genuinely ambiguous — perceptibility is hard even for the annotators.

## Label provenance
Voxel-level masks by radiologists via a human-in-the-loop pipeline; annotator count not disclosed `[VERIFY]`.

## Size
660 CT scans (~5,000 fractures): 420 train (all positive), 80 val (20 fracture-free), 160 test.

## Access / licensing
Public, **CC BY-NC 4.0**. Zenodo: train https://zenodo.org/records/3893508, val https://zenodo.org/records/3893496, test https://zenodo.org/records/3993379. Grand Challenge registration for leaderboard only; Zenodo data openly downloadable. Paper: https://arxiv.org/abs/2402.09372

## Caveats
- Non-commercial license; single-center.
- Test ships images only (no public masks).
- Annotator count undisclosed `[VERIFY]`; noisy/ambiguous masks acknowledged.

## Relevance to detectability
A subtype-labeled rib-fracture set where the annotators themselves flag boundary ambiguity — a candidate for studying perceptibility on a canonically missed finding, with the subtype split (buckle/nondisplaced vs displaced) doubling as a coarse difficulty proxy.
