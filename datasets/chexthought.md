# CheXthought — highest-leverage new discovery

- **Tier:** A/B hybrid — direct operationalization of case difficulty / inter-reader disagreement
- **Modality / anatomy:** CXR / general thoracic
- **Finding type:** General thoracic (reasoning + attention, not categorical findings)

## Subtlety / perceptibility label
**Chain-of-thought reasoning traces** (103,592 traces) + **synchronized visual attention annotations** (~6.6M) across 50,312 multi-read CXRs. Multi-reader design supports modeling of human–human and AI–human disagreement directly from the image. Captures *how* radiologists communicate uncertainty.

## Label provenance
Contributed by **501 radiologists in 71 countries**; multi-read design.

## Size
50,312 CXRs, 103k reasoning traces, ~6.6M visual attention annotations.

## Access / licensing
Stanford AIMI shared datasets — non-commercial research free; commercial license $70k/yr per dataset. https://stanfordaimi.azurewebsites.net/ (and https://aimi.stanford.edu/shared-datasets)

## Caveats
- Very new (released 2026; paper arXiv:2604.26288).
- **Verify before relying on:** referenced details come from the arXiv preprint (arXiv:2604.26288) and a third-party blog (allhealthtech). Confirm directly on the Stanford AIMI portal that the dataset is downloadable and that the chain-of-thought + visual attention components are included in the public release (not held back for commercial license).

## Relevance to detectability
**Most aligned dataset with the broader detectability/perceptibility framing.** Not a categorical subtlety label, but the *direct* operationalization of "case difficulty / inter-reader disagreement / uncertainty communication" at unprecedented scale. **Pursue first** (see `notes/follow-ups.md`).
