# Repository Assets

## Purpose

Store reusable diagrams, screenshots, icons, and templates used by repository documentation. Add assets only when they clarify or support a specific document; empty categories are intentionally not tracked by Git.

## Directory Structure

- `images/` — explanatory raster images.
- `diagrams/` — editable vector diagrams, preferably SVG.
- `screenshots/` — cropped screenshots with sensitive data removed.
- `icons/` — icons used in documentation, subject to license terms.
- `templates/` — reusable visual or document templates.

## Naming Convention

Use descriptive, lowercase, hyphen-separated names. Numbering is appropriate only when it indicates sequence, for example `01-network-architecture.png` or `incident-response-flow.svg`.

## Image and Screenshot Guidelines

Prefer SVG for diagrams and compressed PNG or JPEG for raster images. Crop screenshots to relevant evidence, redact hostnames, usernames, IPs, tokens, and personal information, and add surrounding text explaining what the image demonstrates.

## Diagram Guidelines

Use readable labels, consistent arrows, and a legend when needed. Do not encode meaning by color alone. Keep source files when licensing and format allow.

## File Size Recommendations

Prefer assets below 1 MB; optimize larger images and avoid large binary captures, archives, or datasets. Link to large authorized datasets instead of committing them.

## Accessibility

Markdown images need concise alt text that conveys the image's purpose. Avoid text embedded in images where equivalent selectable text can be provided.

## Attribution and Copyright

Use original, properly licensed, or public-domain assets. Record attribution and license terms near the asset or in the referencing document. Do not copy proprietary diagrams or screenshots without permission.
