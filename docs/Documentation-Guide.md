# Documentation Guide

Write content that is technically accurate, useful to its intended reader, and consistent with nearby chapters. Search for existing material and link to it before introducing duplicate explanations.

## Structure and Headings

Use one descriptive H1 title, then H2 sections and H3 subsections in logical order. Keep the outline scannable; avoid heading levels used only for visual sizing.

## Names and Examples

Follow [Naming Conventions](./Naming-Conventions.md). Explain commands and queries, identify assumptions, and distinguish illustrative examples from production-ready configurations.

## Code, Tables, and Links

Use fenced code blocks with language identifiers where useful. Use tables for concise comparisons, not long prose. Prefer relative links for repository content and authoritative URLs for external references; verify destinations.

The repository validator checks common inline links, reference-style link
definitions, raw HTML `href`/`src` attributes, local images, and GitHub-style
heading fragments. It is a conservative repository checker, not a complete
CommonMark implementation; manually review deeply nested brackets, unusual
parenthesized destinations, and raw HTML whose meaning depends on browser
context.

## Images

Add only images that improve understanding. Use descriptive filenames and alt text, provide attribution, redact sensitive details, and see the [asset guidelines](../assets/README.md).

## References and Accuracy

Cite primary vendor, standards-body, or project documentation. Record relevant versions and dates when behavior changes over time. Do not fabricate commands, identifiers, detection claims, or capabilities.

## Cross-Linking

Connect related foundational, operational, and defensive material with relative links. Avoid link loops and links to non-existent files.

## Safety and Versioning

State authorization assumptions for security testing, protect secrets and personal information, and include cleanup for labs. Explain breaking or version-dependent changes; summarize material repository changes in the established change history when appropriate.

Before submitting, run the unit tests, regenerate/check the catalogue and
search index, run the repository validator, and syntax-check the site script.
See the [deployment and local preview guide](./DEPLOYMENT.md).
