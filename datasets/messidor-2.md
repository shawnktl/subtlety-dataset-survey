# Messidor / Messidor-2

- **Tier:** B — reader-disagreement / multi-rater design (difficulty proxy)
- **Modality / anatomy:** Color fundus photography / diabetic retinopathy grading
- **Finding type:** DR lesions (microaneurysms, exudates), ordinal 5-class grading

## Subtlety / perceptibility label
No explicit subtlety field; disagreement frequency during adjudication is the difficulty signal.

## Label provenance
Messidor-2 adjudicated by **panel of 3 experts** with re-examination until consensus. Kaggle EyePACS competition data is single-rater (much noisier).

## Size
Messidor 1,200; Messidor-2 1,748; EyePACS ~88k.

## Access / licensing
Open with registration. https://www.adcis.net/en/third-party/messidor/

## Caveats
- Not radiology in the chest/abdominal sense, but a classic "subtle finding" domain.
- Ordinal 5-class grading.

## Relevance to detectability
Multi-rater adjudication preserves disagreement signal indirectly.
