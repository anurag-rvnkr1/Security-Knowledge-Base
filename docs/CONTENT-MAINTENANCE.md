# Maintaining Security Knowledge Base

Markdown files are the authoritative learning material. The static portal reads the generated catalogue and search index; do not edit either generated JSON file by hand.

## Build and validate

Run from the repository root with Python 3 and Node.js available:

```bash
python scripts/build-content-index.py
python scripts/validate-knowledge-base.py
python scripts/build-content-index.py --check
node --check assets/js/app.js
```

The generator uses only the Python standard library. It writes `site/content.json` and `site/search-index.json`. The first file contains collection, document, excerpt, asset, and learning-path metadata. The second is a compact inverted index of title, collection, heading, tag, and body terms; the portal downloads it only when a visitor searches. This avoids duplicating full Markdown bodies in the catalogue.

Commit regenerated files with their source changes. `--check` compares both generated outputs with the current repository content without writing files. The validator also checks generated-output reproducibility, catalogue paths and counts, local Markdown links, heading fragments, code fences, root-page assets, sitemap metadata, and likely high-confidence secret signatures. Its local Markdown parser is deliberately conservative: it does not fully implement reference-style links, raw HTML routing, or every GitHub heading-slug edge case. Warnings require human review; only errors fail validation.

## Add a collection or chapter

1. Add a descriptive top-level directory for a new subject, or use the closest existing collection. The catalogue discovers Markdown in new content directories automatically. `assets`, `docs`, repository metadata, generated output, and tooling have separate handling.
2. Add Markdown files using the directory's existing naming and numbering convention. Numbered chapters sort numerically; a collection `README.md`/`Readme.md` appears first, followed by numbered chapters and then remaining files in a stable case-insensitive order.
3. Include a collection `README.md` with a useful overview and links to files that actually exist. CTF subdirectories are separate collections so unrelated challenge categories do not become one chapter sequence.
4. Add a name or description to `COLLECTION_METADATA` in `scripts/build-content-index.py` only when the generated default is not sufficiently clear. That configuration is the single authoritative display-metadata source.
5. Run the build and validation commands above. Review changed JSON and confirm the new paths, type assignments, order, counts, and search terms.

Use one `#` heading for a document title, `##` for its main sections, and deeper levels for nested sections. When correcting legacy heading structure, preserve heading text so existing fragments remain stable; review links and the document outline rather than applying an unreviewed bulk rewrite.

## Add or link a diagram

Store repository diagrams under `assets/diagrams/` (or another appropriate existing asset directory) and use an SVG or raster image format already supported by the catalogue. Link relative to the Markdown source file, for example:

```markdown
![Data flow between the sensor and analysis service](../../assets/diagrams/example.svg)
```

Use concise descriptive alt text, preserve attribution, and verify that the resolved image path appears in the generated catalogue. The reader serves only indexed local images; external images are not loaded.

## Maintain learning paths

The homepage paths are configured in `LEARNING_PATHS` in `scripts/build-content-index.py`. Use collection IDs that exist and connect each step to an actual first learning document. The generator resolves step paths from the collection's ordered documents and fails when a configured path has fewer than two available steps. Keep the narrative guidance in [Learning Paths](./Learning-Paths.md) aligned with the generated paths.

## Test locally

Serve the repository root over HTTP; `file://` URLs do not support the fetches used by the portal:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`. Check search (including a body-only term and a no-result query), collection filtering, a direct `?doc=...` URL, refresh, browser Back/Forward, heading fragments, previous/next within a collection, internal links and diagrams, an invalid path, and mobile navigation/contents. Use browser developer tools to review failed requests and accessibility issues. Stop the local server with `Ctrl+C`.

## GitHub Pages publishing

The portal remains plain HTML, CSS, vanilla JavaScript, Markdown, and generated JSON. The repository documentation describes publishing from `main` at the repository root; verify the repository's **Settings → Pages** source before changing it. The validation workflow checks pull requests and pushes to `main`; it does not deploy or change the Pages publishing source. Keep the generated JSON committed and current so the workflow can rebuild it and confirm there are no generated diffs.
