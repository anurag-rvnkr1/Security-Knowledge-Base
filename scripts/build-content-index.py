#!/usr/bin/env python3
"""Build the static catalogue and compact full-text index for GitHub Pages."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "site" / "content.json"
SEARCH_PATH = ROOT / "site" / "search-index.json"
REPOSITORY = "https://github.com/anurag-rvnkr1/Security-Knowledge-Base"
PAGES = "https://anurag-rvnkr1.github.io/Security-Knowledge-Base/"
DEFAULT_BRANCH = "main"
SKIP_DIRS = {".git", ".github", ".vscode", "__pycache__", "node_modules", "scripts", "site", "assets"}
IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
DOCUMENT_TYPES = {
    "chapter",
    "collection-index",
    "lab",
    "ctf-writeup",
    "cheatsheet",
    "template",
    "reference",
    "document",
}
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into",
    "is", "it", "of", "on", "or", "that", "the", "this", "to", "was", "with",
}

COLLECTION_METADATA = {
    "API-Security": ("API Security", "API architecture, authentication, authorization, testing, and monitoring."),
    "Active-Directory": ("Active Directory", "Directory architecture, administration, identity security, and defensive operations."),
    "CTF-Writeups": ("CTF Writeups", "Challenge reasoning, evidence, and defensive lessons from authorized environments."),
    "Cheatsheets": ("Cheatsheets", "Concise command and query references with context and operational caveats."),
    "Cloud-Security": ("Cloud Security", "Cloud identity, architecture, controls, monitoring, and incident response."),
    "Containers": ("Containers", "Container architecture, image and runtime security, and hardening."),
    "Cryptography": ("Cryptography", "Cryptographic foundations, protocols, and secure application."),
    "Detection-Engineering": ("Detection Engineering", "Telemetry, detection logic, validation, tuning, and lifecycle practices."),
    "DevSecOps": ("DevSecOps", "Security integrated into software development and delivery."),
    "Digital-Forensics": ("Digital Forensics", "Evidence handling, artifacts, analysis, and investigation workflows."),
    "Email-Security": ("Email Security", "Email authentication, phishing analysis, and defensive controls."),
    "Endpoint-Security": ("Endpoint Security", "Endpoint visibility, hardening, monitoring, and protection."),
    "Identity-and-Access-Management": ("Identity and Access Management", "Identity, authentication, authorization, and access governance."),
    "Incident-Response": ("Incident Response", "Preparation, triage, containment, recovery, and investigation."),
    "Kubernetes": ("Kubernetes", "Kubernetes architecture, operations, and cloud-native security."),
    "Labs": ("Labs", "Controlled exercises for security learning, investigation, and defense."),
    "Linux": ("Linux", "Linux administration, security, monitoring, and defensive operations."),
    "MITRE-ATTACK": ("MITRE ATT&CK", "ATT&CK tactics, techniques, mapping, and defensive context."),
    "Malware-Analysis": ("Malware Analysis", "Safe malware analysis workflows, artifacts, and defensive investigation."),
    "Network-Security": ("Network Security", "Network protection, monitoring, architecture, and defensive controls."),
    "Networking": ("Networking", "Networking foundations for security engineering and operations."),
    "OSINT": ("OSINT", "Open-source intelligence collection, analysis, and source validation."),
    "OWASP": ("OWASP", "Application-security guidance, testing, vulnerabilities, and defensive practices."),
    "Resources": ("Resources", "Curated courses, tools, standards, research, and learning references."),
    "Reverse-Engineering": ("Reverse Engineering", "Authorized reverse-engineering concepts and technical analysis."),
    "SIEM": ("SIEM", "Security monitoring, telemetry, investigation, and security operations."),
    "SOC": ("SOC", "Security operations, triage, alert handling, and analyst workflows."),
    "Security-Architecture": ("Security Architecture", "Security design principles, controls, architecture, and planning."),
    "Security-Automation": ("Security Automation", "Automation patterns for repeatable security operations."),
    "Threat-Hunting": ("Threat Hunting", "Hypothesis-driven hunting, telemetry, analysis, and investigation."),
    "Threat-Intelligence": ("Threat Intelligence", "Threat intelligence collection, enrichment, analysis, and use."),
    "Vulnerability-Management": ("Vulnerability Management", "Discovery, assessment, prioritization, remediation, and lifecycle management."),
    "Web-Security": ("Web Security", "Web application security, testing, vulnerabilities, and defensive practices."),
    "Windows": ("Windows", "Windows administration, logging, security, and hardening."),
    "docs": ("Project Guides", "Project documentation, contribution guidance, and responsible-use policies."),
}

LEARNING_PATHS = (
    {
        "id": "security-foundations",
        "title": "Security foundations",
        "description": "Build protocol, operating-system, and application-security context.",
        "collections": ("Networking", "Linux", "Windows", "Web-Security", "Cryptography"),
    },
    {
        "id": "defensive-operations",
        "title": "Defensive operations",
        "description": "Connect host visibility to monitoring, detection, hunting, and response.",
        "collections": ("Windows", "SIEM", "Detection-Engineering", "Threat-Hunting", "Incident-Response"),
    },
    {
        "id": "application-security",
        "title": "Application security",
        "description": "Progress from application-security foundations to APIs and secure delivery.",
        "collections": ("OWASP", "Web-Security", "API-Security", "DevSecOps"),
    },
    {
        "id": "cloud-defense",
        "title": "Cloud defense",
        "description": "Study cloud controls alongside identity, telemetry, and response.",
        "collections": ("Cloud-Security", "Identity-and-Access-Management", "Kubernetes", "Incident-Response"),
    },
    {
        "id": "dfir",
        "title": "Digital forensics and response",
        "description": "Develop evidence, investigation, and response context.",
        "collections": ("Windows", "Digital-Forensics", "Malware-Analysis", "Incident-Response"),
    },
)

RELATED_COLLECTIONS = {
    "API-Security": ("Web-Security", "OWASP", "DevSecOps"),
    "Active-Directory": ("Windows", "Identity-and-Access-Management", "Detection-Engineering"),
    "Cloud-Security": ("Identity-and-Access-Management", "Containers", "Kubernetes", "Incident-Response"),
    "Detection-Engineering": ("SIEM", "Threat-Hunting", "Incident-Response"),
    "Digital-Forensics": ("Incident-Response", "Windows", "Malware-Analysis"),
    "Kubernetes": ("Containers", "Cloud-Security", "Security-Architecture"),
    "Web-Security": ("OWASP", "API-Security", "DevSecOps"),
}
PREREQUISITES = {
    "API-Security": ["HTTP and basic authentication and authorization concepts"],
    "Cloud-Security": ["Cloud service and identity fundamentals"],
    "Detection-Engineering": ["Familiarity with the relevant telemetry and query language"],
    "Kubernetes": ["Container and Linux fundamentals"],
    "Threat-Hunting": ["Access to relevant endpoint, identity, or network telemetry"],
    "Web-Security": ["HTTP, browser, and basic web-application concepts"],
}


def humanize(value: str) -> str:
    text = re.sub(r"[-_]+", " ", value)
    text = re.sub(r"^\d+\s*", "", text).strip()
    result = " ".join(part[:1].upper() + part[1:] for part in text.split())
    for pattern, replacement in (
        (r"\bApi\b", "API"), (r"\bMitre\b", "MITRE"), (r"\bOwasp\b", "OWASP"),
        (r"\bOsint\b", "OSINT"), (r"\bSiem\b", "SIEM"), (r"\bSoc\b", "SOC"),
        (r"\bIam\b", "IAM"), (r"\bCtf\b", "CTF"), (r"\bDfIr\b", "DFIR"),
    ):
        result = re.sub(pattern, replacement, result)
    return result


def plain_text(markdown: str) -> str:
    text = re.sub(r"```[^\n]*\n.*?```|~~~[^\n]*\n.*?~~~", " ", markdown, flags=re.S)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"(`+|\*{1,3}|_{1,3}|~~)", "", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"^\s{0,3}(?:[-*+]|\d+[.)])\s+", "", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def slugify(text: str) -> str:
    text = text.casefold().replace("_", "-")
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text or "section"


def markdown_metadata(path: Path, relative: str, collection_name: str) -> tuple[str, list[dict], str, str]:
    source = path.read_text(encoding="utf-8-sig")
    headings: list[dict] = []
    used_ids: Counter[str] = Counter()
    in_fence = False
    fence_char = ""
    fence_length = 0
    for line in source.splitlines():
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence, fence_char, fence_length = True, marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                in_fence = False
            continue
        if in_fence:
            continue
        heading = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        title = plain_text(heading.group(2)).strip()
        if not title:
            continue
        base = slugify(title)
        number = used_ids[base]
        used_ids[base] += 1
        headings.append({"text": title, "id": base if number == 0 else f"{base}-{number}", "level": len(heading.group(1))})

    stem = Path(relative).stem
    is_readme = stem.casefold() == "readme"
    title = collection_name if is_readme else next(
        (heading["text"] for heading in headings if heading["level"] == 1),
        humanize(stem),
    )
    paragraph = ""
    in_fence = False
    for line in source.splitlines():
        if re.match(r"^\s{0,3}(`{3,}|~{3,})", line):
            in_fence = not in_fence
            continue
        if in_fence or not line.strip() or re.match(r"^\s{0,3}#{1,6}\s", line):
            continue
        candidate = plain_text(line)
        if candidate and len(candidate) > 30:
            paragraph = candidate
            break
    excerpt = paragraph[:277].rstrip()
    if len(paragraph) > 280:
        excerpt += "…"
    if "template" in stem.casefold():
        kind = "template"
    elif relative.startswith("CTF-Writeups/"):
        kind = "ctf-writeup" if not is_readme else "collection-index"
    elif relative.split("/", 1)[0] == "Labs" and not is_readme:
        kind = "lab"
    elif "cheatsheet" in stem.casefold() or relative.split("/", 1)[0] == "Cheatsheets" and not is_readme:
        kind = "cheatsheet"
    elif is_readme:
        kind = "collection-index"
    elif relative.split("/", 1)[0] == "Resources" or re.search(r"resource|reference|glossary", stem, re.I):
        kind = "reference"
    elif re.match(r"^\d+", stem):
        kind = "chapter"
    else:
        kind = "document"
    if kind not in DOCUMENT_TYPES:
        raise ValueError(f"Invalid document type {kind!r} for {relative}")
    return title, headings, excerpt, kind


def collection_for(relative: str) -> str | None:
    parts = relative.split("/")
    if len(parts) < 2:
        return None
    root = parts[0]
    if root in SKIP_DIRS:
        return None
    if root == "CTF-Writeups" and len(parts) > 2:
        return "/".join(parts[:2])
    return root


def order_key(document: dict) -> tuple:
    name = Path(document["path"]).name.casefold()
    if document["type"] == "collection-index":
        return (0, 0, name)
    match = re.match(r"^(\d+)", name)
    if match:
        return (1, int(match.group(1)), name)
    return (2, 0, name)


def collection_metadata(identifier: str) -> tuple[str, str]:
    if identifier in COLLECTION_METADATA:
        return COLLECTION_METADATA[identifier]
    if identifier.startswith("CTF-Writeups/"):
        name = humanize(identifier.split("/", 1)[1])
        return name, f"Authorized CTF writeups and learning material for {name} challenges."
    name = humanize(identifier.rsplit("/", 1)[-1])
    return name, f"Technical learning and reference material for {name}."


def build_payloads() -> tuple[dict, dict]:
    files = sorted(
        (path for path in ROOT.rglob("*") if path.is_file() and path.suffix.casefold() == ".md"),
        key=lambda path: path.relative_to(ROOT).as_posix().casefold(),
    )
    grouped: dict[str, list[dict]] = defaultdict(list)
    assets: list[str] = []
    markdown_paths: set[str] = set()
    for file_path in files:
        relative = file_path.relative_to(ROOT).as_posix()
        parts = relative.split("/")
        if any(part in SKIP_DIRS or part.startswith(".") for part in parts):
            continue
        collection_id = collection_for(relative)
        if not collection_id:
            continue
        if relative in markdown_paths:
            raise ValueError(f"Duplicate Markdown path discovered: {relative}")
        markdown_paths.add(relative)
        display_name, description = collection_metadata(collection_id)
        title, headings, excerpt, kind = markdown_metadata(file_path, relative, display_name)
        grouped[collection_id].append({
            "title": title,
            "path": relative,
            "type": kind,
            "headings": headings,
            "excerpt": excerpt,
            "tags": [collection_id.replace("/", " "), kind],
        })

    for file_path in ROOT.rglob("*"):
        if not file_path.is_file() or file_path.suffix.casefold() not in IMAGE_SUFFIXES:
            continue
        relative = file_path.relative_to(ROOT).as_posix()
        if any(part in {".git", "node_modules", "site", "__pycache__"} for part in relative.split("/")):
            continue
        assets.append(relative)
    assets.sort(key=str.casefold)

    if not grouped:
        raise ValueError("No Markdown collections were discovered.")
    collections: list[dict] = []
    flattened: list[dict] = []
    for identifier in sorted(grouped, key=str.casefold):
        display_name, description = collection_metadata(identifier)
        documents = sorted(grouped[identifier], key=order_key)
        if not documents:
            raise ValueError(f"Collection has no documents: {identifier}")
        for order, document in enumerate(documents):
            document["order"] = order
            document["collection"] = identifier
            flattened.append(document)
        related = [item for item in RELATED_COLLECTIONS.get(identifier, ()) if item in grouped]
        collections.append({
            "id": identifier,
            "name": display_name,
            "path": identifier,
            "description": description,
            "prerequisites": PREREQUISITES.get(identifier, []),
            "related": related,
            "documentCount": len(documents),
            "documents": documents,
        })

    by_id = {item["id"]: item for item in collections}
    learning_paths = []
    for path in LEARNING_PATHS:
        steps = []
        for collection_id in path["collections"]:
            collection = by_id.get(collection_id)
            if collection is None:
                continue
            target = next(
                (document for document in collection["documents"] if document["type"] not in {"collection-index", "template"}),
                collection["documents"][0],
            )
            steps.append({
                "collection": collection_id,
                "label": collection["name"],
                "path": target["path"],
            })
        if len(steps) < 2:
            raise ValueError(f"Learning path needs at least two available steps: {path['id']}")
        learning_paths.append({
            "id": path["id"],
            "title": path["title"],
            "description": path["description"],
            "steps": steps,
        })

    totals_by_type = Counter(document["type"] for document in flattened)
    catalog = {
        "version": 2,
        "generatedFrom": DEFAULT_BRANCH,
        "repository": REPOSITORY,
        "pages": PAGES,
        "stats": {
            "markdownDocuments": len(flattened),
            "collections": len(collections),
            "documentTypes": dict(sorted(totals_by_type.items())),
        },
        "collections": collections,
        "assets": assets,
        "learningPaths": learning_paths,
    }

    postings: dict[str, list[list[int]]] = defaultdict(list)
    for document_id, document in enumerate(flattened):
        collection = by_id[document["collection"]]
        source_text = (ROOT / document["path"]).read_text(encoding="utf-8-sig")
        body = Counter(re.findall(r"[\w]+", plain_text(source_text).casefold(), flags=re.UNICODE))
        title = Counter(re.findall(r"[\w]+", document["title"].casefold(), flags=re.UNICODE))
        headings = Counter(
            token
            for heading in document["headings"]
            for token in re.findall(r"[\w]+", heading["text"].casefold(), flags=re.UNICODE)
        )
        metadata = Counter(
            re.findall(r"[\w]+", f"{collection['name']} {collection['description']} {' '.join(document['tags'])}".casefold(), flags=re.UNICODE)
        )
        scores: Counter[str] = Counter()
        scores.update({term: min(count, 3) * 10 for term, count in title.items()})
        scores.update({term: min(count, 4) * 5 for term, count in headings.items()})
        scores.update({term: min(count, 3) * 2 for term, count in metadata.items()})
        scores.update({term: min(count, 5) for term, count in body.items()})
        for term, score in scores.items():
            if term not in STOP_WORDS and len(term) > 1:
                postings[term].append([document_id, score])
    search_index = {
        "version": 1,
        "generatedFrom": DEFAULT_BRANCH,
        "documentPaths": [document["path"] for document in flattened],
        "terms": {term: postings[term] for term in sorted(postings)},
    }
    for document in flattened:
        del document["headings"]
    return catalog, search_index


def encode_json(value: dict, compact: bool = False) -> str:
    options = {"ensure_ascii": False}
    if compact:
        return json.dumps(value, separators=(",", ":"), **options) + "\n"
    return json.dumps(value, indent=2, **options) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify generated files are current without writing them",
    )
    args = parser.parse_args()
    try:
        catalog, search_index = build_payloads()
        expected = {
            CATALOG_PATH: encode_json(catalog),
            SEARCH_PATH: encode_json(search_index, compact=True),
        }
        if args.check:
            stale = [path.relative_to(ROOT).as_posix() for path, content in expected.items()
                     if not path.is_file() or path.read_text(encoding="utf-8") != content]
            if stale:
                print("Generated output is stale: " + ", ".join(stale), file=sys.stderr)
                return 1
            print(
                f"Catalogue is current: {catalog['stats']['markdownDocuments']} documents "
                f"across {catalog['stats']['collections']} collections; "
                f"{len(search_index['terms'])} indexed terms."
            )
            return 0
        for path, content in expected.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
        print(
            f"Generated {CATALOG_PATH.relative_to(ROOT)} and {SEARCH_PATH.relative_to(ROOT)}: "
            f"{catalog['stats']['markdownDocuments']} documents across "
            f"{catalog['stats']['collections']} collections; {len(search_index['terms'])} terms."
        )
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Content index generation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
