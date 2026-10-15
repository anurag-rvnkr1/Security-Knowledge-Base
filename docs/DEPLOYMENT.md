# GitHub Pages Deployment

The portal is a static HTML/CSS/JavaScript application. It reads the generated
catalogue and search index, then fetches the Markdown sources served alongside
the site. There is no build-time framework or backend.

## Publishing configuration

The repository contains no GitHub Pages deployment workflow. The CI workflow
validates content and code; it does not publish the site. The Pages repository
setting is not available in this checkout, so a maintainer must confirm it in
**Settings → Pages**. The expected configuration for the published URL is
**Deploy from a branch → `main` → `/(root)`**. If the repository uses a
different configuration, update this guide and verify relative asset paths
against that deployment.

## Local preview

From the repository root, run:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/>. A local HTTP server is required because the
browser loads JSON and Markdown with `fetch()`; a `file://` preview is not
supported. Stop the server with `Ctrl+C`.

## Regenerate and validate

Markdown files are the source of truth. After adding, removing, or renaming a
document, rebuild both generated files:

```bash
python scripts/build-content-index.py
```

Before submitting, run the same checks used in CI:

```bash
python -m unittest discover -s tests -v
python scripts/build-content-index.py --check
python scripts/validate-knowledge-base.py
node --check assets/js/app.js
```

Commit source changes together with regenerated `site/content.json` and
`site/search-index.json`. Do not edit those JSON files by hand. The search
index is loaded only when a visitor starts searching.

## Preview checklist

- Home, collection cards, learning-path starts, labs, CTF writeups, and
  references load.
- Search finds terms from titles, headings, and document text; errors can be
  retried.
- A document opens from search and from a collection, and its direct URL
  survives refresh.
- Browser Back/Forward, reader close, and focus restoration behave as expected.
- Relative Markdown links, fragments, images, and GitHub source links work.
- Code-copy controls provide feedback; wide code and tables remain contained.
- Keyboard navigation, Escape, mobile table of contents, reduced motion, and
  mobile navigation work.
- No page-level horizontal overflow is introduced at narrow viewport widths.

## After publishing

Confirm the Pages deployment status in GitHub, then test the published URL in a
browser. Check the browser console and network panel for failed catalogue,
search-index, stylesheet, script, or Markdown requests. A successful static
build or valid sitemap does not prove that dynamically rendered documents will
be indexed by search engines.
