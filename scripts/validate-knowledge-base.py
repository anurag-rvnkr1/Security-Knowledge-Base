#!/usr/bin/env python3
"""Validate source links, headings, assets, and generated handbook indexes.

The checker intentionally supports the repository's common Markdown link
forms rather than claiming complete CommonMark parsing. Ambiguous syntax is
reported as a warning; definite missing local resources fail validation.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import importlib.util

SPEC = importlib.util.spec_from_file_location("build_content_index", ROOT / "scripts" / "build-content-index.py")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)

INLINE_LINK_RE = re.compile(
    r"(?<!!)\[([^\]]*)\]\(\s*(<[^>]+>|(?:\\.|[^()\s]|\([^()]*\))+)",
)
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(\s*(<[^>]+>|(?:\\.|[^()\s]|\([^()]*\))+)") 
REFERENCE_DEF_RE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
REFERENCE_USE_RE = re.compile(r"(?<!!)\[([^\]]+)\](?:\[([^\]]*)\])?")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
FENCE_CLOSE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})\s*$")
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)(?:\s+#+)?\s*$")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
)


class ResourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.images_without_alt = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for attr in ("id", "name"):
            if values.get(attr):
                self.ids.add(values[attr])
        for attr in ("href", "src"):
            if values.get(attr):
                self.targets.append((values[attr], tag))
        if tag.lower() == "img" and not (values.get("alt") or "").strip():
            self.images_without_alt = True


def visible_lines(text: str):
    """Yield (line number, text, in-code-fence) for conservative Markdown scans."""
    fence_char = ""
    fence_size = 0
    for number, line in enumerate(text.splitlines(), 1):
        if not fence_char:
            marker = FENCE_RE.match(line)
            if marker:
                token = marker.group(1)
                fence_char, fence_size = token[0], len(token)
                yield number, line, True
                continue
            yield number, line, False
        else:
            closer = FENCE_CLOSE_RE.match(line)
            if closer and closer.group(1)[0] == fence_char and len(closer.group(1)) >= fence_size:
                fence_char, fence_size = "", 0
            yield number, line, True


def unclosed_fence_line(text: str) -> int | None:
    fence_char = ""
    fence_size = 0
    opening_line = None
    for number, line in enumerate(text.splitlines(), 1):
        if not fence_char:
            marker = FENCE_RE.match(line)
            if marker:
                token = marker.group(1)
                fence_char, fence_size, opening_line = token[0], len(token), number
        else:
            closer = FENCE_CLOSE_RE.match(line)
            if closer and closer.group(1)[0] == fence_char and len(closer.group(1)) >= fence_size:
                fence_char, fence_size, opening_line = "", 0, None
    return opening_line


def heading_anchors(text: str) -> tuple[set[str], list[str], list[str]]:
    anchors: set[str] = set()
    headings: list[str] = []
    warnings: list[str] = []
    used_ids: set[str] = set()
    base_counts: Counter[str] = Counter()
    lines = list(visible_lines(text))
    for number, line, in_code in lines:
        if in_code:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        title = html.unescape(re.sub(r"`([^`]*)`", r"\1", match.group(2)))
        title = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", title)
        base = github_slug(title)
        headings.append(title)
        if not base:
            base = "section"
        suffix = base_counts[base]
        candidate = base if suffix == 0 else f"{base}-{suffix}"
        if suffix or candidate in used_ids:
            warnings.append(f"duplicate heading ID at line {number}: {title}")
        while candidate in used_ids:
            suffix += 1
            candidate = f"{base}-{suffix}"
            if candidate in used_ids:
                warnings.append(f"generated heading ID collision at line {number}: {candidate}")
        base_counts[base] = suffix + 1
        used_ids.add(candidate)
        anchors.add(candidate)
    parser = ResourceParser()
    try:
        parser.feed("\n".join(line for _, line, in_code in lines if not in_code))
        collisions = used_ids.intersection(parser.ids)
        for anchor in collisions:
            warnings.append(f"HTML anchor ID collides with generated heading ID: {anchor}")
        anchors.update(parser.ids)
    except Exception:
        pass
    for number, line, in_code in lines:
        if not in_code and re.match(r"^\s{0,3}#{1,6}(?:\s*)$", line):
            warnings.append(f"empty heading at line {number}")
    return anchors, headings, warnings


def github_slug(heading: str) -> str:
    heading = unicodedata.normalize("NFKC", heading).casefold()
    heading = re.sub(r"<[^>]*>", "", heading)
    heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"`([^`]*)`", r"\1", heading)
    heading = re.sub(r"[^\w\-\s]", "", heading, flags=re.UNICODE)
    return re.sub(r"\s+", "-", heading.strip())


def _strip_angle(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target.replace("\\(", "(").replace("\\)", ")")


def markdown_targets(text: str) -> list[tuple[str, str, int]]:
    lines = list(visible_lines(text))
    clean_lines = [
        (number, re.sub(r"`+[^`]*`+", "", line))
        for number, line, in_code in lines if not in_code
    ]
    source = "\n".join(line for _, line in clean_lines)
    targets: list[tuple[str, str, int]] = []
    definitions = {
        label.strip().casefold(): _strip_angle(target)
        for label, target in REFERENCE_DEF_RE.findall(source)
    }
    for number, line in clean_lines:
        for match in IMAGE_RE.finditer(line):
            targets.append((_strip_angle(match.group(2)), "image", number))
            if not match.group(1).strip():
                targets.append(("", "image_alt", number))
        for match in INLINE_LINK_RE.finditer(line):
            targets.append((_strip_angle(match.group(2)), "link", number))
        # Reference definitions are checked as destinations; uses are checked
        # for missing labels because unresolved references can mislead readers.
        if re.match(r"^\s*(?:[-+*]|\d+[.)])\s+\[[ xX]\](?:\s|$)", line):
            continue
        reference_line = re.sub(r"`[^`]*`", "", line)
        for match in REFERENCE_USE_RE.finditer(reference_line):
            raw_label = (match.group(2) if match.group(2) is not None else match.group(1)).strip()
            label = raw_label.casefold()
            suffix = reference_line[match.end():match.end() + 1]
            explicit = match.group(2) is not None
            if suffix == "(":
                continue
            if explicit or label in definitions:
                if label not in definitions:
                    targets.append((f"__missing_reference__:{label}", "reference", number))
    for match in REFERENCE_DEF_RE.finditer(source):
        line_number = source.count("\n", 0, match.start()) + 1
        targets.append((_strip_angle(match.group(2)), "reference", line_number))
    for line_number, line in clean_lines:
        line_parser = ResourceParser()
        try:
            line_parser.feed(line)
        except Exception:
            continue
        for target, tag in line_parser.targets:
            targets.append((target, "image" if tag == "img" else "html", line_number))
        if line_parser.images_without_alt:
            targets.append(("", "image_alt", line_number))
    return targets


def _target_file(source: Path, target_path: str) -> Path | None:
    decoded = unquote(target_path)
    if not decoded:
        return source
    if decoded.startswith("/"):
        candidate = ROOT / decoded.lstrip("/")
    else:
        candidate = source.parent / decoded
    try:
        resolved = candidate.resolve()
        resolved.relative_to(ROOT.resolve())
    except (OSError, ValueError):
        return None
    if resolved.is_dir():
        return resolved
    return resolved


def check_link(source: Path, target: str, line: int, anchors_cache: dict[Path, set[str]]) -> str | None:
    if target.startswith("__missing_reference__:"):
        return f"unresolved Markdown reference label {target.split(':', 1)[1]!r}"
    if not target or target.startswith("#"):
        destination = source
        fragment = unquote(target[1:]) if target.startswith("#") else ""
        query = ""
    else:
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            return None
        destination = _target_file(source, parts.path)
        fragment, query = unquote(parts.fragment), parts.query
        if destination is None:
            return "link resolves outside the repository"
    if not destination.exists():
        return f"missing local target {target!r}"
    if fragment and destination.is_file() and destination.suffix.casefold() in {".md", ".markdown"}:
        if destination not in anchors_cache:
            anchors_cache[destination] = heading_anchors(destination.read_text(encoding="utf-8", errors="replace"))[0]
        if fragment not in anchors_cache[destination]:
            return f"unresolved heading fragment #{fragment}"
    elif fragment and destination.is_file() and destination.suffix.casefold() in {".html", ".htm"}:
        parser = ResourceParser()
        parser.feed(destination.read_text(encoding="utf-8", errors="replace"))
        if fragment not in parser.ids:
            return f"unresolved HTML fragment #{fragment}"
    return None


def source_files(categories: list[dict]) -> list[Path]:
    return sorted(
        (ROOT / relative for relative in [
            doc["path"] for category in categories
            for doc in category["documents"]
        ]),
        key=lambda path: path.as_posix().casefold(),
    )


def all_markdown_files() -> list[Path]:
    ignored = {".git", ".github", "__pycache__", "node_modules", "scripts", "site"}
    return sorted(
        (
            path for path in ROOT.rglob("*")
            if path.is_file() and path.suffix.casefold() in {".md", ".markdown"}
            and not any(part in ignored for part in path.relative_to(ROOT).parts)
        ),
        key=lambda path: path.relative_to(ROOT).as_posix().casefold(),
    )


def validate() -> tuple[list[str], list[str], dict[str, object]]:
    errors: set[str] = set()
    warnings: set[str] = set()
    anchors_cache: dict[Path, set[str]] = {}
    catalogue, search_index = builder.build_outputs()
    source_docs = source_files(catalogue["categories"])
    markdown_docs = all_markdown_files()
    catalog_path = ROOT / "site" / "content.json"
    search_path = ROOT / "site" / "search-index.json"

    duplicate_heading_paths: set[str] = set()
    duplicate_heading_count = 0
    broken_local_links = 0
    broken_image_refs = 0
    for path in markdown_docs:
        text = path.read_text(encoding="utf-8", errors="replace")
        anchors, headings, heading_warnings = heading_anchors(text)
        anchors_cache[path] = anchors
        if not headings:
            if text.strip():
                warnings.add(f"{path.relative_to(ROOT)}: missing H1/Markdown title heading")
            else:
                warnings.add(f"{path.relative_to(ROOT)}: empty Markdown file; title uses the filename fallback")
        for message in heading_warnings:
            if message.startswith(("duplicate heading", "generated heading ID collision")):
                duplicate_heading_paths.add(path.relative_to(ROOT).as_posix())
                duplicate_heading_count += 1
            else:
                warnings.add(f"{path.relative_to(ROOT)}: {message}")
        unclosed_line = unclosed_fence_line(text)
        if unclosed_line:
            errors.add(f"{path.relative_to(ROOT)}:{unclosed_line}: unclosed code fence")
        for target, kind, number in markdown_targets(text):
            if kind == "image_alt":
                warnings.add(f"{path.relative_to(ROOT)}:{number}: image is missing alternative text")
                continue
            message = check_link(path, target, number, anchors_cache)
            if message:
                if "missing local target" in message or "unresolved heading fragment" in message or "unresolved HTML fragment" in message:
                    broken_local_links += 1
                if kind == "image" and "missing local target" in message:
                    broken_image_refs += 1
                finding = f"{path.relative_to(ROOT)}:{number}: {message}"
                if kind == "image" and message.startswith("missing local target"):
                    errors.add(finding)
                else:
                    errors.add(finding)

    expected_paths = [doc["path"] for category in catalogue["categories"] for doc in category["documents"]]
    search_paths = [doc["path"] for doc in search_index["documents"]]
    malformed_titles = 0
    invalid_paths = 0
    document_kinds: Counter[str] = Counter()
    for category in catalogue["categories"]:
        for doc in category["documents"]:
            if not builder._valid_title(doc["title"]):
                malformed_titles += 1
            path = Path(doc["path"])
            if path.is_absolute() or ".." in path.parts or not (ROOT / path).is_file():
                invalid_paths += 1
                errors.add(f"catalogue: invalid source path {doc['path']!r}")
            document_kinds[doc["kind"]] += 1
    if len(expected_paths) != len(set(expected_paths)):
        errors.add("catalogue: duplicate document paths")
    if expected_paths != search_paths:
        errors.add("search index: document ordering or coverage differs from catalogue")
    if malformed_titles:
        errors.add("catalogue: one or more titles are blank or malformed")
    for path, payload in ((catalog_path, catalogue), (search_path, search_index)):
        if not path.exists():
            errors.add(f"{path.relative_to(ROOT)}: generated output is missing")
            continue
        try:
            actual = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            errors.add(f"{path.relative_to(ROOT)}: invalid JSON")
            continue
        if actual != payload:
            errors.add(f"{path.relative_to(ROOT)}: generated output differs from Markdown sources; run the content-index builder")

    sitemap_locs = set()
    try:
        sitemap_tree = ET.parse(ROOT / "sitemap.xml")
        sitemap_locs = {
            element.text.strip()
            for element in sitemap_tree.iter()
            if element.tag.endswith("}loc") and element.text and element.text.strip()
        }
    except (OSError, ET.ParseError):
        errors.add("sitemap.xml: missing or invalid XML")
    robots = (ROOT / "robots.txt")
    if not robots.exists() or "Sitemap:" not in robots.read_text(encoding="utf-8", errors="replace"):
        warnings.add("robots.txt: sitemap directive is missing")

    required = (
        "assets/css/style.css", "assets/css/reader.css", "assets/js/app.js",
        "site/content.json", "site/search-index.json", "favicon.svg",
    )
    for resource in required:
        if not (ROOT / resource).is_file():
            errors.add(f"homepage resource is missing: {resource}")
    index_html = (ROOT / "index.html").read_text(encoding="utf-8", errors="replace")
    if 'rel="canonical"' not in index_html:
        warnings.add("index.html: canonical URL is missing")
    home_parser = ResourceParser()
    home_parser.feed(index_html)
    catalogued_paths = set(expected_paths)
    for target, _tag in home_parser.targets:
        message = check_link(ROOT / "index.html", target, 1, anchors_cache)
        if message:
            errors.add(f"index.html: {message}")
        route = urlsplit(target)
        routed_doc = dict(pair.split("=", 1) for pair in route.query.split("&") if "=" in pair).get("doc")
        if route.path.endswith("index.html") and routed_doc:
            routed_doc = unquote(routed_doc.replace("+", " "))
            if routed_doc not in catalogued_paths:
                errors.add(f"index.html: document route points to an uncatalogued Markdown path {routed_doc!r}")
    not_found_html = ROOT / "404.html"
    not_found_parser = ResourceParser()
    not_found_parser.feed(not_found_html.read_text(encoding="utf-8", errors="replace"))
    for target, _tag in not_found_parser.targets:
        message = check_link(not_found_html, target, 1, anchors_cache)
        if message:
            errors.add(f"404.html: {message}")
    canonical = re.search(r'<link\b[^>]*\brel="canonical"[^>]*\bhref="([^"]+)"', index_html, re.IGNORECASE)
    if canonical and canonical.group(1) not in sitemap_locs:
        warnings.add("sitemap.xml: canonical homepage URL is not listed in the sitemap")
    for path in [*markdown_docs, *(ROOT / item for item in ("index.html", "404.html", "README.md", "Contributing.md", "SECURITY.md"))]:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for pattern in SECRET_PATTERNS:
            for match in pattern.finditer(content):
                line = content.count("\n", 0, match.start()) + 1
                errors.add(f"{path.relative_to(ROOT)}:{line}: secret-like credential pattern detected; value suppressed")
    stats = {
        "collections": len(catalogue["categories"]),
        "documents": len(source_docs),
        "repository_markdown": len(markdown_docs),
        "missing_h1": sum(
            bool(path.read_text(encoding="utf-8", errors="replace").strip())
            and not heading_anchors(path.read_text(encoding="utf-8", errors="replace"))[1]
            for path in markdown_docs
        ),
        "duplicate_heading_docs": len(duplicate_heading_paths),
        "duplicate_heading_count": duplicate_heading_count,
        "broken_local_links": broken_local_links,
        "broken_image_refs": broken_image_refs,
        "malformed_titles": malformed_titles,
        "invalid_paths": invalid_paths,
        "document_kinds": document_kinds,
    }
    return sorted(errors), sorted(warnings), stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    errors, warnings, stats = validate()
    print(
        f"Checked {stats['documents']} collection documents in {stats['collections']} collections and "
        f"{stats['repository_markdown']} Markdown files total "
        f"(kinds: {dict(stats['document_kinds'])}); {stats['malformed_titles']} malformed titles, "
        f"{stats['invalid_paths']} invalid paths, {stats['missing_h1']} missing H1 titles; "
        f"{stats['duplicate_heading_count']} repeated heading IDs in {stats['duplicate_heading_docs']} documents; "
        f"{stats['broken_local_links']} broken local links/fragments and {stats['broken_image_refs']} broken image references."
    )
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Validation: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
