# REFLACX

- **Tier:** B/C — process-level (eye-tracking) signal
- **Modality / anatomy:** CXR / MIMIC-CXR subset with synchronized eye-tracking + dictated reports
- **Finding type:** Thoracic abnormalities (with gaze + report)

## Subtlety / perceptibility label
Not a subtlety dataset per se — but gaze dwell time and report uncertainty language are arguably the *behavioral* fingerprint of perceptibility difficulty. Eye-gaze fixations + timestamped report transcription + abnormality ellipses + image-level labels.

## Label provenance
3,032 reading sessions across 2,616 CXRs, **5 radiologists**. Subset includes all 5 readers on the same images (allows direct inter-rater comparison).

## Size
2,616 unique CXRs.

## Access / licensing
Open via PhysioNet (credentialed). https://physionet.org/content/reflacx-xray-localization/1.0.0/

## Caveats
- Not a subtlety dataset per se.

## Relevance to detectability
Process-level signal; pairs well with CheXthought. Gaze dwell on subtle findings is intriguing as a feature.
