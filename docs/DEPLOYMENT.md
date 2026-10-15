# GitHub Pages Deployment

## What
Publish the portal as a static GitHub Pages site.

## Why
The repository already contains the knowledge source. GitHub Pages can serve the frontend without a backend.

## Steps

1. Keep `index.html`, `404.html`, `favicon.svg`, `robots.txt`, `assets/`, and generated `site/` output in the repository root.
2. Regenerate and validate the catalogue as described in [Content Maintenance](./CONTENT-MAINTENANCE.md), then commit the source and generated JSON together.
3. In **Settings → Pages**, verify the existing publishing source. The repository is documented to publish from `main` and `/(root)`; this documentation change does not alter that setting.
4. Wait for the Pages deployment to complete, then open https://anurag-rvnkr1.github.io/Security-Knowledge-Base/.

### Why `main / (root)` works
GitHub Pages takes static files from the selected branch and directory. Because `index.html` is in the root, it becomes the entry page. The browser then loads CSS, JavaScript, catalogue JSON, source Markdown, and the full-text search index when a visitor searches.

## Local verification

From the repository root:

```bash
python -m http.server 8000
```

Open http://localhost:8000/.

Stop with `Ctrl+C`.

Test search, a document, refresh, Back/Forward, code-copy buttons, images, GitHub links, and mobile layout.

## Updating content

The Markdown files remain authoritative. After adding or renaming Markdown:

```bash
python scripts/build-content-index.py
```

Commit both the source change and regenerated `site/content.json`.
Also commit `site/search-index.json`; the generator updates both files.

## What to verify after deployment

- Home page loads.
- Domain cards appear.
- Search works.
- A Markdown document opens.
- Images resolve relative to the source document.
- `Open on GitHub` points to the real source path.
- Spaces and punctuation in paths work.
- Refreshing a document URL preserves the document.
- Browser Back/Forward works.
- Mobile navigation works.
- No horizontal page overflow appears.
