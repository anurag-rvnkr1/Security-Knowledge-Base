# GitHub Pages Deployment

## What
Publish the portal as a static GitHub Pages site.

## Why
The repository already contains the knowledge source. GitHub Pages can serve the frontend without a backend.

## Steps

1. Open https://github.com/anurag-rvnkr1/Security-Knowledge-Base.
2. Put `index.html`, `404.html`, `favicon.svg`, `robots.txt`, `assets/`, `site/`, and `scripts/` in the repository root.
3. Commit to `main`.
4. Open **Settings → Pages**.
5. Under **Build and deployment**, choose **Deploy from a branch**.
6. Select **main**.
7. Select **/(root)**.
8. Click **Save**.
9. Wait for GitHub Pages to publish.
10. Open https://anurag-rvnkr1.github.io/Security-Knowledge-Base/.

### Why `main / (root)` works
GitHub Pages takes static files from the selected branch and directory. Because `index.html` is in the root, it becomes the entry page. The browser then loads the CSS, JavaScript, JSON index, and source Markdown.

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
