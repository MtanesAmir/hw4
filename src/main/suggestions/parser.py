import os
import re

def parse_bugs_report(bugs_md_path: str):
    """
    Parses the Bugs.md report and returns a dict mapping bug categories (1-5) to a list of violations.
    Categories:
      1: Tight Coupling (The Domino Effect)
      2: The "God Class" / Monolith
      3: Local State Dependency (Sticky Sessions)
      4: Unbounded Retries (Thundering Herd)
      5: Infinite Resource Waiting
    """
    if not os.path.exists(bugs_md_path):
        return {}
        
    with open(bugs_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    
    categories = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    
    current_category = None
    category_regex = re.compile(r'^##\s*(\d+)\.')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        cat_match = category_regex.match(line)
        if cat_match:
            current_category = int(cat_match.group(1))
            continue
            
        if current_category and line.startswith('|') and not line.startswith('| :---') and not line.startswith('| Node |'):
            # Parse table row
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 6:
                node_raw = parts[1]
                node_match = re.search(r'\[\[(.*?)\]\]', node_raw)
                node_name = node_match.group(1) if node_match else node_raw
                
                file_raw = parts[2]
                file_match = re.search(r'\[(.*?)\]\((.*?)\)', file_raw)
                file_name = file_match.group(1) if file_match else file_raw
                
                loc = parts[3]
                details = parts[4]
                fix = parts[5]
                
                categories[current_category].append({
                    'node': node_name,
                    'file': file_name,
                    'location': loc,
                    'details': details,
                    'fix': fix
                })
                
    return categories
