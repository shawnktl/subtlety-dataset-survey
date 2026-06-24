# CADA (Cerebral Aneurysm Detection And Analysis)

- **Tier:** C — adjacent / partial signal (canonically subtle finding; extreme detection imbalance)
- **Modality / anatomy:** 3D rotational X-ray angiography (3DRA / 3D-DSA) / cerebral vasculature
- **Finding type:** Cerebral aneurysms — detection, segmentation, and rupture-risk estimation (3 tasks)

## Subtlety / perceptibility label
No explicit subtlety field. Extreme foreground/background imbalance (mean aneurysm volume 0.391 mL vs image volumes 280–2,350 mL) makes small aneurysms a canonical hard-detection problem; cohort is suspected-SAH patients. Difficulty is structural, not a labeled perceptibility axis.

## Label provenance
Expert annotations of aneurysms on 3DRA. `[VERIFY]` rater count / consensus.

## Size
109 training datasets with 127 annotated aneurysms + 22 test datasets (cohort of 115 patients).

## Access / licensing
Open via Grand Challenge registration. https://cada.grand-challenge.org/ ; dataset: https://cada.grand-challenge.org/Dataset/ ; segmentation track: https://cada-as.grand-challenge.org/ ; paper: CADA 2020, *Medical Image Analysis* 2021, https://www.sciencedirect.com/science/article/abs/pii/S1361841521003789

## Caveats
- 3DRA is invasive / less common than MRA or CTA.
- Test labels withheld; highly imbalanced.

## Relevance to detectability
Complements ADAM with an angiography-modality aneurysm benchmark; the tiny-target-in-huge-volume framing is a clean illustration of why small aneurysms are canonically subtle, though no per-lesion perceptibility label is provided.
