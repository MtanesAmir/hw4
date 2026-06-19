import json
import re
import os

class BugsGraph:
    def __init__(self, vault_dir: str):
        self.vault_dir = vault_dir
        self.nodes = {}
        self.adjacency = {}
        self.edges = []
        self.vault_mapping = {}

    def add_edge(self, u: str, v: str):
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        if v not in self.adjacency[u]:
            self.adjacency[u].append(v)
        if u not in self.adjacency[v]:
            self.adjacency[v].append(u)
        self.edges.append((u, v))

    def build_vault_mapping(self):
        if not os.path.exists(self.vault_dir):
            return
        for file_name in os.listdir(self.vault_dir):
            if file_name.endswith('.md'):
                base_name = file_name[:-3]
                clean_label = re.sub(r'_\d+$', '', base_name)
                # Frontmatter parsing
                full_path = os.path.join(self.vault_dir, file_name)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    source_file = "N/A"
                    location = "N/A"
                    
                    sf_match = re.search(r'source_file:\s*(.*)', content)
                    if sf_match:
                        source_file = sf_match.group(1).strip().strip('"').strip("'")
                        
                    loc_match = re.search(r'location:\s*(.*)', content)
                    if loc_match:
                        location = loc_match.group(1).strip().strip('"').strip("'")
                        
                    key = (clean_label, source_file, location)
                    self.vault_mapping[key] = base_name
                except Exception:
                    pass

    def load_from_json(self, json_path: str):
        self.build_vault_mapping()
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Parse nodes
        for node in data.get('nodes', []):
            node_id = node.get('id')
            label = node.get('label', node_id)
            node_type = node.get('type')
            community = node.get('community', None)
            
            meta = node.get('metadata') or {}
            source_file = node.get('source_file') or meta.get('source_file', 'N/A')
            location = node.get('source_location') or node.get('location') or meta.get('location') or meta.get('source_location', 'N/A')
            
            clean_label = re.sub(r'_\d+$', '', label)
            vault_name = self.vault_mapping.get((clean_label, source_file, location), label)
            
            self.nodes[vault_name] = {
                'id': node_id,
                'label': label,
                'type': node_type,
                'community': community,
                'source_file': source_file,
                'location': location
            }
            
        # Parse links
        node_id_to_vault = {node_info['id']: vault_name for vault_name, node_info in self.nodes.items()}
        for link in data.get('links', []):
            src_id = link.get('source')
            tgt_id = link.get('target')
            
            src_name = node_id_to_vault.get(src_id)
            tgt_name = node_id_to_vault.get(tgt_id)
            
            if src_name and tgt_name:
                self.add_edge(src_name, tgt_name)
