import unittest
import tempfile
import os
import shutil
import json
from agent.workflow import ResearchBugsAgentWorkflow

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def test_agent_workflow_execution(self):
        # Setup a minimal valid graph structure
        graph_data = {
            "nodes": [
                {"id": "A", "label": "NodeA", "type": "file", "community": 0, "metadata": {"source_file": "A.py", "location": "L1"}},
                {"id": "B", "label": "NodeB", "type": "file", "community": 1, "metadata": {"source_file": "B.py", "location": "L1"}}
            ],
            "links": [
                {"source": "A", "target": "B"}
            ]
        }
        graph_path = os.path.join(self.test_dir, "graph.json")
        with open(graph_path, "w") as f:
            f.write(json.dumps(graph_data))
            
        # Create mock files
        with open(os.path.join(self.test_dir, "A.py"), "w") as f:
            f.write("# empty code\n")
        with open(os.path.join(self.test_dir, "B.py"), "w") as f:
            f.write("# empty code\n")
            
        workflow = ResearchBugsAgentWorkflow(graph_path, self.test_dir, self.test_dir)
        workflow.run()
        
        # Verify report generation
        report_path = os.path.join(self.test_dir, "reports", "bugs_we_found.md")
        self.assertTrue(os.path.exists(report_path))
        
        # Check content
        with open(report_path, "r") as f:
            content = f.read()
        self.assertIn("This file was written by the Agent.", content)
        self.assertIn("NodeA", content)
        self.assertIn("NodeB", content)

if __name__ == "__main__":
    unittest.main()
