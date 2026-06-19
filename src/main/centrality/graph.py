import os
import re
from .extractor import parse_frontmatter, extract_all_links

class KnowledgeGraph:
    def __init__(self, vault_dir: str):
        self.vault_dir = vault_dir
        self.nodes = {}  # node_name -> metadata dict
        self.edges = set()  # set of (node_u, node_v) sorted tuples

    def add_node(self, node_name: str, file_path: str):
        if node_name not in self.nodes:
            # Read file and parse frontmatter
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                metadata = parse_frontmatter(content)
            except Exception:
                metadata = {}
            
            # Populate standard fields
            self.nodes[node_name] = {
                'label': node_name,
                'file_path': file_path,
                'source_file': metadata.get('source_file', 'N/A'),
                'location': metadata.get('location', 'N/A'),
                'type': metadata.get('type', 'N/A')
            }

    def add_edge(self, u: str, v: str):
        # Sort node names to ensure the edge is undirected and unique
        edge = tuple(sorted([u, v]))
        self.edges.add(edge)

    def build_from_entry(self, entry_file_path: str):
        # Entry node name is the filename without .md extension
        entry_node_name = os.path.splitext(os.path.basename(entry_file_path))[0]
        
        # Queue for BFS traversal
        queue = [entry_node_name]
        visited = set()
        
        # Add the entry node itself
        self.add_node(entry_node_name, entry_file_path)

        while queue:
            current_node = queue.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            
            # Read current node file to find links
            node_info = self.nodes.get(current_node)
            if not node_info:
                continue
                
            file_path = node_info['file_path']
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
                
            links = extract_all_links(content)
            for target_node in links:
                # Resolve target node to file name in the vault
                target_file_name = target_node
                # Remove anchors if present in link (e.g. [[Node#Section]])
                if '#' in target_file_name:
                    target_file_name = target_file_name.split('#', 1)[0]
                
                # Check for standard markdown extension, or append if missing
                if not target_file_name.lower().endswith('.md'):
                    target_file_name += '.md'
                
                target_file_path = os.path.join(self.vault_dir, target_file_name)
                
                # If the markdown file exists in the vault, it represents a valid node
                if os.path.exists(target_file_path):
                    # Normalize node name by stripping .md from target if it had one
                    norm_target_node = os.path.splitext(os.path.basename(target_file_path))[0]
                    
                    self.add_node(norm_target_node, target_file_path)
                    self.add_edge(current_node, norm_target_node)
                    
                    if norm_target_node not in visited:
                        queue.append(norm_target_node)


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
                        # Extract the node label by removing trailing _X suffix
                        label = re.sub(r'_\d+$', '', base_name)
                        mapping[(label, src_file, loc)] = base_name
                except Exception:
                    pass
        return mapping

    def load_from_json(self, json_file_path: str):
        import json
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
            
            # Use label, src_file, and loc to uniquely identify in the vault
            vault_name = vault_map.get((label, src_file, loc))
            if vault_name:
                node_name = vault_name
            else:
                node_name = label
                
            id_to_name[node_id] = node_name
            
            if node_name not in self.nodes:
                self.nodes[node_name] = {
                    'label': node_name,
                    'file_path': os.path.join(self.vault_dir, node_name + ".md") if self.vault_dir else "",
                    'source_file': src_file,
                    'location': loc,
                    'type': file_type
                }
                
        for link in data.get('links', []):
            src_id = link.get('source')
            tgt_id = link.get('target')
            u = id_to_name.get(src_id)
            v = id_to_name.get(tgt_id)
            if u and v:
                self.add_edge(u, v)

    def calculate_degrees(self) -> dict:
        """
        Calculates the degree (connections) of each node.
        Returns a dict mapping node_name -> degree.
        """
        degrees = {node: 0 for node in self.nodes}
        for u, v in self.edges:
            if u in degrees:
                degrees[u] += 1
            if v in degrees:
                degrees[v] += 1
        return degrees
