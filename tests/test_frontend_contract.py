import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.elements = {}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            self.ids.append(element_id)
            self.elements[element_id] = (tag, attributes)


class FrontendContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = PageParser()
        cls.parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))

    def test_page_has_unique_ids_and_skip_navigation(self):
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)))
        self.assertEqual(self.parser.elements["main"][0], "main")
        self.assertEqual(self.parser.elements["search"][1].get("aria-label"), "Search all handbook content")

    def test_search_results_have_screen_reader_announcement(self):
        tag, attributes = self.parser.elements["searchResults"]
        self.assertEqual(tag, "div")
        self.assertEqual(attributes.get("aria-live"), "polite")

    def test_reader_is_modal_named_and_has_keyboard_controls(self):
        tag, attributes = self.parser.elements["viewer"]
        self.assertEqual(tag, "div")
        self.assertEqual(attributes.get("role"), "dialog")
        self.assertEqual(attributes.get("aria-modal"), "true")
        self.assertTrue(attributes.get("aria-label"))
        self.assertEqual(self.parser.elements["close"][1].get("aria-label"), "Close document")
        self.assertTrue(self.parser.elements["tocbtn"][1].get("aria-controls"))

    def test_reader_errors_offer_a_document_retry(self):
        app = (ROOT / "assets" / "js" / "app.js").read_text(encoding="utf-8")
        self.assertIn('id="retryDocument"', app)
        self.assertIn("openDocument(state.currentPath, decodeFragment(location.hash.slice(1)), true)", app)

    def test_fragment_target_is_restored_after_reader_scroll_reset(self):
        app = (ROOT / "assets" / "js" / "app.js").read_text(encoding="utf-8")
        reset = app.index("$('#article').scrollTop = 0;")
        target = app.index("const target = fragment ? document.getElementById(fragment) : null;", reset)
        scroll = app.index("target.scrollIntoView({ block: 'start' });", target)
        self.assertLess(reset, target)
        self.assertLess(target, scroll)


if __name__ == "__main__":
    unittest.main()
