import unittest
from centrality.extractor import parse_frontmatter, extract_wiki_links, extract_markdown_links, extract_all_links

class TestExtractor(unittest.TestCase):
    def test_parse_frontmatter(self):
        content = """---
source_file: "projects/PySnooper/verify.sh"
type: "code"
community: "Community 6"
location: "L1"
---
# Page Header
"""
        metadata = parse_frontmatter(content)
        self.assertEqual(metadata.get('source_file'), 'projects/PySnooper/verify.sh')
        self.assertEqual(metadata.get('type'), 'code')
        self.assertEqual(metadata.get('community'), 'Community 6')
        self.assertEqual(metadata.get('location'), 'L1')

    def test_parse_frontmatter_empty(self):
        content = "# Just markdown\nNo frontmatter here."
        metadata = parse_frontmatter(content)
        self.assertEqual(metadata, {})

    def test_extract_wiki_links(self):
        content = """
## Connections
- [[Ansible Project]] - conceptually_related_to
- [[Black Project|Black]] - conceptually_related_to
- [[projects/PySnooper/verify.sh]]
"""
        links = extract_wiki_links(content)
        self.assertEqual(links, ['Ansible Project', 'Black Project', 'projects/PySnooper/verify.sh'])

    def test_extract_markdown_links(self):
        content = """
[Link to README](README.md)
[External Link](https://google.com)
[Anchor link](#section)
"""
        links = extract_markdown_links(content)
        self.assertEqual(links, ['README.md'])

if __name__ == '__main__':
    unittest.main()
