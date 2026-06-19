import unittest
import tempfile
import os
import shutil
from reverse_engineer.ast_scanner import ASTScanner
from reverse_engineer.mapper import generate_block_diagram, generate_oop_diagram

class TestReverseEngineer(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def test_ast_scanning_rules(self):
        # Create a mock python file with inheritance and composition
        code = """import os
from collections import OrderedDict

class BaseModule:
    def execute(self):
        pass

class CustomAgent(BaseModule):
    def __init__(self):
        self.scanner = OrderedDict()
        
    def run_flow(self):
        self.execute()
"""
        file_path = os.path.join(self.test_dir, "agent.py")
        with open(file_path, "w") as f:
            f.write(code)
            
        scanner = ASTScanner(self.test_dir)
        scanner.scan()
        
        self.assertIn("CustomAgent", scanner.classes)
        self.assertIn("BaseModule", scanner.classes)
        
        agent_info = scanner.classes["CustomAgent"]
        self.assertIn("BaseModule", agent_info["bases"])
        self.assertIn("OrderedDict", agent_info["compositions"])
        self.assertIn("run_flow", agent_info["methods"])
        
        block_mermaid = generate_block_diagram(scanner.modules)
        oop_mermaid = generate_oop_diagram(scanner.classes)
        
        self.assertIn("graph TD", block_mermaid)
        self.assertIn("classDiagram", oop_mermaid)
        self.assertIn("class CustomAgent", oop_mermaid)

if __name__ == "__main__":
    unittest.main()
