# CheXpert

- **Tier:** C — uncertainty axis exists but is upstream of perceptibility
- **Modality / anatomy:** CXR / 14 observations
- **Finding type:** Thoracic observations

## Subtlety / perceptibility label
NLP-derived labels with **uncertainty values** (positive / negative / uncertain / blank). This is a *labeler* uncertainty, not a reader perceptibility rating, but the uncertain class is sometimes used as a proxy for "difficult to call."

## Label provenance
NLP-derived from reports.

## Size
224,316 images, 65,240 patients.

## Access / licensing
Open via Stanford AIMI. https://stanfordmlgroup.github.io/competitions/chexpert/

## Caveats
- The uncertainty label reflects report-language ambiguity, not visual subtlety per se.
- Heavy known label-noise issues.

## Relevance to detectability
Uncertainty axis exists but is upstream of perceptibility.
