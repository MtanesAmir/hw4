import unittest
import tempfile
import os
import shutil
from suggestions.parser import parse_bugs_report
from suggestions.mapper import map_bugs_to_suggestions

class TestSuggestions(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def test_parser_and_mapper(self):
        bugs_md_content = """# Architectural Bugs Report

## 1. Tight Coupling (The Domino Effect)
| Node | Origin File | Location | Details | Fix Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| [[ServiceA]] | [ServiceA.py](ServiceA.py) | L10 | Coupling ratio: 0.8 | Decouple |

## 2. The "God Class" / Monolith
No violations detected in this category.

## 3. Local State Dependency (Sticky Sessions)
No violations detected in this category.

## 4. Unbounded Retries (Thundering Herd)
No violations detected in this category.

## 5. Infinite Resource Waiting
No violations detected in this category.
"""
        bugs_path = os.path.join(self.test_dir, "Bugs.md")
        with open(bugs_path, "w") as f:
            f.write(bugs_md_content)
            
        categories = parse_bugs_report(bugs_path)
        self.assertEqual(len(categories[1]), 1)
        self.assertEqual(categories[1][0]['node'], "ServiceA")
        
        sugs = map_bugs_to_suggestions(categories)
        self.assertEqual(len(sugs), 1)
        self.assertEqual(sugs[0]['node'], "ServiceA")
        self.assertEqual(sugs[0]['principle'], "Decoupling of Application Architecture")

if __name__ == "__main__":
    unittest.main()
