# FracAtlas

- **Tier:** C — adjacent / partial signal (canonically missable fractures; adjudicated consensus)
- **Modality / anatomy:** Plain X-ray / MSK — hand, leg, hip, shoulder
- **Finding type:** Bone fracture (classification, bounding box, segmentation mask)

## Subtlety / perceptibility label
No explicit subtlety field. Includes non-displaced/hairline fractures that are missable on plain film, and the annotation pipeline routed radiologist disagreements to an orthopedic surgeon — indicating real reader uncertainty on a subset (though that disagreement is adjudicated away, not preserved per-rater).

## Label provenance
2 radiologists labeled independently; disagreements adjudicated by an orthopedic surgeon (consensus-style). makesense.ai.

## Size
4,083 images; 717 fractured; 922 fracture instances (hand 1,538 imgs/437 fx, leg 2,272/263, hip 338/63, shoulder 349/63).

## Access / licensing
Public, CC BY 4.0, no registration. Figshare DOI 10.6084/m9.figshare.22363012 (~323 MB). COCO/YOLO/Pascal VOC. Paper: https://www.nature.com/articles/s41597-023-02432-4

## Caveats
- Multi-hospital (Bangladesh); minority fracture-positive (717/4,083).
- Per-rater disagreement not preserved (adjudicated consensus); no subtlety grade.

## Relevance to detectability
A general MSK-fracture set spanning multiple body regions, with an annotation workflow that explicitly surfaced reader disagreement (escalated to a surgeon) — the disagreement isn't released, but the adjudication trail marks where fractures were perceptually hard. Complements GRAZPEDWRI-DX (pediatric wrist) and RibFrac (ribs) for fracture coverage.
