"""Publication checks for the RNA-seq workshop and its public entry points."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'rnaseq-de-workshop'

class WorkshopPublicationTests(unittest.TestCase):
    def test_discoverable_from_home_tutorials_and_presentations(self):
        for name in ('docs/index.md', 'docs/tutorials/index.md', 'docs/presentations/index.md', 'mkdocs.yml'):
            with self.subTest(path=name):
                self.assertIn(SLUG, (ROOT / name).read_text())

    def test_deck_assets_and_evidence(self):
        path = ROOT / 'docs/presentations' / SLUG / 'index.html'
        text = path.read_text()
        self.assertGreaterEqual(text.count('class="slide'), 12)
        for term in ('toy', 'pydeseq2', 'Metadata missing samples', '0ba950565ee6a0fe9da3bde2164f6c814bd57dc9'):
            self.assertIn(term, text)
        for asset in re.findall(r'src="([^"#]+)"', text):
            if not asset.startswith(('https:', 'http:')):
                self.assertTrue((path.parent / asset).is_file(), asset)
        self.assertNotRegex(text, r'[\u2013\u2014]|<hr\b')
        self.assertNotIn('manuelcorpas1', text)
        self.assertNotIn('drjlgross@gmail.com', text)

    def test_guide_has_reproducible_contract_and_scoping(self):
        text = (ROOT / 'docs/tutorials' / (SLUG + '.md')).read_text()
        for term in ('~ batch + condition', 'condition,treated,control', '--backend pydeseq2', 'input_checksum', 'worksheet', '0ba950565ee6a0fe9da3bde2164f6c814bd57dc9'):
            self.assertIn(term, text)
        self.assertNotRegex(text, r'[\u2013\u2014]|(?m:^---$)|<hr\b')

if __name__ == '__main__':
    unittest.main()
