# CT-ScanGaze

- **Tier:** C — adjacent / partial signal (process-level eye-tracking / gaze proxy)
- **Modality / anatomy:** Chest/body CT (3D volumes) / radiologist gaze
- **Finding type:** Process-level gaze / 3D scanpath signal during CT reading (not a single finding label)

## Subtlety / perceptibility label
No finding-level subtlety label — it carries a **process-level perceptibility signal**: 3D eye-gaze scanpaths from expert radiologists reading CT, capturing where attention dwells and lingers (a direct search-difficulty / perceptibility proxy). Notably the **first public eye-gaze dataset on CT**, extending the gaze paradigm beyond the chest-radiograph gaze sets already in the survey (REFLACX, EGD-CXR, FG-CXR) into 3D volumetric reading.

## Label provenance
Eye-gaze fixation sequences captured from expert radiologists during CT reading. `[VERIFY]` exact reader count.

## Size
909 CT volumes with recorded 3D scanpaths.

## Access / licensing
Public — data on Hugging Face (`phamtrongthang/CT-ScanGaze`), code at github.com/UARK-AICV/CTScanGaze. License **CC-BY-NC-SA-4.0** (non-commercial, share-alike). Paper: Pham et al., "CT-ScanGaze," ICCV 2025, https://arxiv.org/abs/2507.12591

## Caveats
- Reader count and exact anatomy/findings breakdown not enumerated in the README/abstract `[VERIFY via full paper]`.
- Non-commercial + share-alike license.

## Relevance to detectability
The first volumetric (3D) radiology gaze dataset — the same "perceptibility-as-behavior" angle as the existing CXR gaze sets, but in cross-sectional CT, where search patterns over slices are a richer proxy for how hard a finding is to locate.
