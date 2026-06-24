# CAMUS

- **Tier:** B — reader-disagreement / multi-rater design (inter-/intra-observer fold) + explicit image-quality grade
- **Modality / anatomy:** 2D echocardiography / cardiac — LV endo/epicardium, myocardium, left atrium (apical 2- & 4-chamber)
- **Finding type:** Chamber / myocardium segmentation + derived LV volumes / ejection fraction

## Subtlety / perceptibility label
Two genuine signals: (1) an explicit **image-quality grade** (good / medium / poor; ~19% poor), with folds stratified by quality and EF — a direct difficulty axis; and (2) measured **inter- and intra-observer variability** — 1 cardiologist annotated all 500 patients, 2 additional cardiologists independently annotated a 50-patient fold (inter-observer LV Dice ~0.90, Hausdorff ~7.3 mm), and the same expert re-annotated for intra-observer. Endocardial border tracing is canonically subtle/ambiguous.

## Label provenance
1 cardiologist (full set); 2 more on a 50-patient fold for inter-observer; same expert re-annotated for intra-observer. Per-rater contours preserved on the variability fold.

## Size
500 patients × 2 views = 1,000 sequences; reference contours at end-diastole and end-systole.

## Access / licensing
Public, free, registration. https://www.creatis.insa-lyon.fr/Challenge/camus/ ; data: https://humanheart-project.creatis.insa-lyon.fr/database/ ; paper: Leclerc et al., *IEEE TMI* 2019, doi:10.1109/TMI.2019.2900516

## Caveats
- The image-quality grade is one expert's opinion `[VERIFY whether multi-rater]`.
- Multi-rater contours only on the 50-patient fold, not all 500.

## Relevance to detectability
The strongest cardiac fit: an explicit per-image quality stratum *and* a preserved inter-/intra-observer-variability fold on a canonically ambiguous tracing task — both axes of the detectability framing (image difficulty + reader divergence) in echocardiography.
