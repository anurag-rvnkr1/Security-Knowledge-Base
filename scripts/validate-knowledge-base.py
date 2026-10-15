#!/usr/bin/env python3
"""Validate generated content, repository references, and static-site metadata."""
from __future__ import annotations

from collections import Counter, defaultdict
import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "site" / "content.json"
SEARCH_INDEX = ROOT / "site" / "search-index.json"
REPOSITORY = "https://github.com/anurag-rvnkr1/Security-Knowledge-Base"
PAGES = "https://anurag-rvnkr1.github.io/Security-Knowledge-Base/"
ALLOWED_TYPES = {
    "chapter", "collection-index", "lab", "ctf-writeup", "cheatsheet",
    "template", "reference", "document",
}
EXCLUDED_DIRS = {".git", ".github", ".vscode", "__pycache__", "node_modules", "scripts", "site"}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|(?:\\.|[^\s)])+)")
HEADING_PATTERN = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE_PATTERN = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
)


class Findings:
    def __init__(self) -> None:
        self.items: list[tuple[str, str, str]] = []

    def add(self, severity: str, path: str, message: str) -> None:
        self.items.append((severity, path, message))

    def report(self) -> int:
        totals = Counter(severity for severity, _, _ in self.items)
        by_domain: dict[str, Counter] = defaultdict(Counter)
        by_check: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for severity, path, _ in self.items:
            domain = path.split("/", 1)[0] if "/" in path else "repository"
            by_domain[domain][severity] += 1
        for severity, path, message in self.items:
            if "unresolved local link" in message:
                check = "unresolved local links"
            elif "heading fragment" in message:
                check = "unresolved heading fragments"
            elif "unclosed fenced" in message:
                check = "unclosed code fences"
            elif "H1 headings" in message:
                check = "multiple H1 headings"
            elif "credential/private-key" in message:
                check = "credential signatures"
            else:
                check = "other checks"
            by_check[f"{severity}: {check}"].append((path, message))
        print(
            "Findings: "
            + ", ".join(f"{severity}={totals[severity]}" for severity in ("error", "warning", "info"))
        )
        print("By check:")
        for check in sorted(by_check):
            print(f"  {check}: {len(by_check[check])}")
        if by_domain:
            print("By domain:")
            for domain in sorted(by_domain, key=str.casefold):
                counts = by_domain[domain]
                summary = ", ".join(
                    f"{severity}={counts[severity]}"
                    for severity in ("error", "warning", "info")
                    if counts[severity]
                )
                print(f"  {domain}: {summary}")
        shown = 0
        for check in sorted(by_check):
            for path, message in by_check[check][:5]:
                print(f"{check.upper()}: {path}: {message}")
                shown += 1
        if len(self.items) > shown:
            print(f"... {len(self.items) - shown} additional findings summarized above")
        if totals["error"]:
            print("Validation failed.")
            return 1
        print("Validation passed; warnings are review items, not build failures.")
        return 0


def slugify(text: str) -> str:
    text = text.casefold().replace("_", "-")
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", text).strip("-") or "section"


def markdown_headings(source: str) -> list[str]:
    result: list[str] = []
    fence_char = ""
    fence_length = 0
    for line in source.splitlines():
        fence = FENCE_PATTERN.match(line)
        if fence:
            marker = fence.group(1)
            if not fence_char:
                fence_char, fence_length = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = ""
            continue
        if fence_char:
            continue
        heading = HEADING_PATTERN.match(line)
        if heading:
            text = re.sub(r"(`+|\*{1,3}|_{1,3}|~~)", "", heading.group(2)).strip()
            result.append(text)
    return result


def is_ignored(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS or part.startswith(".") for part in path.parts)


def local_target(source: Path, destination: str) -> tuple[str | None, str | None]:
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return None, None
    if not parsed.path:
        return source.as_posix(), unquote(parsed.fragment) if parsed.fragment else None
    decoded = unquote(parsed.path)
    if decoded.startswith("/"):
        target = posixpath.normpath(decoded.lstrip("/"))
    else:
        target = posixpath.normpath(posixpath.join(source.parent.as_posix(), decoded))
    if target == ".." or target.startswith("../"):
        return target, unquote(parsed.fragment) if parsed.fragment else None
    return target, unquote(parsed.fragment) if parsed.fragment else None


def find_target(target: str, tracked: set[str], directories: set[str]) -> str | None:
    candidates = [target]
    if target in directories or target.endswith("/"):
        normalized = target.rstrip("/")
        candidates.extend(
            f"{normalized}/{name}"
            for name in ("README.md", "Readme.md", "readme.md")
        )
    if not Path(target).suffix:
        candidates.append(target + ".md")
    for candidate in candidates:
        if candidate in tracked:
            return candidate
    return None


def check_link(
    findings: Findings,
    source_path: str,
    destination: str,
    tracked: set[str],
    directories: set[str],
    heading_cache: dict[str, set[str]],
) -> None:
    value = destination.strip().strip("<>")
    if not value or value.startswith(("mailto:", "tel:", "data:", "javascript:", "http:", "https:", "//")):
        return
    source = Path(source_path)
    target, fragment = local_target(source, value)
    if target is None:
        return
    if target == source_path and not urlsplit(value).path:
        resolved = source_path
    else:
        resolved = find_target(target, tracked, directories)
    if resolved is None:
        case_match = next((path for path in tracked if path.casefold() == target.casefold()), None)
        suffix = f"; actual case is {case_match}" if case_match else ""
        findings.add("warning", source_path, f"unresolved local link {value!r}{suffix}")
        return
    if fragment and resolved.casefold().endswith(".md"):
        anchors = heading_cache.setdefault(
            resolved,
            {slugify(heading) for heading in markdown_headings((ROOT / resolved).read_text(encoding="utf-8-sig"))},
        )
        if fragment not in anchors:
            findings.add("warning", source_path, f"heading fragment {fragment!r} not found in {resolved}")


def check_markdown(findings: Findings, tracked: set[str], directories: set[str]) -> None:
    heading_cache: dict[str, set[str]] = {}
    for relative in sorted(path for path in tracked if path.casefold().endswith(".md")):
        source = (ROOT / relative).read_text(encoding="utf-8-sig")
        lines = source.splitlines()
        fence_char = ""
        fence_length = 0
        fence_line = 0
        h1_count = 0
        for line_number, line in enumerate(lines, 1):
            fence = FENCE_PATTERN.match(line)
            if fence:
                marker = fence.group(1)
                if not fence_char:
                    fence_char, fence_length, fence_line = marker[0], len(marker), line_number
                elif marker[0] == fence_char and len(marker) >= fence_length:
                    fence_char = ""
                continue
            if not fence_char:
                if re.match(r"^\s{0,3}#\s+", line):
                    h1_count += 1
                for match in LINK_PATTERN.finditer(line):
                    destination = match.group(1)
                    if destination.startswith("<") and destination.endswith(">"):
                        destination = destination[1:-1]
                    check_link(findings, relative, destination, tracked, directories, heading_cache)
        if fence_char:
            findings.add("warning", relative, f"unclosed fenced code block opened on line {fence_line}")
        if h1_count > 1:
            findings.add("warning", relative, f"contains {h1_count} H1 headings")
        for pattern in SECRET_PATTERNS:
            if pattern.search(source):
                findings.add("error", relative, "contains a high-confidence credential/private-key signature; value suppressed")
                break


def check_root_html(findings: Findings) -> None:
    for relative in ("index.html", "404.html"):
        path = ROOT / relative
        if not path.is_file():
            findings.add("error", relative, "required static page is missing")
            continue
        source = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\b(?:href|src)\s*=\s*['\"]([^'\"]+)['\"]", source, re.I):
            destination = match.group(1)
            if destination.startswith(("#", "http:", "https:", "mailto:", "tel:", "//", "data:")):
                continue
            local_path = unquote(urlsplit(destination).path)
            if not local_path:
                continue
            candidate = (ROOT / local_path).resolve()
            if ROOT not in candidate.parents and candidate != ROOT:
                findings.add("error", relative, f"root reference escapes repository: {destination!r}")
            elif not candidate.exists():
                findings.add("warning", relative, f"referenced local resource does not exist: {destination!r}")
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    if "<title>" not in index or 'name="description"' not in index:
        findings.add("error", "index.html", "title and description metadata are required")
    if f'<link rel="canonical" href="{PAGES}">' not in index:
        findings.add("error", "index.html", "canonical URL does not match the published site")


def check_seo(findings: Findings) -> None:
    robots_path = ROOT / "robots.txt"
    sitemap_path = ROOT / "sitemap.xml"
    if not robots_path.is_file() or f"Sitemap: {PAGES}sitemap.xml" not in robots_path.read_text(encoding="utf-8"):
        findings.add("error", "robots.txt", "expected sitemap declaration is missing")
    if not sitemap_path.is_file():
        findings.add("error", "sitemap.xml", "sitemap is missing")
        return
    try:
        tree = ET.parse(sitemap_path)
    except ET.ParseError as error:
        findings.add("error", "sitemap.xml", f"invalid XML: {error}")
        return
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [node.text or "" for node in tree.findall(".//s:loc", namespace)]
    if not locations or any(not location.startswith(PAGES) for location in locations):
        findings.add("error", "sitemap.xml", "sitemap contains no URLs or a URL outside the published site")
    if any("?" in location for location in locations):
        findings.add("error", "sitemap.xml", "dynamic query-string routes must not be listed as static URLs")


def check_catalogue(findings: Findings, tracked: set[str]) -> None:
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        search = json.loads(SEARCH_INDEX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        findings.add("error", "site/content.json", f"catalogue or search index is unreadable: {error}")
        return
    if catalog.get("version") != 2 or catalog.get("generatedFrom") != "main":
        findings.add("error", "site/content.json", "unexpected catalogue version or source branch")
    if catalog.get("repository") != REPOSITORY or catalog.get("pages") != PAGES:
        findings.add("error", "site/content.json", "repository or published-page URL is incorrect")
    collections = catalog.get("collections")
    if not isinstance(collections, list) or not collections:
        findings.add("error", "site/content.json", "catalogue must contain non-empty collections")
        return
    collection_ids: set[str] = set()
    document_paths: list[str] = []
    for collection in collections:
        identifier = collection.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in collection_ids:
            findings.add("error", "site/content.json", f"invalid or duplicate collection id: {identifier!r}")
            continue
        collection_ids.add(identifier)
        if not collection.get("name") or not collection.get("description"):
            findings.add("error", "site/content.json", f"collection metadata is incomplete: {identifier}")
        documents = collection.get("documents")
        if not isinstance(documents, list) or not documents:
            findings.add("error", "site/content.json", f"collection is empty or invalid: {identifier}")
            continue
        if collection.get("documentCount") != len(documents):
            findings.add("error", "site/content.json", f"document count mismatch: {identifier}")
        for expected_order, document in enumerate(documents):
            path = document.get("path")
            if not isinstance(path, str) or not path or path.startswith("/") or ".." in path.split("/"):
                findings.add("error", "site/content.json", f"invalid document path: {path!r}")
                continue
            document_paths.append(path)
            if path not in tracked or not (ROOT / path).is_file():
                findings.add("error", "site/content.json", f"catalogue path does not exist: {path!r}")
            if document.get("collection") != identifier or document.get("order") != expected_order:
                findings.add("error", "site/content.json", f"invalid collection/order metadata for {path}")
            if document.get("type") not in ALLOWED_TYPES:
                findings.add("error", "site/content.json", f"invalid document type for {path}")
            if not document.get("title") or not isinstance(document.get("excerpt"), str):
                findings.add("error", "site/content.json", f"missing title or excerpt for {path}")
    if len(document_paths) != len(set(document_paths)):
        findings.add("error", "site/content.json", "duplicate document paths found")
    stats = catalog.get("stats", {})
    if stats.get("markdownDocuments") != len(document_paths) or stats.get("collections") != len(collections):
        findings.add("error", "site/content.json", "catalogue statistics do not match discovered documents")

    if search.get("version") != 1 or search.get("generatedFrom") != "main":
        findings.add("error", "site/search-index.json", "unexpected search-index version or source branch")
    if search.get("documentPaths") != document_paths:
        findings.add("error", "site/search-index.json", "search-index document order differs from the catalogue")
    terms = search.get("terms")
    if not isinstance(terms, dict):
        findings.add("error", "site/search-index.json", "terms must be a dictionary")
    else:
        for term, postings in terms.items():
            previous = -1
            if not isinstance(postings, list):
                findings.add("error", "site/search-index.json", f"invalid postings for term {term!r}")
                break
            for posting in postings:
                if (
                    not isinstance(posting, list) or len(posting) != 2
                    or not isinstance(posting[0], int) or not 0 <= posting[0] < len(document_paths)
                    or not isinstance(posting[1], int) or posting[1] < 1
                    or posting[0] <= previous
                ):
                    findings.add("error", "site/search-index.json", f"invalid posting for term {term!r}")
                    break
                previous = posting[0]
    assets = catalog.get("assets")
    if not isinstance(assets, list) or len(assets) != len(set(assets)):
        findings.add("error", "site/content.json", "asset list is invalid or contains duplicates")
    else:
        for path in assets:
            if path not in tracked and not (ROOT / path).is_file():
                findings.add("error", "site/content.json", f"catalogue asset does not exist: {path!r}")


def check_reproducible(findings: Findings) -> None:
    result = subprocess.run(
        [sys.executable, "scripts/build-content-index.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        detail = (result.stdout + result.stderr).strip().splitlines()
        findings.add("error", "site/content.json", detail[-1] if detail else "generated files are not reproducible")
    else:
        print(result.stdout.strip())


def main() -> int:
    findings = Findings()
    tracked = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and not is_ignored(path.relative_to(ROOT))
    }
    directories = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_dir() and not is_ignored(path.relative_to(ROOT))
    }
    check_catalogue(findings, tracked)
    check_root_html(findings)
    check_seo(findings)
    check_markdown(findings, tracked, directories)
    check_reproducible(findings)
    return findings.report()


if __name__ == "__main__":
    raise SystemExit(main())
