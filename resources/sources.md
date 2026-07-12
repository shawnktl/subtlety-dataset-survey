# Sources

Links / citations for each dataset's source page, carried forward from the survey. Grouped by tier; see each dataset page under `datasets/` for the full per-dataset record.

## Tier A — direct subtlety / conspicuity labels

- **LIDC-IDRI:** https://www.cancerimagingarchive.net/collection/lidc-idri/
- **JSRT:** http://db.jsrt.or.jp/eng.php
- **CBIS-DDSM:** https://www.cancerimagingarchive.net/collection/cbis-ddsm/ ; Lee et al., Sci Data 2017 https://www.nature.com/articles/sdata2017177
- **LNDb:** https://lndb.grand-challenge.org/ ; LNDb v4 https://www.nature.com/articles/s41597-024-03345-6
- **OPTIMAM / OMI-DB:** https://www.cancerresearchhorizons.com/our-portfolio/our-licensing-opportunities/optimam-mammography-image-database-omi-db ; Halling-Brown et al., Radiology AI 2020 https://pubs.rsna.org/doi/full/10.1148/ryai.2020200103

## Tier A/B hybrid

- **CheXthought:** arXiv:2604.26288 https://arxiv.org/abs/2604.26288 ; Stanford AIMI https://stanfordaimi.azurewebsites.net/

## Tier B — reader-disagreement / multi-rater designs

- **VinDr-CXR:** https://physionet.org/content/vindr-cxr/1.0.0/
- **VinDr-Mammo:** https://physionet.org/content/vindr-mammo/1.0.0/
- **MURA:** https://stanfordmlgroup.github.io/competitions/mura/
- **BraTS (review):** https://pmc.ncbi.nlm.nih.gov/articles/PMC11945730/ ; challenge/Synapse https://www.synapse.org/brats
- **Messidor-2:** https://www.adcis.net/en/third-party/messidor/
- **OAI:** https://nda.nih.gov/oai/
- **MIDRC / RICORD:** https://www.midrc.org/
- **PI-CAI:** https://pi-cai.grand-challenge.org/

## Tier C — adjacent / partial signal

- **REFLACX:** https://physionet.org/content/reflacx-xray-localization/1.0.0/
- **EGD-CXR:** https://physionet.org/content/egd-cxr/1.0.0/
- **FG-CXR:** Springer chapter / arXiv:2411.15413 (verify download directly)
- **NLST:** https://cdas.cancer.gov/nlst/ ; missed-cancer analysis https://pmc.ncbi.nlm.nih.gov/articles/PMC7759925/
- **SIIM-ACR Pneumothorax:** https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation
- **BCS-DBT:** https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/
- **EMBED:** https://registry.opendata.aws/emory-breast-imaging-dataset-embed/
- **INbreast:** academic request (restricted)
- **PadChest:** http://bimcv.cipf.es/bimcv-projects/padchest/ ; arXiv:1901.07441 https://arxiv.org/abs/1901.07441
- **CheXpert:** https://stanfordmlgroup.github.io/competitions/chexpert/
- **NIH ChestX-Ray14:** NIH Clinical Center release (Wang et al., 2017)
- **ISBI/MS multi-rater consensus:** Lesjak et al., 2017 https://pubmed.ncbi.nlm.nih.gov/29103086/

## Adjacent references cited in the gaps analysis

- **RSNA PE (original gaps note):** https://pubs.rsna.org/doi/full/10.1148/ryai.2021200254 — now a full Tier A dataset page (see below).

---

## 2026-06-24 wider-net sweep — new dataset sources

### Neuro — ischemic stroke

- **AISD:** https://github.com/GriffinLiang/AISD ; Liang et al., MICCAI 2021 (Symmetry-Enhanced Attention Network for Acute Ischemic Infarct Segmentation with NCCT)
- **CPAISD:** https://zenodo.org/records/10892316 ; Tuchinov et al., arXiv:2404.02518 ; code https://github.com/sb-ai-lab/early_hyperacute_stroke_dataset
- **ISLES 2022:** https://isles22.grand-challenge.org/ ; Hernandez Petzsche et al., Sci Data 2022 https://www.nature.com/articles/s41597-022-01875-5 ; Zenodo DOI 10.5281/zenodo.7153326
- **ISLES 2015 (SISS):** https://www.isles-challenge.org/ISLES2015/ ; Maier et al., Med Image Anal 2017 https://pmc.ncbi.nlm.nih.gov/articles/PMC5099118/ ; Zenodo bundle https://zenodo.org/records/17736412
- **ISLES 2018:** http://www.isles-challenge.org/ISLES2018/ ; Hakim et al., Stroke 2021 https://pmc.ncbi.nlm.nih.gov/articles/PMC8240494/ ; Zenodo https://zenodo.org/records/17736412
- **ATLAS v2.0:** https://atlas.grand-challenge.org/ ; Liew et al., Sci Data 2022 https://pmc.ncbi.nlm.nih.gov/articles/PMC9203460/ ; ICPSR DOI 10.3886/ICPSR36684.v4

### Neuro — hemorrhage / aneurysm

- **CQ500:** http://headctstudy.qure.ai/dataset ; Chilamkurthy et al., The Lancet 2018 https://arxiv.org/abs/1803.05854
- **RSNA ICH:** https://www.kaggle.com/c/rsna-intracranial-hemorrhage-detection ; https://registry.opendata.aws/rsna-intracranial-hemorrhage-detection/ ; Flanders et al. https://pubs.rsna.org/doi/10.1148/ryai.2020190211
- **PhysioNet CT-ICH:** https://physionet.org/content/ct-ich/ (Hssayeni et al.)
- **BHSD:** https://github.com/White65534/BHSD ; arXiv:2308.11298 (MLMI 2023)
- **ADAM:** https://adam.isi.uu.nl/ ; Timmins et al., NeuroImage 2021 https://www.sciencedirect.com/science/article/pii/S1053811921004936
- **CADA:** https://cada.grand-challenge.org/ ; Med Image Anal 2021 https://www.sciencedirect.com/science/article/abs/pii/S1361841521003789

### Neuro — WMH / MS / mets

- **MSSEG-2016:** Commowick et al., NeuroImage 2021 https://www.sciencedirect.com/science/article/pii/S1053811921008624 (Sci Rep 2018 https://www.nature.com/articles/s41598-018-31911-7) ; data via Shanoir (DUA)
- **WMH Challenge (2017):** https://wmh.isi.uu.nl/ ; data DOI 10.34894/AECRSD ; Kuijf et al., IEEE TMI 2019 https://pubmed.ncbi.nlm.nih.gov/30908194/
- **QUBIQ:** https://qubiq21.grand-challenge.org/ ; Menze et al., arXiv:2405.18435
- **BraTS-METS (2023):** Moawad et al., arXiv:2306.00838 ; data on Synapse
- **UCSF-BMSR:** https://registry.opendata.aws/ucsf-bmsr/ ; Rudie et al., Radiology: AI 2024 https://pubs.rsna.org/doi/full/10.1148/ryai.230126
- **MS3SEG:** Bashiri et al., Sci Data 2026 https://www.nature.com/articles/s41597-026-07184-5 ; figshare DOI 10.6084/m9.figshare.30393475 ; code https://github.com/Mahdi-Bashiri/MS3SEG

### Abdomen / body

- **KiTS21:** https://kits-challenge.org/kits21/ ; arXiv:2307.01984 ; code https://github.com/neheller/kits21
- **CURVAS:** https://www.nature.com/articles/s41597-025-06473-9 ; challenge curvas.grand-challenge.org ; results arXiv:2505.08685
- **CURVAS-PDACVI:** https://zenodo.org/records/15401568 ; https://sycaimedical.com/curvaspdacvi/
- **PANORAMA:** https://panorama.grand-challenge.org/ ; data https://zenodo.org/records/13715870 ; method arXiv:2503.10068
- **LiTS:** Med Image Anal 2023 https://www.sciencedirect.com/science/article/pii/S1361841522003085

### Thorax — PE / cardiac

- **RSNA-PE (RSPECT):** https://pubs.rsna.org/doi/full/10.1148/ryai.2021200254 ; augmentation https://pubs.rsna.org/doi/full/10.1148/ryai.230001 ; https://registry.opendata.aws/rsna-pulmonary-embolism-detection/
- **FUMPE:** https://www.nature.com/articles/sdata2018180 ; figshare DOI 10.6084/m9.figshare.c.4107803
- **CAMUS:** https://www.creatis.insa-lyon.fr/Challenge/camus/ ; Leclerc et al., IEEE TMI 2019 (doi:10.1109/TMI.2019.2900516)
- **ChestX-Det:** https://github.com/Deepwise-AILab/ChestX-Det10-Dataset ; arXiv:2006.10550

### MSK / spine

- **VerSe (Genant layer):** https://github.com/anjany/verse ; OSF https://osf.io/nqjyw/ ; Löffler et al., Radiology: AI 2020 https://pmc.ncbi.nlm.nih.gov/articles/PMC8082364/
- **RSNA 2022 Cervical Spine Fracture:** https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection ; https://pubs.rsna.org/doi/full/10.1148/ryai.230034
- **RibFrac:** https://ribfrac.grand-challenge.org/ ; arXiv:2402.09372 ; Zenodo https://zenodo.org/records/3893508
- **GRAZPEDWRI-DX:** https://www.nature.com/articles/s41597-022-01328-z ; figshare DOI 10.6084/m9.figshare.14825193
- **FracAtlas:** https://www.nature.com/articles/s41597-023-02432-4 ; figshare DOI 10.6084/m9.figshare.22363012

### Process-level (gaze)

- **CT-ScanGaze:** Pham et al., ICCV 2025 arXiv:2507.12591 ; data huggingface.co/datasets/phamtrongthang/CT-ScanGaze ; code https://github.com/UARK-AICV/CTScanGaze
