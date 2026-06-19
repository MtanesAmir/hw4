import os
import re

def parse_markdown_tables(file_path):
    """
    Parses Markdown tables in a file and returns rows as dictionaries.
    Automatically resolves markdown links [label](target) to target.
    """
    if not os.path.exists(file_path):
        return []
        
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    results = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('|'):
            headers = [h.strip() for h in line.split('|')[1:-1]]
            i += 1
            if i >= len(lines):
                break
            sep_line = lines[i].strip()
            if not sep_line.startswith('|') or '-' not in sep_line:
                i += 1
                continue
            i += 1
            while i < len(lines) and lines[i].strip().startswith('|'):
                row_cells = [c.strip() for c in lines[i].strip().split('|')[1:-1]]
                row_dict = dict(zip(headers, row_cells))
                
                for k, v in row_dict.items():
                    link_match = re.match(r'^\[(.*?)\]\((.*?)\)$', v)
                    if link_match:
                        row_dict[k] = link_match.group(2)
                        
                is_valid = True
                for val in row_dict.values():
                    clean_val = val.strip().lower()
                    if val.strip() == '-' or clean_val in (
                        'none', 
                        'all checks passed.', 
                        'all checks clean. no improvements required.',
                        'all checks clean'
                    ):
                        is_valid = False
                        break
                if is_valid and row_dict:
                    results.append(row_dict)
                i += 1
        else:
            i += 1
    return results
