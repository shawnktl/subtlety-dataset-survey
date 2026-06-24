# Link Status

Automated link-availability check over the survey's source/access URLs, produced by `scripts/verify_links.py`. Dead/forbidden links are **findings to triage**, not errors — a 403 is usually a bot-block, not a removed resource. Verify any flagged link directly in a browser before acting on it.

**Last checked:** 2026-06-22

**Summary:** 26 OK · 3 redirect · 2 forbidden (403/401/429) · 1 dead · 32 total

| Status | HTTP | URL | Found in | Note |
|---|---|---|---|---|
| dead | 404 | https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation | `datasets/siim-acr-pneumothorax.md`, `resources/sources.md` | client error 404 |
| forbidden | 403 | https://pubs.rsna.org/doi/full/10.1148/ryai.2020200103 | `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| forbidden | 403 | https://pubs.rsna.org/doi/full/10.1148/ryai.2021200254 | `resources/sources.md` | bot-block / auth (403) — verify manually in a browser |
| redirect | 200 | http://bimcv.cipf.es/bimcv-projects/padchest/ | `datasets/padchest.md`, `resources/sources.md` | -> https://bimcv.cipf.es/bimcv-projects/padchest/ |
| redirect | 200 | https://aimi.stanford.edu/shared-datasets | `datasets/chexthought.md` | -> https://aimi.stanford.edu/data |
| redirect | 200 | https://www.synapse.org/brats | `datasets/brats.md`, `resources/sources.md` | -> https://www.synapse.org/Synapse:syn53708126 |
| OK | 200 | http://db.jsrt.or.jp/eng.php | `datasets/jsrt.md`, `resources/sources.md` |  |
| OK | 200 | https://arxiv.org/abs/1901.07441 | `resources/sources.md` |  |
| OK | 200 | https://arxiv.org/abs/2604.26288 | `resources/sources.md` |  |
| OK | 200 | https://cdas.cancer.gov/nlst/ | `datasets/nlst.md`, `resources/sources.md` |  |
| OK | 200 | https://lndb.grand-challenge.org/ | `datasets/lndb.md`, `resources/sources.md` |  |
| OK | 200 | https://nda.nih.gov/oai/ | `datasets/oai.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/egd-cxr/1.0.0/ | `datasets/egd-cxr.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/reflacx-xray-localization/1.0.0/ | `datasets/reflacx.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/vindr-cxr/1.0.0/ | `datasets/vindr-cxr.md`, `resources/sources.md` |  |
| OK | 200 | https://physionet.org/content/vindr-mammo/1.0.0/ | `datasets/vindr-mammo.md`, `resources/sources.md` |  |
| OK | 200 | https://pi-cai.grand-challenge.org/ | `datasets/pi-cai.md`, `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11945730/ | `resources/sources.md` |  |
| OK | 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7759925/ | `resources/sources.md` |  |
| OK | 200 | https://pubmed.ncbi.nlm.nih.gov/29103086/ | `resources/sources.md` |  |
| OK | 200 | https://registry.opendata.aws/emory-breast-imaging-dataset-embed/ | `datasets/embed.md`, `resources/sources.md` |  |
| OK | 200 | https://stanfordaimi.azurewebsites.net/ | `datasets/chexthought.md`, `resources/sources.md`, `notes/follow-ups.md` |  |
| OK | 200 | https://stanfordmlgroup.github.io/competitions/chexpert/ | `datasets/chexpert.md`, `resources/sources.md` |  |
| OK | 200 | https://stanfordmlgroup.github.io/competitions/mura/ | `datasets/mura.md`, `resources/sources.md` |  |
| OK | 200 | https://www.adcis.net/en/third-party/messidor/ | `datasets/messidor-2.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/ | `datasets/bcs-dbt.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerimagingarchive.net/collection/cbis-ddsm/ | `datasets/cbis-ddsm.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerimagingarchive.net/collection/lidc-idri/ | `datasets/lidc-idri.md`, `resources/sources.md` |  |
| OK | 200 | https://www.cancerresearchhorizons.com/our-portfolio/our-licensing-opportunities/optimam-mammography-image-database-omi-db | `datasets/optimam-omi-db.md`, `resources/sources.md` |  |
| OK | 200 | https://www.midrc.org/ | `datasets/midrc-ricord.md`, `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/s41597-024-03345-6 | `resources/sources.md` |  |
| OK | 200 | https://www.nature.com/articles/sdata2017177 | `resources/sources.md` |  |
