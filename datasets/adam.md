# ADAM (Aneurysm Detection And segMentation challenge)

- **Tier:** C — adjacent / partial signal (canonically subtle finding + detection-difficulty design)
- **Modality / anatomy:** TOF-MRA (+ co-registered T1/T2/FLAIR) / intracranial vasculature
- **Finding type:** Unruptured intracranial aneurysms (UIA) — detection (Task 1) + segmentation (Task 2)

## Subtlety / perceptibility label
No explicit subtlety field. Small UIAs (<3–5 mm) are canonically hard to detect on TOF-MRA; the challenge is explicitly a detection task scored by sensitivity and false-positive count, and includes 20 aneurysm-negative cases to test false-positive behavior — a detection-difficulty design rather than a labeled perceptibility axis.

## Label provenance
Manual binary masks by expert annotators (radiologists); reference standard from clinical reads + expert delineation. `[VERIFY]` exact rater count / consensus protocol.

## Size
113 training subjects (93 with ≥1 annotated UIA, 20 with no aneurysm); separate hidden test set. Each training subject has 1 TOF-MRA + 1 structural scan.

## Access / licensing
Open via Grand Challenge registration (UMC Utrecht). https://adam.isi.uu.nl/ ; details: https://adam.isi.uu.nl/details/ ; paper: Timmins et al., *NeuroImage* 2021, https://www.sciencedirect.com/science/article/pii/S1053811921004936

## Caveats
- Test labels withheld (eval via submission).
- Modest case count; single primary site.

## Relevance to detectability
A small-aneurysm detection benchmark on MRA — the canonically subtle "did you miss the 3 mm aneurysm" problem, with built-in negative cases to probe false positives. Difficulty is inherent to the task, not labeled per-lesion.
