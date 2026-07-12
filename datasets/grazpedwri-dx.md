# GRAZPEDWRI-DX

- **Tier:** C — adjacent / partial signal (canonically occult fractures + secondary-sign labels)
- **Modality / anatomy:** Plain X-ray / pediatric wrist & distal forearm
- **Finding type:** 9 classes — fracture, periosteal reaction, bone anomaly, bone lesion, metal, foreign body, pronator sign, soft tissue, axis

## Subtlety / perceptibility label
No explicit subtlety field, but pediatric wrist fractures include canonically missed entities (buckle/torus, subtle distal radius), and the dataset explicitly labels **secondary/indirect signs** — pronator quadratus sign, periosteal reaction — as their own classes. Those are precisely the cues radiologists rely on when the fracture line itself is occult, making this an unusually perceptibility-aware annotation scheme.

## Label provenance
Annotated by radiologists, visiting colleagues, and medical students; all annotations validated by 3 board-certified pediatric radiologists (Supervisely). Validation/consensus-reviewed, not per-rater independent.

## Size
20,327 images; 10,643 studies; 6,091 patients; 67,771 annotated objects.

## Access / licensing
Public, CC BY 4.0. Figshare DOI 10.6084/m9.figshare.14825193 (~15.2 GB). YOLO + Pascal VOC. Paper: https://www.nature.com/articles/s41597-022-01328-z

## Caveats
- Single-center (Graz, 2008–2018).
- Mixed annotators (incl. students) with expert validation — not a multi-reader-disagreement design.
- No per-image subtlety grade; pediatric-only.

## Relevance to detectability
One of the few detection datasets that annotates the *secondary signs* of an occult finding as distinct classes — a direct, large-scale handle on the "the fracture is invisible but the soft-tissue/periosteal cue isn't" perceptibility problem in pediatric MSK.
