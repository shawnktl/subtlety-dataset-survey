# Subtlety / Perceptibility Dataset Survey

A browsable reference of 26 public radiology datasets that annotate finding **subtlety / perceptibility / conspicuity** — or carry a usable difficulty proxy (reader disagreement, multi-rater designs, eye-tracking signal). Built from a completed survey spawned by `nodule-detectability`.

## Browse it

- **Live site (GitHub Pages):** https://shawnktl.github.io/subtlety-dataset-survey/
- Or read the markdown directly, starting from [index.md](index.md).

The site is a static HTML rendering of the markdown in this repo — same content, just navigable in a browser with a tier-ranked landing page and one page per dataset.

## Start here

- **[index.md](index.md)** — tier-ranked table linking every dataset page.
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** — scope, why it exists, how to use it.
- **[notes/follow-ups.md](notes/follow-ups.md)** — top-3 next moves + the MR-subtlety gap.
- **[datasets/](datasets/)** — one page per dataset.
- **[resources/sources.md](resources/sources.md)** — links/citations.

## Tiers

- **A** — direct subtlety/conspicuity label (LIDC-IDRI, JSRT, CBIS-DDSM, LNDb, OPTIMAM).
- **B** — reader-disagreement / multi-rater difficulty proxy (+ CheXthought as an A/B hybrid).
- **C** — adjacent / partial signal.

## Rebuilding the site

The HTML under `docs/` is generated from the markdown sources by a dependency-light,
standard-library-only build script. After editing any markdown (`index.md`,
`datasets/*.md`, `notes/*.md`, `resources/*.md`, `PROJECT_SUMMARY.md`), rebuild with:

```bash
python scripts/build_site.py
```

This regenerates the full `docs/` tree deterministically (re-running with unchanged
sources produces byte-identical output). Commit the regenerated `docs/` alongside the
markdown change. No external packages are required (Python 3.12+).

Publishing: a GitHub Actions workflow (`.github/workflows/pages.yml`) deploys the
committed `docs/` folder to GitHub Pages on every push to `master`. Set the repo's
**Settings → Pages → Source** to **GitHub Actions** once, and the live URL above
updates automatically on merge.

> Note: `BOOTSTRAP.md`, `CLAUDE.md`, `study/`, and `review/` are leftovers from the generic knowledge-base bootstrap template and are not part of this reference. (`scripts/build_site.py` is part of this reference — it builds the site; the other `scripts/*.py` are bootstrap leftovers.)
