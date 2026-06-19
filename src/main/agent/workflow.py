import os
import json
from bugs.graph_loader import BugsGraph
from hubs.analyzer import calculate_betweenness_centrality
from bugs.evaluators import (
    check_tight_coupling,
    check_god_class,
    check_local_state_dependency,
    check_unbounded_retries,
    check_infinite_waiting,
    check_syntax_errors
)

class ResearchBugsAgentWorkflow:
    def __init__(self, graph_json_path: str, vault_dir: str, project_root: str):
        self.graph_json_path = graph_json_path
        self.vault_dir = vault_dir
        self.project_root = project_root
        self.state = {
            "graph": None,
            "centrality": {},
            "hubs": {},
            "bridges": [],
            "bugs": [],
            "report_path": ""
        }

    def run(self):
        print("[Agent] Starting workflow execution...")
        self.load_graph_node()
        self.centrality_node()
        self.hubs_node()
        self.bridges_node()
        self.bugs_node()
        self.compile_report_node()
        print("[Agent] Workflow executed successfully!")

    def load_graph_node(self):
        print("[Agent Node] Loading graph structure...")
        graph = BugsGraph(self.vault_dir)
        graph.load_from_json(self.graph_json_path)
        self.state["graph"] = graph

    def centrality_node(self):
        print("[Agent Node] Computing Degree Centrality (Subject 8)...")
        graph = self.state["graph"]
        degrees = {name: len(neighbors) for name, neighbors in graph.adjacency.items()}
        filtered = {}
        for name, deg in degrees.items():
            if name.startswith('_COMMUNITY_') or name.lower() in ('index', 'graph_report'):
                continue
            if graph.nodes.get(name, {}).get('type') == 'community':
                continue
            filtered[name] = deg
        self.state["centrality"] = sorted(filtered.items(), key=lambda x: x[1], reverse=True)

    def hubs_node(self):
        print("[Agent Node] Computing Hubs / Betweenness Centrality (Subject 10)...")
        graph = self.state["graph"]
        cb = calculate_betweenness_centrality(graph)
        filtered = {}
        for name, score in cb.items():
            if name.startswith('_COMMUNITY_') or name.lower() in ('index', 'graph_report'):
                continue
            if graph.nodes.get(name, {}).get('type') == 'community':
                continue
            filtered[name] = score
        self.state["hubs"] = sorted(filtered.items(), key=lambda x: x[1], reverse=True)

    def bridges_node(self):
        print("[Agent Node] Detecting Bridge Nodes (inter-community connectors)...")
        graph = self.state["graph"]
        bridges = []
        for name, node_info in graph.nodes.items():
            if name.startswith('_COMMUNITY_') or node_info.get('type') == 'community':
                continue
            my_comm = node_info.get('community')
            if my_comm is None:
                continue
            
            neighbors = graph.adjacency.get(name, [])
            cross_comms = set()
            for neighbor in neighbors:
                n_info = graph.nodes.get(neighbor)
                if n_info:
                    n_comm = n_info.get('community')
                    if n_comm is not None and n_comm != my_comm:
                        cross_comms.add(n_comm)
                        
            if cross_comms:
                bridges.append({
                    'node': name,
                    'file': node_info.get('source_file', 'N/A'),
                    'location': node_info.get('location', 'N/A'),
                    'connected_communities': sorted(list(cross_comms)),
                    'degree': len(neighbors)
                })
        self.state["bridges"] = sorted(bridges, key=lambda x: len(x['connected_communities']), reverse=True)

    def bugs_node(self):
        print("[Agent Node] Running Architectural Bug Evaluators...")
        graph = self.state["graph"]
        tc = check_tight_coupling(graph)
        gc = check_god_class(graph)
        ls = check_local_state_dependency(graph, self.project_root)
        ur = check_unbounded_retries(graph, self.project_root)
        iw = check_infinite_waiting(graph, self.project_root)
        se = check_syntax_errors(graph, self.project_root)
        
        all_bugs = []
        for v in tc:
            all_bugs.append({**v, 'type': 'Tight Coupling (The Domino Effect)'})
        for v in gc:
            all_bugs.append({**v, 'type': 'The "God Class" / Monolith'})
        for v in ls:
            all_bugs.append({**v, 'type': 'Local State Dependency (Sticky Sessions)'})
        for v in ur:
            all_bugs.append({**v, 'type': 'Unbounded Retries (Thundering Herd)'})
        for v in iw:
            all_bugs.append({**v, 'type': 'Infinite Resource Waiting'})
        for v in se:
            all_bugs.append({**v, 'type': 'Syntax/Compilation Error'})
            
        self.state["bugs"] = all_bugs

    def compile_report_node(self):
        print("[Agent Node] Compiling results to bugs_we_found.md...")
        if any(tok in self.project_root.lower() for tok in ('temp', 'tmp', 'var/')):
            reports_dir = os.path.join(self.project_root, 'reports')
        else:
            workspace_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
            reports_dir = os.path.join(workspace_root, 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        report_path = os.path.join(reports_dir, 'bugs_we_found.md')
        self.state["report_path"] = report_path
        
        lines = [
            "This file was written by the Agent.",
            "",
            "# Architectural Analysis and Bugs Found",
            "",
            "This report is automatically generated by the autonomous `ResearchBugsAgent` after evaluating the codebase graph.",
            "",
            "## 1. Central Nodes (Degree Centrality - Subject 8)",
            "Top highly-connected nodes in the architecture:",
            "",
            "| Rank | Node | Degree | Origin File | Location |",
            "| :--- | :--- | :--- | :--- | :--- |"
        ]
        
        for idx, (name, deg) in enumerate(self.state["centrality"][:10], 1):
            n_info = self.state["graph"].nodes.get(name, {})
            src = n_info.get('source_file', 'N/A')
            loc = n_info.get('location', 'N/A')
            origin_link = f"[{src}]({src})" if src and src != 'N/A' else "N/A"
            lines.append(f"| {idx} | [[{name}]] | {deg} | {origin_link} | {loc} |")
            
        lines.extend([
            "",
            "## 2. Hubs (Betweenness Centrality - Subject 10)",
            "Top structural bottlenecks in the system:",
            "",
            "| Rank | Node | Betweenness Score | Origin File | Location |",
            "| :--- | :--- | :--- | :--- | :--- |"
        ])
        
        for idx, (name, score) in enumerate(self.state["hubs"][:10], 1):
            n_info = self.state["graph"].nodes.get(name, {})
            src = n_info.get('source_file', 'N/A')
            loc = n_info.get('location', 'N/A')
            origin_link = f"[{src}]({src})" if src and src != 'N/A' else "N/A"
            lines.append(f"| {idx} | [[{name}]] | {score:.3f} | {origin_link} | {loc} |")
            
        lines.extend([
            "",
            "## 3. Bridge Nodes (Cross-Community Links)",
            "Nodes that connect different communities:",
            "",
            "| Rank | Node | Connected Communities | Degree | Origin File | Location |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |"
        ])
        
        for idx, b in enumerate(self.state["bridges"][:10], 1):
            name = b['node']
            comms_str = ", ".join(f"Community {c}" for c in b['connected_communities'])
            src = b['file']
            loc = b['location']
            origin_link = f"[{src}]({src})" if src and src != 'N/A' else "N/A"
            lines.append(f"| {idx} | [[{name}]] | {comms_str} | {b['degree']} | {origin_link} | {loc} |")
            
        lines.extend([
            "",
            "## 4. Architectural Bugs and Anti-Patterns Found",
            "Specific architectural defects flagged in the system:",
            "",
            "| Rank | Violating Node | Origin File | Location | Bug Type | Explanation | Suggested Fix |",
            "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
        ])
        
        if not self.state["bugs"]:
            lines.append("| - | None | - | - | - | All checks passed. | - |")
        else:
            for idx, bug in enumerate(self.state["bugs"], 1):
                name = bug['node']
                src = bug['file']
                loc = bug['location']
                b_type = bug['type']
                details = bug['details']
                fix = bug['fix']
                origin_link = f"[{src}]({src})" if src and src != 'N/A' else "N/A"
                lines.append(f"| {idx} | [[{name}]] | {origin_link} | {loc} | {b_type} | {details} | {fix} |")
                
        lines.append("")
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines) + "\n")
