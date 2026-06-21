# JSRT Standard Digital Image Database

- **Tier:** A — direct subtlety/perceptibility/conspicuity label
- **Modality / anatomy:** Conventional CXR (digitized film, 2048×2048) / pulmonary nodules
- **Finding type:** Pulmonary nodules (malignant + benign)

## Subtlety / perceptibility label
Nodules classified into **5 subtlety levels** by radiologist consensus. ROC analysis from the original paper validated meaningful separation across subtlety bins (Az 0.574–0.991 across the 5 categories).

## Label provenance
Radiologist **consensus** (not per-reader).

## Size
247 CXRs total — 154 with nodules (100 malignant, 54 benign), 93 normals.

## Access / licensing
Open via the JSRT site (registration). http://db.jsrt.or.jp/eng.php. DICOM-format version also distributed by the JSRT image working group.

## Caveats
- Small by modern standards.
- Film-digitized, not native digital.
- Subtlety is **consensus** (not per-reader), so reader-disagreement signal is not preserved.
- Decades-old but widely cited (~800+).

## Relevance to detectability
Direct subtlety label; canonical CXR perceptibility benchmark. Natural modality-transfer test for an LIDC-trained subtlety classifier.
