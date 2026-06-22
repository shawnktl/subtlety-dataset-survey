# EMBED (Emory mammography)

- **Tier:** C (possibly B on closer inspection of the schema)
- **Modality / anatomy:** FFDM + DBT / lesion-level annotations
- **Finding type:** Breast lesions (BI-RADS descriptors)

## Subtlety / perceptibility label
**No explicit subtlety/conspicuity field** in the published documentation reviewed. 40,000 annotated lesions with BI-RADS descriptors (mass shape, calcification type, etc.).

## Label provenance
Lesion-level annotations; structured DB (MagView) underlying.

## Size
3.4M images, 116k women, racially diverse.

## Access / licensing
AWS Open Data Registry + Emory DUA. https://registry.opendata.aws/emory-breast-imaging-dataset-embed/

## Caveats
- **Verify before relying on:** the headline paper doesn't list conspicuity, but the underlying MagView structured DB may include a field not surfaced in the headline paper. Confirm subtlety/conspicuity coverage directly — possible the structured DB has a field not surfaced. Worth a direct check of the schema.

## Relevance to detectability
Adjacent today; could upgrade to a difficulty-proxy dataset if the schema turns out to carry a conspicuity field.
