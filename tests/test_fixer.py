import os
import unittest
import tempfile
import shutil

from fixer.parser import parse_markdown_tables
from fixer.engine import refactor_file
from fixer.reporter import FixerReporter

class TestFixer(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def test_parse_markdown_tables(self):
        md_content = """
# Test Report

| Violating Node | Origin File | Location | Bug Type |
| :--- | :--- | :--- | :--- |
| [[node.py]] | [path/to/node.py](path/to/node.py) | L15 | Infinite Waiting |
| [[none.py]] | - | - | - |
"""
        md_path = os.path.join(self.test_dir, "report.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        rows = parse_markdown_tables(md_path)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['Location'], 'L15')
        self.assertEqual(rows[0]['Bug Type'], 'Infinite Waiting')
        self.assertEqual(rows[0]['Origin File'], 'path/to/node.py')
        
    def test_refactor_infinite_waiting(self):
        code = """import requests
def fetch():
    return requests.get("https://example.com")
"""
        code_path = os.path.join(self.test_dir, "code.py")
        with open(code_path, 'w', encoding='utf-8') as f:
            f.write(code)
            
        success, original = refactor_file(code_path, 'Infinite Resource Waiting')
        self.assertTrue(success)
        self.assertIn("requests.get", original)
        
        with open(code_path, 'r', encoding='utf-8') as f:
            refactored = f.read()
        self.assertIn('timeout=10', refactored)
        self.assertIn('requests.get("https://example.com", timeout=10)', refactored)
        
    def test_refactor_unbounded_retries(self):
        code = """def run():
    while True:
        try:
            call_api()
            break
        except Exception:
            pass
"""
        code_path = os.path.join(self.test_dir, "code.py")
        with open(code_path, 'w', encoding='utf-8') as f:
            f.write(code)
            
        success, _ = refactor_file(code_path, 'Unbounded Retries')
        self.assertTrue(success)
        
        with open(code_path, 'r', encoding='utf-8') as f:
            refactored = f.read()
        self.assertIn('while _retries < 3:', refactored)
        self.assertIn('_retries += 1', refactored)
        self.assertIn('time.sleep(1)', refactored)
        
    def test_refactor_local_state(self):
        code = """class App:
    def __init__(self):
        self.session = {}
"""
        code_path = os.path.join(self.test_dir, "code.py")
        with open(code_path, 'w', encoding='utf-8') as f:
            f.write(code)
            
        success, _ = refactor_file(code_path, 'Local State Dependency')
        self.assertTrue(success)
        
        with open(code_path, 'r', encoding='utf-8') as f:
            refactored = f.read()
        self.assertIn('import redis', refactored)
        self.assertIn('redis.Redis', refactored)
        
if __name__ == '__main__':
    unittest.main()
