#!/usr/bin/env python3
"""Build the collection catalogue and full-text search index from Markdown.

Run from any directory with ``python scripts/build-content-index.py``. The
Markdown documents in topical top-level directories are authoritative;
``site/content.json`` and ``site/search-index.json`` are generated artifacts.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import unicodedata
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_OUT = ROOT / "site" / "content.json"
SEARCH_OUT = ROOT / "site" / "search-index.json"
NON_COLLECTIONS = {
    ".git", ".github", "__pycache__", "node_modules",
    "scripts", "site",
}
COLLECTION_NAMES = {
    "MITRE-ATTACK": "MITRE ATT&CK",
    "assets": "Assets & Diagrams",
    "docs": "Project Documentation",
}
DESCRIPTIONS = {
    "API-Security": "API architecture, authentication, authorization, testing and monitoring.",
    "assets": "Repository diagrams, visual assets, and guidance for maintaining them.",
    "Active-Directory": "Directory architecture, administration, security and blue-team practices.",
    "CTF-Writeups": "Challenge writeups that explain evidence, reasoning and defensive lessons.",
    "Cheatsheets": "Compact technical references for security workflows and tools.",
    "Cloud-Security": "Cloud security concepts, controls, architecture and monitoring.",
    "Containers": "Container architecture, security, hardening and runtime concepts.",
    "Cryptography": "Cryptographic foundations, algorithms, protocols and applied security.",
    "Detection-Engineering": "Telemetry, detection logic, validation, tuning and lifecycle practices.",
    "docs": "Authoring, learning-path, responsible-use, deployment, and maintenance guidance.",
    "DevSecOps": "Security integrated into development, CI/CD and software delivery.",
    "Digital-Forensics": "Forensic evidence, artifacts, analysis and investigation workflows.",
    "Email-Security": "Email threats, authentication, phishing analysis and defensive controls.",
    "Endpoint-Security": "Endpoint visibility, hardening, monitoring and protection.",
    "Identity-and-Access-Management": "Identity, authentication, authorization, access control and governance.",
    "Incident-Response": "Incident preparation, triage, containment, recovery and investigation.",
    "Kubernetes": "Kubernetes architecture, operations and cloud-native security.",
    "Labs": "Controlled hands-on security exercises and practical worksheets.",
    "Linux": "Linux administration, security, monitoring and defensive operations.",
    "MITRE-ATTACK": "ATT&CK tactics, techniques, mapping and defensive context.",
    "Malware-Analysis": "Malware analysis workflows, artifacts and defensive investigation.",
    "Network-Security": "Network protection, monitoring, architecture and defensive controls.",
    "Networking": "Networking fundamentals underpinning security operations.",
    "OSINT": "Open-source intelligence collection, analysis and research workflows.",
    "OWASP": "Application-security guidance, vulnerabilities and defensive practices.",
    "Resources": "Courses, tools, standards, research and learning references.",
    "Reverse-Engineering": "Reverse-engineering concepts and technical analysis.",
    "SIEM": "Security monitoring, telemetry, analysis, detection and operations.",
    "SOC": "Security operations, triage, alert handling and analyst workflows.",
    "Security-Architecture": "Security architecture, design principles, controls and planning.",
    "Security-Automation": "Automation patterns for repeatable security operations.",
    "Threat-Hunting": "Hypothesis-driven hunting, telemetry, analysis and investigation.",
    "Threat-Intelligence": "Threat intelligence collection, enrichment, analysis and use.",
    "Vulnerability-Management": "Discovery, assessment, prioritization, remediation and lifecycle management.",
    "Web-Security": "Web application security, vulnerabilities, testing and defensive practices.",
    "Windows": "Windows administration, logging, security and hardening.",
}
ACRONYMS = {
    "acl": "ACL", "api": "API", "att&ck": "ATT&CK", "aws": "AWS",
    "c2": "C2", "ctf": "CTF", "cve": "CVE", "cwe": "CWE",
    "dfir": "DFIR", "dns": "DNS", "edr": "EDR", "gcp": "GCP",
    "graphql": "GraphQL", "grpc": "gRPC", "iam": "IAM", "ip": "IP",
    "jwt": "JWT", "kql": "KQL", "mitre": "MITRE", "nmap": "Nmap",
    "oauth": "OAuth", "oidc": "OIDC", "osint": "OSINT", "owasp": "OWASP",
    "pki": "PKI", "rest": "REST", "siem": "SIEM", "soc": "SOC",
    "sql": "SQL", "ssh": "SSH", "tls": "TLS", "url": "URL",
    "uuid": "UUID", "web": "Web", "xss": "XSS",
}
PLACEHOLDER_TITLES = {
    "contents", "table of contents", "learning objectives", "objectives",
    "purpose", "scope", "overview", "references", "key takeaways", "summary",
    "todo", "tbd", "title", "untitled", "document", "replace with title",
    "your title here",
}
TOKEN_RE = re.compile(r"(?u)\.?[^\W_]+(?:[+#]+|(?:[.&/-][^\W_]+)*)")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
FENCE_CLOSE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})\s*$")
STOP_WORDS = {
    "a", "about", "after", "all", "also", "an", "and", "any", "are", "as",
    "at", "be", "because", "been", "before", "between", "both", "but", "by",
    "can", "could", "did", "do", "does", "each", "for", "from", "had", "has",
    "have", "how", "if", "in", "into", "is", "it", "its", "may", "more",
    "most", "must", "not", "of", "on", "one", "or", "our", "over", "should",
    "such", "than", "that", "the", "their", "them", "then", "there", "these",
    "they", "this", "those", "through", "to", "under", "up", "use", "used",
    "using", "was", "we", "were", "what", "when", "where", "which", "while",
    "who", "will", "with", "you", "your",
}


def _clean_title(value: str) -> str:
    value = html.unescape(value).strip()
    value = re.sub(r"^\s*\d{1,3}\s*[-.)]\s*", "", value)
    value = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]*>", "", value)
    value = re.sub(r"(\*\*|__)(.+?)\1", r"\2", value)
    value = re.sub(r"(?<!\w)(\*|_)(.+?)\1(?!\w)", r"\2", value)
    value = re.sub(r"~~(.+?)~~", r"\1", value)
    value = re.sub(r"`+(.+?)`+", r"\1", value)
    value = re.sub(r"\\([\\`*_{}\[\]()#+.!|>])", r"\1", value)
    return " ".join(value.split()).strip()


def _valid_title(value: str) -> bool:
    cleaned = _clean_title(value)
    return (
        0 < len(cleaned) <= 180
        and bool(re.search(r"[^\W_]", cleaned, re.UNICODE))
        and cleaned.casefold() not in PLACEHOLDER_TITLES
        and not cleaned.casefold().endswith(".md")
        and not cleaned.startswith(("<!--", "<?", "{%"))
    )


def _front_matter_title(text: str) -> str | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() in {"---", "..."}), None)
    if end is None:
        return None
    for line in lines[1:end]:
        match = re.match(r"^\s*title\s*:\s*(.*?)\s*$", line, re.IGNORECASE)
        if not match:
            continue
        value = match.group(1)
        if value.startswith(("'", '"')) and len(value) >= 2 and value[-1] == value[0]:
            quote = value[0]
            value = value[1:-1]
            if quote == "'":
                value = value.replace("''", "'")
            else:
                value = re.sub(r"\\([\\\"'])", r"\1", value)
        elif value.startswith(("[", "{", "|", ">")) or " #" in value:
            return None
        value = _clean_title(value)
        return value if _valid_title(value) else None
    return None


def _outside_fences(lines: list[str]):
    fence_char = ""
    fence_size = 0
    for line in lines:
        if not fence_char:
            marker = FENCE_RE.match(line)
            if marker:
                token = marker.group(1)
                fence_char, fence_size = token[0], len(token)
                continue
        else:
            closer = FENCE_CLOSE_RE.match(line)
            if closer and closer.group(1)[0] == fence_char and len(closer.group(1)) >= fence_size:
                fence_char, fence_size = "", 0
            continue
        if not fence_char:
            yield line


class _H1Text(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_h1 = False
        self.parts: list[str] = []
        self.headings: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "h1" and not self.in_h1:
            self.in_h1 = True
            self.parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "h1":
            if self.in_h1:
                self.headings.append(" ".join(self.parts))
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_h1:
            self.parts.append(data)


def _html_h1(text: str) -> str | None:
    parser = _H1Text()
    try:
        parser.feed(text)
    except Exception:
        return None
    for heading in parser.headings:
        value = _clean_title(heading)
        if _valid_title(value):
            return value
    return None


def humanize_filename(stem: str) -> str:
    stem = re.sub(r"^\s*\d{1,3}\s*[-._ )]+\s*", "", stem)
    words = re.sub(r"[-_]+", " ", stem).split()
    output = []
    for word in words:
        key = word.casefold()
        output.append(ACRONYMS.get(key, word if word.isupper() else word[:1].upper() + word[1:]))
    title = " ".join(output)
    if not title:
        return "Untitled document"
    if not re.search(r"[^\W\d_]", title, re.UNICODE):
        return f"Document {title}"
    return title


def _is_filename_heading(title: str, filename: str) -> bool:
    return (
        title.casefold().endswith(".md")
        and re.sub(r"[^\w]", "", title.casefold())
        == re.sub(r"[^\w]", "", Path(filename).name.casefold())
    )


def extract_title(text: str, filename: str) -> str:
    """Choose a front-matter title, Markdown H1, HTML H1, then filename."""
    title = _front_matter_title(text)
    if title:
        return title
    outside = list(_outside_fences(text.splitlines()))
    for line in outside:
        match = re.match(r"^\s{0,3}#\s+(.+?)(?:\s+#+)?\s*$", line)
        if match:
            title = _clean_title(match.group(1))
            if _valid_title(title) and not _is_filename_heading(title, filename):
                return title
    # An HTML H1 is considered only when no valid Markdown H1 was found.
    title = _html_h1("\n".join(outside))
    return title if title else humanize_filename(Path(filename).stem)


def _plain_text(markdown: str) -> tuple[list[str], str]:
    """Extract searchable headings and readable text without parsing Markdown."""
    headings: list[str] = []
    text_lines: list[str] = []
    in_fence = False
    fence_char = ""
    fence_size = 0
    for line in markdown.splitlines():
        if not in_fence:
            marker = FENCE_RE.match(line)
            if marker:
                token = marker.group(1)
                in_fence, fence_char, fence_size = True, token[0], len(token)
                continue
        else:
            closer = FENCE_CLOSE_RE.match(line)
            if closer and closer.group(1)[0] == fence_char and len(closer.group(1)) >= fence_size:
                in_fence, fence_char, fence_size = False, "", 0
            continue
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", line)
        if heading:
            value = _clean_title(heading.group(1))
            if value:
                headings.append(value)
        # Keep inline code contents useful for technical search.
        cleaned = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", line)
        cleaned = re.sub(r"\[([^\]]+)\]\((?:<[^>]+>|[^)]+)(?:\s+['\"].*?['\"])?\)", r"\1", cleaned)
        cleaned = re.sub(r"<https?://[^>]+>", " ", cleaned)
        cleaned = re.sub(r"<[^>]+>", " ", cleaned)
        cleaned = re.sub(r"(\*\*|__)(.+?)\1", r"\2", cleaned)
        cleaned = re.sub(r"(?<!\w)(\*|_)(.+?)\1(?!\w)", r"\2", cleaned)
        cleaned = re.sub(r"~~(.+?)~~", r"\1", cleaned)
        cleaned = re.sub(r"`+(.+?)`+", r"\1", cleaned)
        cleaned = re.sub(r"^\s{0,3}(?:>\s?|[-+*]\s+|\d+[.)]\s+)", "", cleaned)
        text_lines.append(cleaned)
    plain = " ".join(html.unescape(line) for line in text_lines)
    plain = unicodedata.normalize("NFKC", plain)
    return headings, " ".join(plain.split())


def _search_terms(text: str) -> Counter[str]:
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return Counter(
        match.group(0) for match in TOKEN_RE.finditer(normalized)
        if match.group(0) not in STOP_WORDS and len(match.group(0)) > 1
    )


def _collection_documents() -> tuple[list[dict], list[dict]]:
    categories = []
    all_docs = []
    roots = sorted(
        path for path in ROOT.iterdir()
        if path.is_dir() and not path.name.startswith(".") and path.name not in NON_COLLECTIONS
    )
    for directory in roots:
        files = sorted(directory.rglob("*.md"), key=lambda p: p.relative_to(ROOT).as_posix().casefold())
        if not files:
            continue
        documents = []
        for source in files:
            relative = source.relative_to(ROOT).as_posix()
            text = source.read_text(encoding="utf-8", errors="replace")
            title = extract_title(text, source.name)
            stem = source.stem
            kind = "template" if "template" in stem.casefold() else ("index" if stem.casefold() == "readme" else "document")
            doc = {
                "title": title, "path": relative, "tags": [directory.name], "kind": kind,
            }
            documents.append(doc)
            all_docs.append((doc, text))
        categories.append({
            "name": COLLECTION_NAMES.get(directory.name, humanize_filename(directory.name)),
            "path": directory.name,
            "description": DESCRIPTIONS.get(directory.name, f"Knowledge material covering {humanize_filename(directory.name)}."),
            "icon": "book",
            "documents": documents,
        })
    root_documents = []
    for source in sorted(ROOT.glob("*.md"), key=lambda path: path.name.casefold()):
        relative = source.relative_to(ROOT).as_posix()
        text = source.read_text(encoding="utf-8", errors="replace")
        title = extract_title(text, source.name)
        stem = source.stem
        kind = "template" if "template" in stem.casefold() else ("index" if stem.casefold() == "readme" else "document")
        doc = {"title": title, "path": relative, "tags": ["_root"], "kind": kind}
        root_documents.append(doc)
        all_docs.append((doc, text))
    if root_documents:
        categories.append({
            "name": "Repository Documents",
            "path": "_root",
            "description": "Project overview, policies, contribution guidance, and change history.",
            "icon": "book",
            "documents": root_documents,
        })
    return categories, all_docs





LEARNING_PATHS = [
    ("Cybersecurity Fundamentals", ["Networking", "Linux", "Windows", "Web-Security", "Cryptography"]),
    ("SOC Analyst", ["Networking", "Windows", "SIEM", "Detection-Engineering", "Threat-Hunting", "Incident-Response"]),
    ("Blue Team", ["Windows", "Endpoint-Security", "SIEM", "Detection-Engineering", "Threat-Hunting", "Incident-Response", "Digital-Forensics"]),
    ("Application Security", ["OWASP", "Web-Security", "API-Security", "DevSecOps"]),
    ("Cloud Security", ["Cloud-Security", "Identity-and-Access-Management", "Incident-Response"]),
    ("DFIR", ["Digital-Forensics", "Incident-Response", "Malware-Analysis"]),
]
LEARNING_PATH_STARTS = {"OWASP": "OWASP/README.md"}


def first_chapter(category: dict) -> str:
    selected = LEARNING_PATH_STARTS.get(category["path"])
    if selected and any(doc["path"] == selected for doc in category["documents"]):
        return selected
    docs = category["documents"]
    return next((doc["path"] for doc in docs if doc["kind"] != "index"), docs[0]["path"])


def build_outputs() -> tuple[dict, dict]:
    categories, sources = _collection_documents()
    category_by_path = {category["path"]: category for category in categories}
    search_documents = []
    postings: dict[str, list[list[int]]] = {}
    for doc_id, (doc, markdown) in enumerate(sources):
        headings, body = _plain_text(markdown)
        title_terms = _search_terms(doc["title"])
        heading_terms = _search_terms(" ".join(headings))
        body_terms = _search_terms(body)
        search_documents.append({
            "path": doc["path"],
            "title": doc["title"],
            "collection": doc["tags"][0],
            "headings": headings,
            "snippet": body[:240],
        })
        for token in title_terms.keys() | heading_terms.keys() | body_terms.keys():
            postings.setdefault(token, []).append([
                doc_id,
                min(title_terms[token], 4),
                min(heading_terms[token], 8),
                min(body_terms[token], 12),
            ])
    paths = [
        {"name": name, "documents": [first_chapter(category_by_path[root]) for root in roots if root in category_by_path]}
        for name, roots in LEARNING_PATHS
    ]
    catalogue = {
        "version": 2,
        "generatedFrom": "main",
        "repository": "https://github.com/anurag-rvnkr1/Security-Knowledge-Base",
        "pages": "https://anurag-rvnkr1.github.io/Security-Knowledge-Base/",
        "stats": {"markdownDocuments": len(sources)},
        "categories": categories,
        "learningPaths": paths,
    }
    search_index = {
        "version": 1,
        "catalogueVersion": catalogue["version"],
        "documents": search_documents,
        "terms": {term: postings[term] for term in sorted(postings)},
    }
    return catalogue, search_index


def write_or_check(path: Path, payload: dict, check: bool, compact: bool = False) -> bool:
    rendered = (
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
        if compact else json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    )
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != rendered:
            print(f"Generated output is stale: {path.relative_to(ROOT)}", file=sys.stderr)
            return False
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files differ from source")
    args = parser.parse_args()
    catalogue, search_index = build_outputs()
    ok = write_or_check(CONTENT_OUT, catalogue, args.check)
    ok = write_or_check(SEARCH_OUT, search_index, args.check, compact=True) and ok
    if not args.check:
        print(
            f"Indexed {catalogue['stats']['markdownDocuments']} Markdown documents "
            f"across {len(catalogue['categories'])} collections "
            f"({len(search_index['terms'])} search terms)."
        )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
