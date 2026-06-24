# Search Strategy — Living Discovery Methods

This is the **living, evolving** strategy document that drives the weekly discovery
pass. It is both **machine-read** (by `scripts/find_candidates.py`, which parses the
query templates and channel list below) and **human/agent-read** (by an agent following
`notes/refresh-agent.md`).

**It is version-controlled and cumulative.** Promote methods that surface *real* new
datasets; retire ones that only produce noise. **Never overwrite the effectiveness log
— always append.**

---

## How `find_candidates.py` reads this file

The candidate finder extracts its query set from the fenced ` ```queries ` block under
**Query templates** below (one query per non-blank, non-comment line). It also reads the
**Anchor datasets** list for citation chasing. Everything else in this file is for the
human/agent reader. If you add a query template you want the script to use, add it inside
that fenced block. If the block is missing or empty, the script falls back to a small
built-in default set (and notes that in the run log).

---

## Channels

Each channel below is keyless/open (or degrades gracefully without a key). The script
queries the scholarly + a subset of dataset-repository channels automatically; channels
marked **(manual)** are for the agent's manual web pass (no clean keyless API, or
JS-rendered listings the script can't reach reliably).

### Scholarly (scripted)

| Channel | Endpoint | Query recipe |
|---|---|---|
| **Semantic Scholar Graph API** | `https://api.semanticscholar.org/graph/v1/paper/search?query=<q>&fields=title,year,externalIds,abstract,url,openAccessPdf` | Run each query template. Then citation-chase the anchor datasets: `/paper/<id>/references` and `/paper/<id>/citations`. Unauthenticated calls are heavily throttled (HTTP 429) — back off and continue; partial results are fine. |
| **OpenAlex** | `https://api.openalex.org/works?search=<q>&per-page=25` | Run each query template against the `works` `search`. Polite-pool: send a `mailto` in the User-Agent. Also usable for cites/cited-by via `filter=cites:<id>` / `cited_by:<id>` if an anchor's OpenAlex ID is known. |
| **Europe PMC** | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<q>&format=json&pageSize=25` | Run each query template. Returns biomedical lit incl. preprints; good for radiology reader-study papers. |

### Dataset repositories (scripted where keyless)

| Channel | Endpoint | Notes |
|---|---|---|
| **Zenodo** | `https://zenodo.org/api/records?q=<q>&type=dataset&size=20` | Keyless for search. Filters to `type=dataset`. |
| **Figshare** | `https://api.figshare.com/v2/articles/search` (POST JSON `{"search_for": "<q>"}`) | Keyless search. Returns articles incl. datasets. |
| **HuggingFace datasets** | `https://huggingface.co/api/datasets?search=<q>&limit=20` | Keyless. Good for ML-packaged medical datasets. |

### Dataset repositories (manual web pass — agent only)

| Channel | Where | Why manual |
|---|---|---|
| **PhysioNet** | https://physionet.org/about/database/ | Listing is paginated HTML; no clean keyless search API. Browse the database list for new radiology releases. |
| **TCIA** | https://www.cancerimagingarchive.net/collections/ + REST API `https://services.cancerimagingarchive.net/services/v4/TCIA/query/getCollectionValues` | The REST API returns collection *names* only (no subtlety metadata); judging relevance needs the human-readable collection pages. The script may probe the name list; relevance triage is manual. |
| **grand-challenge.org** | https://grand-challenge.org/challenges/ | Challenge listings are JS-rendered; browse for new reader-study / detection challenges. |
| **Papers With Code** | https://paperswithcode.com/datasets?q=<q> | Dataset search; API has been unstable. Browse manually. |
| **OpenNeuro** | https://openneuro.org/search | Neuro MR/fMRI; GraphQL API exists but schema shifts — browse manually. |
| **Kaggle** | https://www.kaggle.com/datasets?search=<q> | Needs `kaggle.json` API token. The script probes only if `KAGGLE_USERNAME`/`KAGGLE_KEY` env vars are present; otherwise it's a manual pass. |

---

## Query templates

The fenced block below is the **machine-read query set**. One query per line. Lines
starting with `#` are comments and ignored. Keep queries broad enough to catch new
work but specific enough to limit noise. Add per-modality and per-construct variants as
you learn what surfaces real datasets (record results in the effectiveness log).

```queries
# --- core subtlety / perceptibility constructs ---
radiology dataset lesion subtlety annotation
medical imaging perceptibility dataset
lesion conspicuity dataset radiology
detectability radiology reader study dataset
# --- reader-study / observer-performance designs (difficulty proxy) ---
observer performance study dataset radiology
multi-reader multi-case dataset radiology annotation
reader disagreement dataset medical imaging
inter-rater variability radiology dataset public
# --- difficulty / hard-case framings ---
hard cases dataset radiology detection
missed findings dataset radiology
case difficulty annotation medical imaging dataset
# --- modality-specific variants ---
mammography lesion conspicuity BI-RADS dataset
chest radiograph subtle nodule dataset reader
CT lung nodule subtlety rating dataset
brain MRI lesion multi-rater dataset
fundus retinal lesion grader agreement dataset
# --- eye-tracking / process-level (Tier C signal) ---
eye tracking radiologist dataset gaze chest
```

---

## Anchor datasets (Tier A) — for citation chasing

The script chases forward (citations) and backward (references) from these anchors via
Semantic Scholar. Each entry: a name + the best DOI/arXiv/identifier to resolve it.
Update DOIs here if a better anchor paper is found.

```anchors
# name | identifier (DOI, arXiv id, or Semantic Scholar paperId)
LIDC-IDRI | 10.1118/1.3528204
JSRT | 10.2214/ajr.174.1.1740071
CBIS-DDSM | 10.1038/sdata.2017.177
LNDb | 10.1038/s41597-024-03345-6
CheXthought | arXiv:2604.26288
```

---

## Citation-chasing procedure

For each anchor in the `anchors` block:

1. **Resolve** the identifier to a Semantic Scholar `paperId`
   (`/paper/DOI:<doi>` or `/paper/arXiv:<id>`).
2. **Backward (references):** `GET /paper/<id>/references` — papers the anchor builds on.
   Useful for finding the *original* dataset/observer-study papers an anchor reused.
3. **Forward (citations):** `GET /paper/<id>/citations` — papers that *use* the anchor.
   This is where new datasets that extend or benchmark against the anchor surface.
4. For each cited/referencing paper, flag it as a candidate if its title/abstract
   matches any query construct (subtlety, conspicuity, reader study, multi-rater, …)
   **and** it isn't already deduped against `datasets/`.
5. Manual extension (agent): for the highest-signal citing papers, open them and check
   whether they *release* a dataset (many reader-study papers don't) — only released,
   accessible datasets become dataset pages.

---

## Dedup rule

A hit is a duplicate of an existing dataset if **any** of:
- its DOI matches a DOI already cited in `datasets/` or `resources/sources.md`;
- its title/name contains an existing dataset's name (case-insensitive); or
- its source URL host+path matches a URL already in `datasets/` / `resources/sources.md`.

`find_candidates.py` applies this automatically against the markdown corpus.

---

## Effectiveness log (APPEND-ONLY)

Each refresh pass appends a dated entry recording **which channels/queries yielded real
new datasets vs. noise, dead ends, and any new method discovered.** This is how the
strategy measurably improves run over run. **Promote what works; retire what doesn't.
Never edit or delete past entries — only append below.**

<!-- APPEND NEW ENTRIES ABOVE THIS LINE, NEWEST FIRST -->

### 2026-06-24 — comprehensive wider-net discovery sweep (gap regions: neuro/stroke, abdomen/body, +PE/spine/cardiac)

**Goal:** widen the (then-26, chest/breast-dominated) index by anatomy AND by *kind* of detectability signal (not just explicit "subtlety 1–5"). **Result: +33 datasets → 59 total.** By region: 6 ischemic-stroke (was 0), 4 hemorrhage + 2 aneurysm, 3 WMH/MS-multirater + 3 brain-mets, 5 abdominal (was 0), 2 PE + 1 cardiac, 4 fracture/spine, 1 volumetric gaze. Tier landing: A 5→8, B 8→20, C 12→30.

**Channels run this sweep:** scholarly (Semantic Scholar, OpenAlex, Europe PMC) + dataset repos (Zenodo, Figshare, HuggingFace) via the existing `find_candidates.py` run (candidates.md, 480 leads), plus heavy manual web-search verification per gap region (Grand-Challenge, TCIA, PhysioNet, GitHub, AWS Open Data, OSF, Mendeley). Each candidate was confirmed to (a) be publicly accessible and (b) carry a real detectability/disagreement/canonical-subtlety signal before being added.

**What worked (promote):**
- **Conceptual-scope widening was the single biggest lever.** Treating *canonically-subtle findings* (early ischemic change, small ICH, PDAC, subsegmental PE, small mets, occult fractures) as in-scope — not just explicit labels — is what unlocked the gap regions. Most new hits have NO numeric subtlety field; they qualify via canonical-subtlety or preserved multi-rater disagreement.
- **"preserved per-rater masks" is the highest-quality Tier-B filter.** Datasets that *release* individual rater annotations (MSSEG-2016 7-rater, QUBIQ, KiTS21 3-per-ROI, CURVAS/-PDACVI, WMH O3/O4, CQ500 reads.csv) are genuinely useful, vs the many "consensus only" sets where disagreement is fused away. Query constructs that surfaced these: `inter-rater variability radiology dataset public`, `MultiRater MultiOrgan`, plus challenge names (QUBIQ, CURVAS).
- **Grand-Challenge + Zenodo challenge-data records** are the richest vein for stroke/abdomen (ISLES editions, PANORAMA, CURVAS, INSTANCE, ADAM, CADA, KiTS, LiTS, RibFrac). The auto-scanned candidates.md had already flagged ISLES 2022, PANORAMA ×4, and the MultiRater abdominal paper — those leads converted directly to pages.
- **Explicit-conspicuity-label hunt in stroke paid off:** AISD (clear/blurred/invisible NCCT infarct) and CPAISD (perceptibility-defined) are the rare Tier-A finds outside the chest — found by searching acute-ischemic NCCT segmentation and *reading the annotation protocol*, not by a generic "subtlety" query.
- **RSNA-PE QA-flag claim verified** (QA-Motion / QA-Contrast / Flow-Artifact / True-Filling-Defect / Indeterminate are real per-exam labels) — promoted from an "adjacent reference" to a full Tier-A page.

**Dead ends / excluded (retire or down-weight):**
- **Generic multi-organ segmentation sets have no perceptibility angle** — DeepLesion, AMOS, AbdomenCT-1K, NIH Pancreas-CT, plain MSD Liver/organ tasks were all evaluated and **deliberately excluded** (no subtlety label, no preserved disagreement). The query `medical imaging perceptibility dataset` on Zenodo returns mostly noise (thermal/phishing/traffic-sign datasets) — keep but down-weight.
- **CANDID-PTX excluded** — strong pneumothorax multi-annotator candidate (6 RANZCR physicians) but since Feb 2024 restricted to Health New Zealand users; fails the public-access bar. Re-check if NZ governance changes.
- **MSSEG-2 (2021)** kept at C not B — its reference is 4-expert *consensus*, per-rater masks not clearly released (vs MSSEG-2016's released 7-rater masks). `[VERIFY]` before promoting.
- **No publicly-downloadable mammography eye-tracking dataset** confirmed (research exists, data not released).

**Genuinely lacking regions (say-so, don't pad):**
- **MR with an *explicit* per-lesion subtlety label**: still essentially none (the original survey's sharpest gap). The sweep strongly eased the *disagreement* axis on MR (MSSEG/WMH/QUBIQ/BraTS-METS) but not the *labeled-subtlety* axis.
- **Pediatric** (beyond GRAZPEDWRI-DX wrist) and **ultrasound / nuclear medicine**: no subtlety-labeled public data surfaced.
- **PDAC / pancreas reader-study per-reader data**: PANORAMA ran a reader study but per-reader data isn't clearly public (`[VERIFY]`); CURVAS-PDACVI's 5 per-rater masks are the workaround.

**Method notes for next sweep:** citation-chasing the new Tier-A/B anchors (AISD, CQ500, MSSEG-2016, KiTS21, CURVAS) would compound — add their DOIs to the `anchors` block. Suggested new query templates: `intracranial hemorrhage multi-reader dataset`, `stroke lesion inter-rater dataset`, `pancreatic cancer detection dataset reader study`, `multi-rater segmentation dataset per-annotator`, `eye tracking radiologist CT gaze dataset`.

### (seed) — strategy initialized

- Channels wired into `find_candidates.py`: Semantic Scholar (search + citation chasing),
  OpenAlex, Europe PMC, Zenodo, Figshare, HuggingFace datasets.
- Manual-pass channels documented: PhysioNet, TCIA, grand-challenge, Papers With Code,
  OpenNeuro, Kaggle.
- No effectiveness data yet — first scheduled/dispatched run will populate this log.
