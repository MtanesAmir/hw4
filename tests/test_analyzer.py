import unittest
import os
import tempfile
from centrality.graph import KnowledgeGraph

class TestAnalyzer(unittest.TestCase):
    def test_graph_degrees(self):
        # Create a temporary directory simulating a small vault
        with tempfile.TemporaryDirectory() as temp_dir:
            # Write mock files:
            # - index.md: links to [[NodeA]], [[NodeB]]
            # - NodeA.md: links to [[NodeB]], [[NodeC]]
            # - NodeB.md: links to [[NodeA]]
            # - NodeC.md: contains frontmatter metadata
            
            with open(os.path.join(temp_dir, "index.md"), 'w', encoding='utf-8') as f:
                f.write("Welcome to mock vault. [[NodeA]], [[NodeB]]")
            with open(os.path.join(temp_dir, "NodeA.md"), 'w', encoding='utf-8') as f:
                f.write("Node A content. Links: [[NodeB]] and [[NodeC]]")
            with open(os.path.join(temp_dir, "NodeB.md"), 'w', encoding='utf-8') as f:
                f.write("Node B content. Links: [[NodeA]]")
            with open(os.path.join(temp_dir, "NodeC.md"), 'w', encoding='utf-8') as f:
                f.write("---\nsource_file: 'src/node_c.py'\nlocation: 'L10'\n---\nNode C content")
                
            graph = KnowledgeGraph(temp_dir)
            graph.build_from_entry(os.path.join(temp_dir, "index.md"))
            
            # Verify nodes are parsed correctly
            self.assertIn("index", graph.nodes)
            self.assertIn("NodeA", graph.nodes)
            self.assertIn("NodeB", graph.nodes)
            self.assertIn("NodeC", graph.nodes)
            
            # Check frontmatter parsing
            self.assertEqual(graph.nodes["NodeC"]["source_file"], "src/node_c.py")
            self.assertEqual(graph.nodes["NodeC"]["location"], "L10")
            
            # Check degree calculation:
            # Edges:
            # - (index, NodeA)
            # - (index, NodeB)
            # - (NodeA, NodeB)
            # - (NodeA, NodeC)
            # Degrees:
            # - index: 2
            # - NodeA: 3
            # - NodeB: 2
            # - NodeC: 1
            degrees = graph.calculate_degrees()
            self.assertEqual(degrees["index"], 2)
            self.assertEqual(degrees["NodeA"], 3)
            self.assertEqual(degrees["NodeB"], 2)
            self.assertEqual(degrees["NodeC"], 1)

    def test_load_from_json(self):
        import json
        with tempfile.TemporaryDirectory() as temp_dir:
            obsidian_dir = os.path.join(temp_dir, "obsidian")
            os.makedirs(obsidian_dir)
            
            # Write a mock file inside obsidian dir to test vault mapping resolution
            with open(os.path.join(obsidian_dir, "verify.sh script_1.md"), 'w', encoding='utf-8') as f:
                f.write("---\nsource_file: 'projects/ansible/verify.sh'\nlocation: 'L1'\n---\n")
                
            # Create a mock graph.json
            graph_json_data = {
                "nodes": [
                    {
                        "id": "node_ansible_verify",
                        "label": "verify.sh script",
                        "source_file": "projects/ansible/verify.sh",
                        "source_location": "L1",
                        "file_type": "code"
                    },
                    {
                        "id": "node_readme",
                        "label": "BugsInPy README",
                        "source_file": "README.md",
                        "source_location": "N/A",
                        "file_type": "document"
                    }
                ],
                "links": [
                    {
                        "source": "node_ansible_verify",
                        "target": "node_readme"
                    }
                ]
            }
            
            json_file_path = os.path.join(temp_dir, "graph.json")
            with open(json_file_path, 'w', encoding='utf-8') as f:
                json.dump(graph_json_data, f)
                
            graph = KnowledgeGraph(obsidian_dir)
            graph.load_from_json(json_file_path)
            
            # Verify nodes were loaded and normalized to vault names
            self.assertIn("verify.sh script_1", graph.nodes)
            self.assertIn("BugsInPy README", graph.nodes)
            
            # Check properties
            self.assertEqual(graph.nodes["verify.sh script_1"]["type"], "code")
            self.assertEqual(graph.nodes["verify.sh script_1"]["source_file"], "projects/ansible/verify.sh")
            
            # Check degrees
            degrees = graph.calculate_degrees()
            self.assertEqual(degrees["verify.sh script_1"], 1)
            self.assertEqual(degrees["BugsInPy README"], 1)

    def test_generate_report(self):
        from centrality.reporter import generate_report
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a simple mock graph
            graph = KnowledgeGraph(temp_dir)
            graph.nodes["NodeA"] = {
                "label": "NodeA",
                "file_path": os.path.join(temp_dir, "NodeA.md"),
                "source_file": "src/node_a.py",
                "location": "L1",
                "type": "code"
            }
            graph.nodes["NodeB"] = {
                "label": "NodeB",
                "file_path": os.path.join(temp_dir, "NodeB.md"),
                "source_file": "src/node_b.py",
                "location": "L5",
                "type": "code"
            }
            graph.add_edge("NodeA", "NodeB")
            
            output_file = os.path.join(temp_dir, "Centrality.md")
            generate_report(graph, output_file, "TestProject")
            
            # Read output file
            self.assertTrue(os.path.exists(output_file))
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verify structure and content
            self.assertIn("# Centrality (Subject 8)", content)
            self.assertIn("## Central Nodes in TestProject", content)
            self.assertIn("| Rank | Central Node | Connections (Degree) | Origin File | Location |", content)
            self.assertIn("| 1 | [[NodeA]] | 1 | [src/node_a.py](src/node_a.py) | L1 |", content)
            self.assertIn("| 2 | [[NodeB]] | 1 | [src/node_b.py](src/node_b.py) | L5 |", content)

if __name__ == '__main__':
    unittest.main()
