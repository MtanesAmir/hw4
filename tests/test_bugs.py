import unittest
import tempfile
import os
import shutil
from bugs.graph_loader import BugsGraph
from bugs.evaluators import (
    check_tight_coupling,
    check_god_class,
    check_local_state_dependency,
    check_unbounded_retries,
    check_infinite_waiting
)

class TestBugs(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def test_tight_coupling(self):
        graph = BugsGraph("")
        # 3 nodes: A (comm 0), B (comm 1), C (comm 2)
        # A connects to B and C -> 100% cross-community links
        graph.nodes = {
            "A": {"community": 0, "type": "file", "source_file": "A.py"},
            "B": {"community": 1, "type": "file", "source_file": "B.py"},
            "C": {"community": 2, "type": "file", "source_file": "C.py"}
        }
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        
        tc = check_tight_coupling(graph)
        self.assertEqual(len(tc), 1)
        self.assertEqual(tc[0]['node'], "A")
        
    def test_god_class(self):
        graph = BugsGraph("")
        graph.nodes = {f"Node_{i}": {"type": "file"} for i in range(15)}
        # Node_0 connects to 9 other nodes (degree = 9)
        for i in range(1, 10):
            graph.add_edge("Node_0", f"Node_{i}")
            
        gc = check_god_class(graph, threshold=8)
        self.assertEqual(len(gc), 1)
        self.assertEqual(gc[0]['node'], "Node_0")
        
    def test_local_state_dependency(self):
        # Create a file containing local session storage and no distributed library import
        file_path = os.path.join(self.test_dir, "state_file.py")
        with open(file_path, "w") as f:
            f.write("session = {}\nsession['user'] = 'auth'\n")
            
        graph = BugsGraph("")
        graph.nodes = {
            "StateFile": {"type": "file", "source_file": "state_file.py", "location": "L1"}
        }
        
        ls = check_local_state_dependency(graph, self.test_dir)
        self.assertEqual(len(ls), 1)
        self.assertEqual(ls[0]['node'], "StateFile")
        
    def test_unbounded_retries(self):
        # Create a file with a retry logic but no exponential backoff / randomized delay
        file_path = os.path.join(self.test_dir, "retry_file.py")
        with open(file_path, "w") as f:
            f.write("def perform_retry():\n    for i in range(3):\n        try:\n            call_api()\n        except:\n            pass # immediate retry\n")
            
        graph = BugsGraph("")
        graph.nodes = {
            "RetryFile": {"type": "file", "source_file": "retry_file.py", "location": "L1"}
        }
        
        ur = check_unbounded_retries(graph, self.test_dir)
        self.assertEqual(len(ur), 1)
        self.assertEqual(ur[0]['node'], "RetryFile")
        
    def test_infinite_waiting(self):
        # Create a file calling requests.get without a timeout parameter
        file_path = os.path.join(self.test_dir, "waiting_file.py")
        with open(file_path, "w") as f:
            f.write("import requests\nsys_response = requests.get('https://example.com/api')\n")
            
        graph = BugsGraph("")
        graph.nodes = {
            "WaitingFile": {"type": "file", "source_file": "waiting_file.py", "location": "L1"}
        }
        
        iw = check_infinite_waiting(graph, self.test_dir)
        self.assertEqual(len(iw), 1)
        self.assertEqual(iw[0]['node'], "WaitingFile")

if __name__ == "__main__":
    unittest.main()
