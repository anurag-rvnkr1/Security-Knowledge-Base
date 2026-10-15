import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import importlib.util

SPEC = importlib.util.spec_from_file_location("build_content_index", ROOT / "scripts" / "build-content-index.py")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class TitleExtractionTests(unittest.TestCase):
    def test_markdown_h1_preserves_authored_title_and_removes_chapter_prefix(self):
        self.assertEqual(
            builder.extract_title("# 01 - Introduction to APIs\n\nText", "01-intro.md"),
            "Introduction to APIs",
        )

    def test_front_matter_title_takes_precedence(self):
        text = "---\ntitle: 'OAuth 2.0: *Safe* Design'\n---\n# Other heading\n"
        self.assertEqual(builder.extract_title(text, "oauth.md"), "OAuth 2.0: Safe Design")

    def test_front_matter_supports_double_quotes_and_unicode(self):
        text = '---\ntitle: "安全な API"\n---\n# Other\n'
        self.assertEqual(builder.extract_title(text, "security.md"), "安全な API")

    def test_fenced_heading_is_not_a_document_title(self):
        text = '```markdown\n# Not a title\n```\n\n## Contents\n\n# Real title\n'
        self.assertEqual(builder.extract_title(text, "source.md"), "Real title")

    def test_fence_with_info_string_does_not_close_an_open_fence(self):
        text = "````markdown\n```python\n# Not a title\n```\n````\n# Real title\n"
        self.assertEqual(builder.extract_title(text, "source.md"), "Real title")

    def test_first_real_h1_wins(self):
        self.assertEqual(builder.extract_title("# First\n\n# Second\n", "source.md"), "First")

    def test_html_h1_is_supported(self):
        self.assertEqual(builder.extract_title("<main><h1>Detection &amp; Response</h1></main>", "x.md"), "Detection & Response")

    def test_html_skips_placeholder_and_preserves_technical_punctuation(self):
        text = "<h1>Contents</h1><h1>C# and snake_case APIs</h1>"
        self.assertEqual(builder.extract_title(text, "x.md"), "C# and snake_case APIs")

    def test_markdown_closing_hashes_do_not_strip_c_sharp(self):
        self.assertEqual(builder.extract_title("# C# Security ###\n", "x.md"), "C# Security")

    def test_filename_h1_is_skipped_for_the_authored_chapter_heading(self):
        text = "# 06-Organizational-Units.md\n\n# Part 1 — Organizational Units Fundamentals\n"
        self.assertEqual(
            builder.extract_title(text, "06-Organizational-Units.md"),
            "Part 1 — Organizational Units Fundamentals",
        )

    def test_filename_fallback_handles_numbering_and_acronyms(self):
        self.assertEqual(builder.extract_title("No heading", "12-OWASP-API_(JWT).md"), "OWASP API (JWT)")

    def test_filename_fallback_handles_spaces_and_punctuation(self):
        self.assertEqual(builder.extract_title("", "Web Security (Quick-Start).md"), "Web Security (Quick Start)")

    def test_numeric_only_filename_gets_a_readable_fallback(self):
        self.assertEqual(builder.extract_title("", "01.md"), "Document 01")

    def test_malformed_or_empty_front_matter_title_falls_back_to_h1(self):
        for value in ("", "[]", "TODO", '"'):
            with self.subTest(value=value):
                text = f"---\ntitle: {value}\n---\n# Useful title\n"
                self.assertEqual(builder.extract_title(text, "fallback.md"), "Useful title")

    def test_readme_uses_its_collection_heading(self):
        self.assertEqual(builder.extract_title("# CTF Writeups\n\n## Overview", "README.md"), "CTF Writeups")


class GeneratedIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue, cls.search_index = builder.build_outputs()

    def test_catalogue_covers_repository_markdown_and_groups_non_domains(self):
        documents = [doc for category in self.catalogue["categories"] for doc in category["documents"]]
        paths = [doc["path"] for doc in documents]
        self.assertEqual(len(paths), len(set(paths)))
        self.assertEqual(len(paths), self.catalogue["stats"]["markdownDocuments"])
        self.assertTrue(paths)
        self.assertTrue(any(path.startswith("docs/") for path in paths))
        self.assertTrue(any(path.startswith("assets/") for path in paths))
        self.assertTrue({"README.md", "Contributing.md", "SECURITY.md"}.issubset(paths))
        self.assertEqual(len(paths), len([
            path for path in ROOT.rglob("*.md")
            if not any(part in {".git", ".github", "__pycache__", "node_modules", "scripts", "site"} for part in path.parts)
        ]))

    def test_titles_are_nonempty_and_search_paths_match_catalogue_order(self):
        catalogue_docs = [doc for category in self.catalogue["categories"] for doc in category["documents"]]
        search_docs = self.search_index["documents"]
        self.assertEqual([doc["path"] for doc in catalogue_docs], [doc["path"] for doc in search_docs])
        self.assertEqual([doc["title"] for doc in catalogue_docs], [doc["title"] for doc in search_docs])
        self.assertTrue(all(doc["title"].strip() for doc in catalogue_docs))

    def test_search_postings_cover_expected_security_terms(self):
        terms = self.search_index["terms"]
        self.assertIn("kerberos", terms)
        self.assertIn("xss", terms)
        self.assertTrue(all(0 <= row[0] < len(self.search_index["documents"]) for values in terms.values() for row in values))

    def test_search_tokenizer_preserves_security_technical_punctuation(self):
        terms = builder._search_terms("C++ C# .NET MITRE ATT&CK A/B")
        for term in ("c++", "c#", ".net", "att&ck", "a/b"):
            self.assertIn(term, terms)

    def test_learning_paths_point_to_indexed_documents(self):
        known = {doc["path"] for doc in self.search_index["documents"]}
        paths = self.catalogue["learningPaths"]
        self.assertTrue(paths)
        self.assertTrue(all(path in known for item in paths for path in item["documents"]))
        appsec = next(item for item in paths if item["name"] == "Application Security")
        self.assertEqual(appsec["documents"][0], "OWASP/README.md")


if __name__ == "__main__":
    unittest.main()
