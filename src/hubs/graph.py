import os
import re
import json
from centrality.extractor import parse_frontmatter

class HubsGraph:
    def __init__(self, vault_dir: str):
        self.vault_dir = vault_dir
        self.nodes = {}  # node_name -> metadata dict
        self.adjacency = {}  # node_name -> list of neighbors

    def add_node(self, node_name: str, src_file: str, loc: str, file_type: str):
        if node_name not in self.nodes:
            self.nodes[node_name] = {
                'label': node_name,
                'file_path': os.path.join(self.vault_dir, node_name + ".md") if self.vault_dir else "",
                'source_file': src_file,
                'location': loc,
                'type': file_type
            }
        if node_name not in self.adjacency:
            self.adjacency[node_name] = []

    def add_edge(self, u: str, v: str):
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        if v not in self.adjacency[u]:
            self.adjacency[u].append(v)
        if u not in self.adjacency[v]:
            self.adjacency[v].append(u)

    def build_vault_mapping(self) -> dict:
        mapping = {}
        if not self.vault_dir or not os.path.exists(self.vault_dir):
            return mapping
            
        for fname in os.listdir(self.vault_dir):
            if fname.lower().endswith('.md'):
                file_path = os.path.join(self.vault_dir, fname)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    metadata = parse_frontmatter(content)
                    src_file = metadata.get('source_file')
                    loc = metadata.get('location', 'N/A')
                    if src_file:
                        base_name = os.path.splitext(fname)[0]
                        label = re.sub(r'_\d+$', '', base_name)
                        mapping[(label, src_file, loc)] = base_name
                except Exception:
                    pass
        return mapping

    def load_from_json(self, json_file_path: str):
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        vault_map = self.build_vault_mapping()
        id_to_name = {}
        
        for node_data in data.get('nodes', []):
            node_id = node_data.get('id')
            label = node_data.get('label')
            src_file = node_data.get('source_file', 'N/A')
            loc = node_data.get('source_location', 'N/A')
            file_type = node_data.get('file_type', 'N/A')
            
            vault_name = vault_map.get((label, src_file, loc))
            if vault_name:
                node_name = vault_name
            else:
                node_name = label
                
            id_to_name[node_id] = node_name
            self.add_node(node_name, src_file, loc, file_type)
            
        for link in data.get('links', []):
            src_id = link.get('source')
            tgt_id = link.get('target')
            u = id_to_name.get(src_id)
            v = id_to_name.get(tgt_id)
            if u and v:
                self.add_edge(u, v)
