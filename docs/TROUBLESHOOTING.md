# Troubleshooting

## 1. 404 page
**Cause:** Pages source is wrong or deployment is still propagating.
**Diagnose:** Settings → Pages; confirm `main` and `/(root)`.
**Fix:** Save the correct source and wait for deployment.

## 2. Blank page
**Cause:** JavaScript or the content index failed.
**Diagnose:** F12 → Console and Network.
**Fix:** Confirm `assets/js/app.js` and `site/content.json` exist and are reachable.

## 3. CSS not loading
**Cause:** Wrong asset path.
**Diagnose:** Network → reload → inspect `style.css`.
**Fix:** Use `assets/css/style.css`, not `/assets/css/style.css`.

## 4. JavaScript not loading
**Cause:** Wrong path or syntax error.
**Diagnose:** Network and Console.
**Fix:** Verify `assets/js/app.js` and hard-refresh.

## 5. Markdown not loading
**Cause:** The document path is not in the generated catalogue, or its local Pages request failed.
**Diagnose:** Inspect the document request and confirm its exact case and punctuation in the repository.
**Fix:** Verify the source file, then regenerate `site/content.json` and `site/search-index.json`.

## 6. Search not working
**Cause:** The catalogue or lazily loaded full-text index did not load.
**Diagnose:** Check both `site/content.json` and `site/search-index.json` under the Pages URL.
**Fix:** Run `python scripts/build-content-index.py` and `python scripts/validate-knowledge-base.py`, commit generated output, and hard-refresh.

## 7. Images not loading
**Cause:** Relative image path is wrong.
**Diagnose:** Inspect the generated image URL.
**Fix:** Keep the image path valid relative to its Markdown source and ensure its file is included in the generated local-image catalogue. External images are intentionally not fetched by the reader.

## 8. Broken Markdown links
**Cause:** Target moved or path differs in case/punctuation.
**Diagnose:** Compare the target with the GitHub source tree.
**Fix:** Correct the Markdown path, then regenerate the index if filenames changed.

## 9. GitHub Pages not publishing
**Cause:** Pages configuration or deployment state.
**Diagnose:** Settings → Pages and repository deployment status.
**Fix:** Select **Deploy from a branch → main → /(root)**.

## 10. Wrong base path
**Cause:** Root-relative asset paths.
**Diagnose:** Look for URLs beginning with `/assets`.
**Fix:** Use relative paths such as `assets/css/style.css`.

## 11. Folder names containing spaces
**Cause:** URL characters were not encoded.
**Diagnose:** Compare the requested path with GitHub.
**Fix:** The application encodes every path component with `encodeURIComponent()`. Keep exact source paths in `content.json`.

## 12. Browser cache
**Fix:** Hard refresh with `Ctrl+Shift+R` on Windows/Linux or `Cmd+Shift+R` on macOS.

## 13. Console errors
**Diagnose:** Read the first Console error and inspect its Network request.
**Fix:** Repair that resource before changing unrelated files.

## 14. CORS / fetch errors locally
**Cause:** Opening `index.html` using `file://`.
**Fix:** Run `python -m http.server 8000` from the repository root and use `http://localhost:8000/`.

## 15. Back/Forward problems
**Cause:** Document state is carried in the `doc` query parameter and browser history entries.
**Fix:** Use the reader's close control to return to the opening collection or page. Browser Back and Forward traverse document entries; refreshing a direct document URL should reopen the same source.
