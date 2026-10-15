import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_knowledge_base", ROOT / "scripts" / "validate-knowledge-base.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class HeadingValidationTests(unittest.TestCase):
    def test_github_heading_slugs_and_duplicate_suffixes(self):
        anchors, _, warnings = validator.heading_anchors(
            "# API & Security\n## Threat Model\n## Threat Model\n```md\n# ignored\n```\n<a id=\"custom-anchor\"></a>\n"
        )
        self.assertEqual(anchors, {"api-security", "threat-model", "threat-model-1", "custom-anchor"})
        self.assertEqual(len(warnings), 1)

    def test_unicode_fragments_are_preserved(self):
        self.assertEqual(validator.github_slug("安全な API"), "安全な-api")

    def test_generated_heading_ids_do_not_collide_with_explicit_suffixes(self):
        anchors, _, warnings = validator.heading_anchors("# Repeat\n# Repeat\n# Repeat-1\n")
        self.assertEqual(anchors, {"repeat", "repeat-1", "repeat-1-1"})
        self.assertEqual(len(warnings), 2)

    def test_headings_inside_fences_are_not_anchors(self):
        anchors, headings, _ = validator.heading_anchors("```markdown\n# Hidden\n```\n# Visible\n")
        self.assertEqual(anchors, {"visible"})
        self.assertEqual(headings, ["Visible"])

    def test_unclosed_fence_is_reported_at_its_opening_line(self):
        self.assertEqual(validator.unclosed_fence_line("# Heading\n```python\nprint(1)\n"), 2)
        self.assertIsNone(validator.unclosed_fence_line("```python\nprint(1)\n```\n"))
        self.assertIsNone(validator.unclosed_fence_line("````md\n```py\nx\n```\n````"))


class LinkValidationTests(unittest.TestCase):
    def test_inline_reference_html_and_image_targets_are_detected(self):
        text = (
            "[guide](../docs/README.md#repository-documentation)\n"
            "[style][styles]\n"
            "[styles]: ../docs/Markdown-Style-Guide.md\n"
            "![diagram](../assets/README.md)\n"
            '<a href="../docs/DEPLOYMENT.md">Deploy</a><img src="../favicon.svg" alt="mark">\n'
        )
        found = validator.markdown_targets(text)
        targets = [item[0] for item in found]
        self.assertIn("../docs/README.md#repository-documentation", targets)
        self.assertIn("../docs/Markdown-Style-Guide.md", targets)
        self.assertIn("../assets/README.md", targets)
        self.assertIn("../docs/DEPLOYMENT.md", targets)
        self.assertIn("../favicon.svg", targets)

    def test_unresolved_reference_is_reported_but_task_checkbox_is_not(self):
        targets = validator.markdown_targets("- [ ] pending work\n\n[missing][not-defined]\n")
        self.assertEqual([target for target, _, _ in targets], ["__missing_reference__:not-defined"])

    def test_code_examples_are_not_scanned_as_links(self):
        targets = validator.markdown_targets("```md\n[broken](missing.md)\n```\n")
        self.assertEqual(targets, [])

    def test_inline_code_is_ignored_and_missing_image_alt_is_reported(self):
        targets = validator.markdown_targets('`<img src="demo.png">`\n<img src="real.png" alt="">\n')
        self.assertEqual([kind for _, kind, _ in targets], ["image", "image_alt"])

    def test_nested_relative_file_and_fragment_resolve(self):
        source = ROOT / "Networking" / "fixture.md"
        self.assertIsNone(validator.check_link(
            source,
            "../docs/README.md#repository-documentation",
            1,
            {},
        ))

    def test_query_string_does_not_change_local_target(self):
        source = ROOT / "Networking" / "fixture.md"
        self.assertIsNone(validator.check_link(source, "../docs/README.md?view=1", 1, {}))

    def test_encoded_spaces_parentheses_query_and_fragment(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            directory = Path(temp)
            source = directory / "source.md"
            source.write_text("# Source\n", encoding="utf-8")
            (directory / "guide with (lab).md").write_text(
                "# Encoded target\n", encoding="utf-8"
            )
            url = "guide%20with%20%28lab%29.md?view=full#encoded-target"
            self.assertIsNone(validator.check_link(source, url, 1, {}))


if __name__ == "__main__":
    unittest.main()
