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

if __name__ == '__main__':
    unittest.main()
