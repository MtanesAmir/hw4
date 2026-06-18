import unittest
from hubs.graph import HubsGraph
from hubs.analyzer import calculate_betweenness_centrality

class TestHubs(unittest.TestCase):
    def test_star_graph_betweenness(self):
        # A star graph with center node 'A' and leaf nodes 'B', 'C', 'D'
        # All shortest paths between leaf nodes (B, C, D) must go through A.
        # Leaf nodes should have 0 centrality, and center node A should have 1.0 (max).
        graph = HubsGraph("")
        graph.nodes = {v: {} for v in ["A", "B", "C", "D"]}
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("A", "D")
        
        cb = calculate_betweenness_centrality(graph)
        
        self.assertEqual(cb["B"], 0.0)
        self.assertEqual(cb["C"], 0.0)
        self.assertEqual(cb["D"], 0.0)
        self.assertEqual(cb["A"], 1.0)

    def test_path_graph_betweenness(self):
        # Path graph: A - B - C
        # Only the shortest path between A and C passes through B.
        graph = HubsGraph("")
        graph.nodes = {v: {} for v in ["A", "B", "C"]}
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        
        cb = calculate_betweenness_centrality(graph)
        self.assertEqual(cb["A"], 0.0)
        self.assertEqual(cb["C"], 0.0)
        self.assertEqual(cb["B"], 1.0)

if __name__ == '__main__':
    unittest.main()
