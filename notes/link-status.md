# Link Status

Automated link-availability check over the survey's source/access URLs, produced by `scripts/verify_links.py`. Dead/forbidden links are **findings to triage**, not errors — a 403 is usually a bot-block, not a removed resource. Verify any flagged link directly in a browser before acting on it.

**Last checked:** 2026-06-28

**Summary:** 83 OK · 7 redirect · 10 forbidden (403/401/429) · 8 dead · 108 total

| Status | HTTP | URL | Found in | Note |
|---|---|---|---|---|
| dead | — | http://headctstudy.qure.ai/dataset | `datasets/cq500.md`, `resources/sources.md` | unreachable: [Errno -2] Name or service not known |
| dead | — | https://doi.org/10.34894/AECRSD | `datasets/wmh-challenge.md` | unreachable: timed out |
| dead | — | https://wmh.isi.uu.nl/ | `datasets/wmh-challenge.md`, `resources/sources.md` | unreachable: timed out |
| dead | — | https://www.isles-challenge.org/ISLES2015/ | `datasets/isles-2015-siss.md`, `resources/sources.md` | unreachable: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1010) |
| dead | 404 | https://www.kaggle.com/c/rsna-intracranial-hemorrhage-detection | `datasets/rsna-ich.md`, `resources/sources.md` | client error 404 |
| dead | 404 | https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation | `datasets/siim-acr-pneumothorax.md`, `resources/sources.md` | client error 404 |
| dead | 404 | https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection | `datasets/rsna-cervical-spine.md`, `resources/sources.md` | client error 404 |
| dead | 404 | https://www.kaggle.com/datasets/crawford/qureai-headct | `datasets/cq500.md` | client error 404 |
| forbidden | 403 | https://pubs.rsna.org/doi/10.1148/ryai.2020190211 | `datasets/rsna-ich.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://pubs.rsna.org/doi/full/10.1148/ryai.2020200103 | `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://pubs.rsna.org/doi/full/10.1148/ryai.2021200254 | `datasets/rsna-pe.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://pubs.rsna.org/doi/full/10.1148/ryai.230001 | `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://pubs.rsna.org/doi/full/10.1148/ryai.230034 | `datasets/rsna-cervical-spine.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://pubs.rsna.org/doi/full/10.1148/ryai.230126 | `datasets/ucsf-bmsr.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://www.sciencedirect.com/science/article/abs/pii/S1361841521003789 | `datasets/cada.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://www.sciencedirect.com/science/article/pii/S1053811921004936 | `datasets/adam.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://www.sciencedirect.com/science/article/pii/S1053811921008624 | `datasets/msseg-2016.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://www.sciencedirect.com/science/article/pii/S1361841522003085 | `datasets/lits.md`, `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| redirect | 200 | http://bimcv.cipf.es/bimcv-projects/padchest/ | `datasets/padchest.md`, `resources/sources.md` | -> https://bimcv.cipf.es/bimcv-projects/padchest/ |
| redirect | 200 | https://aimi.stanford.edu/shared-datasets | `datasets/chexthought.md` | -> https://aimi.stanford.edu/data |
| redirect | 200 | https://doi.org/10.6084/m9.figshare.30393475 | `datasets/ms3seg.md` | -> https://figshare.com/articles/dataset/MS3SEG_Dataset/30393475 |
| redirect | 200 | https://doi.org/10.6084/m9.figshare.c.4107803 | `datasets/fumpe.md` | -> https://figshare.com/collections/FUMPE/4107803 |
| redirect | 200 | https://physionet.org/content/ct-ich/ | `datasets/physionet-ct-ich.md`, `resources/sources.md` | -> https://physionet.org/content/ct-ich/1.3.1/ |
| redirect | 200 | https://www.synapse.org/brats | `datasets/brats.md`, `resources/sources.md` | -> https://www.synapse.org/Synapse:syn53708126 |
| redirect | 200 | https://zenodo.org/records/3993379 | `datasets/ribfrac.md` | -> https://zenodo.org/records/3993380 |
| OK | 200 | http://db.jsrt.or.jp/eng.php | `datasets/jsrt.md`, `resources/sources.md` |  |
| OK | 200 | http://www.isles-challenge.org/ISLES2018/ | `datasets/isles-2018.md`, `resources/sources.md` |  |
| OK | 200 | https://adam.isi.uu.nl/ | `datasets/adam.md`, `resources/sources.md` |  |
| OK | 200 | https://adam.isi.uu.nl/details/ | `datasets/adam.md` |  |
| OK | 200 | https://arxiv.org/abs/1803.05854 | `datasets/cq500.md`, `resources/sources.md` |  |
| OK | 200 | https://arxiv.org/abs/1901.07441 | `resources/sources.md` |  |
| OK | 200 | https://arxiv.org/abs/2306.00838 | `datasets/brats-mets.md` |  |
| OK | 200 | https://arxiv.org/abs/2307.01984 | `datasets/kits21.md` |  |
| OK | 200 | https://arxiv.org/abs/2308.11298 | `datasets/bhsd.md` |  |
| OK | 200 | https://arxiv.org/abs/2402.09372 | `datasets/ribfrac.md` |  |
| OK | 200 | https://arxiv.org/abs/2405.18435 | `datasets/qubiq.md` |  |
| OK | 200 | https://arxiv.org/abs/2503.10068 | `datasets/panorama.md` |  |
| OK | 200 | https://arxiv.org/abs/2505.08685 | `datasets/curvas.md` |  |
| OK | 200 | https://arxiv.org/abs/2507.12591 | `datasets/ct-scangaze.md` |  |
| OK | 200 | https://arxiv.org/abs/2604.26288 | `resources/sources.md` |  |
| OK | 200 | https://arxiv.org/pdf/2006.10550 | `datasets/chestx-det.md` |  |
| OK | 200 | https://atlas.grand-challenge.org/ | `datasets/atlas-v2.md`, `resources/sources.md` |  |
| OK | 200 | https://cada-as.grand-challenge.org/ | `datasets/cada.md` |  |
| OK | 200 | https://cada.grand-challenge.org/ | `datasets/cada.md`, `resources/sources.md` |  |
| OK | 200 | https://cada.grand-challenge.org/Dataset/ | `datasets/cada.md` |  |
| OK | 200 | https://cdas.cancer.gov/nlst/ | `datasets/nlst.md`, `resources/sources.md` |  |
| OK | 200 | https://github.com/Deepwise-AILab/ChestX-Det10-Dataset | `datasets/chestx-det.md`, `resources/sources.md` |  |
| OK | 200 | https://github.com/GriffinLiang/AISD | `datasets/aisd.md`, `resources/sources.md` |  |
| OK | 200 | https://github.com/Mahdi-Bashiri/MS3SEG | `resources/sources.md` |  |
| OK | 200 | https://github.com/UARK-AICV/CTScanGaze | `resources/sources.md` |  |
| OK | 200 | https://github.com/White65534/BHSD | `datasets/bhsd.md`, `resources/sources.md` |  |
| OK | 200 | https://github.com/anjany/verse | `datasets/verse.md`, `resources/sources.md` |  |
| OK | 200 | https://github.com/neheller/kits21 | `resources/sources.md` |  |
| OK | 200 | https://github.com/radreports/AISD-ischemic-stroke- | `datasets/aisd.md` |  |
| OK | 200 | https://github.com/sb-ai-lab/early_hyperacute_stroke_dataset | `datasets/cpaisd.md`, `resources/sources.md` |  |
| OK | 200 | https://humanheart-project.creatis.insa-lyon.fr/database/ | `datasets/camus.md` |  |
| OK | 200 | https://isles22.grand-challenge.org/ | `datasets/isles-2022.md`, `resources/sources.md` |  |
| OK | 200 | https://kits-challenge.org/kits21/ | `datasets/kits21.md`, `resources/sources.md` |  |
| OK | 200 | https://lndb.grand-challenge.org/ | `datasets/lndb.md`, `resources/sources.md` |  |
| OK | 200 | https://nda.nih.gov/oai/ | `datasets/oai.md`, `resources/sources.md` |  |
| OK | 200 | https://osf.io/nqjyw/ | `datasets/verse.md`, `resources/sources.md` |  |
| OK | 200 | https://panorama.grand-challenge.org/ | `datasets/panorama.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/egd-cxr/1.0.0/ | `datasets/egd-cxr.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/reflacx-xray-localization/1.0.0/ | `datasets/reflacx.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/vindr-cxr/1.0.0/ | `datasets/vindr-cxr.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/vindr-mammo/1.0.0/ | `datasets/vindr-mammo.md`, `resources/sources.md` |  |
| OK | 200 | https://pi-cai.grand-challenge.org/ | `datasets/pi-cai.md`, `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11945730/ | `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5099118/ | `datasets/isles-2015-siss.md`, `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7759925/ | `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8082364/ | `datasets/verse.md`, `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8240494/ | `datasets/isles-2018.md`, `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9203460/ | `datasets/atlas-v2.md`, `resources/sources.md` |  |
| OK | 200 | https://pubmed.ncbi.nlm.nih.gov/29103086/ | `resources/sources.md` |  |
| OK | 200 | https://pubmed.ncbi.nlm.nih.gov/30908194/ | `datasets/wmh-challenge.md`, `resources/sources.md` |  |
| OK | 200 | https://qubiq21.grand-challenge.org/ | `datasets/qubiq.md`, `resources/sources.md` |  |
| OK | 200 | https://registry.opendata.aws/emory-breast-imaging-dataset-embed/ | `datasets/embed.md`, `resources/sources.md` |  |
| OK | 200 | https://registry.opendata.aws/rsna-intracranial-hemorrhage-detection/ | `datasets/rsna-ich.md`, `resources/sources.md` |  |
| OK | 200 | https://registry.opendata.aws/rsna-pulmonary-embolism-detection/ | `datasets/rsna-pe.md`, `resources/sources.md` |  |
| OK | 200 | https://registry.opendata.aws/ucsf-bmsr/ | `datasets/ucsf-bmsr.md`, `resources/sources.md` |  |
| OK | 200 | https://ribfrac.grand-challenge.org/ | `resources/sources.md` |  |
| OK | 200 | https://stanfordaimi.azurewebsites.net/ | `datasets/chexthought.md`, `resources/sources.md`, `notes/follow-ups.md` |  |
| OK | 200 | https://stanfordmlgroup.github.io/competitions/chexpert/ | `datasets/chexpert.md`, `resources/sources.md` |  |
| OK | 200 | https://stanfordmlgroup.github.io/competitions/mura/ | `datasets/mura.md`, `resources/sources.md` |  |
| OK | 200 | https://sycaimedical.com/curvaspdacvi/ | `datasets/curvas-pdacvi.md`, `resources/sources.md` |  |
| OK | 200 | https://www.adcis.net/en/third-party/messidor/ | `datasets/messidor-2.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/ | `datasets/bcs-dbt.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerimagingarchive.net/collection/cbis-ddsm/ | `datasets/cbis-ddsm.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerimagingarchive.net/collection/lidc-idri/ | `datasets/lidc-idri.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerresearchhorizons.com/our-portfolio/our-licensing-opportunities/optimam-mammography-image-database-omi-db | `datasets/optimam-omi-db.md`, `resources/sources.md` |  |
| OK | 200 | https://www.creatis.insa-lyon.fr/Challenge/camus/ | `datasets/camus.md`, `resources/sources.md` |  |
| OK | 200 | https://www.icpsr.umich.edu/web/ICPSR/studies/36684 | `datasets/atlas-v2.md` |  |
| OK | 200 | https://www.midrc.org/ | `datasets/midrc-ricord.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41597-022-01328-z | `datasets/grazpedwri-dx.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41597-022-01875-5 | `datasets/isles-2022.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41597-023-02432-4 | `datasets/fracatlas.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41597-024-03345-6 | `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41597-025-06473-9 | `datasets/curvas.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41597-026-07184-5 | `datasets/ms3seg.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41598-018-31911-7 | `datasets/msseg-2016.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/sdata2017177 | `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/sdata2018180 | `datasets/fumpe.md`, `resources/sources.md` |  |
| OK | 200 | https://zenodo.org/records/10892316 | `datasets/cpaisd.md`, `resources/sources.md` |  |
| OK | 200 | https://zenodo.org/records/13715870 | `datasets/panorama.md`, `resources/sources.md` |  |
| OK | 200 | https://zenodo.org/records/15401568 | `datasets/curvas-pdacvi.md`, `resources/sources.md` |  |
| OK | 200 | https://zenodo.org/records/17736412 | `datasets/isles-2015-siss.md`, `datasets/isles-2018.md`, `resources/sources.md` |  |
| OK | 200 | https://zenodo.org/records/3893496 | `datasets/ribfrac.md` |  |
| OK | 200 | https://zenodo.org/records/3893508 | `datasets/ribfrac.md`, `resources/sources.md` |  |
