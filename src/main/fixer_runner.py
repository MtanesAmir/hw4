import os
import argparse
import sys

# Ensure flat sibling imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fixer.parser import parse_markdown_tables
from fixer.engine import refactor_file
from fixer.reporter import FixerReporter

def clean_file_path(path_str):
    if not path_str or path_str == 'N/A' or path_str == '-':
        return None
    import re
    link_match = re.match(r'^\[(.*?)\]\((.*?)\)$', path_str)
    if link_match:
        path_str = link_match.group(2)
    if path_str.startswith('[[') and path_str.endswith(']]'):
        path_str = path_str[2:-2]
    return path_str.strip()

def main():
    parser = argparse.ArgumentParser(description="Automated architectural bug fixer.")
    parser.add_argument("-b", "--bugs", default="reports/Bugs.md", help="Path to Bugs.md report")
    parser.add_argument("-s", "--suggestions", default="reports/Suggestions.md", help="Path to Suggestions.md report")
    parser.add_argument("-r", "--root", default="obsidian", help="Target project root directory containing source code")
    args = parser.parse_args()
    
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    
    bugs_path = os.path.abspath(os.path.join(workspace_root, args.bugs))
    suggestions_path = os.path.abspath(os.path.join(workspace_root, args.suggestions))
    project_root = os.path.abspath(os.path.join(workspace_root, args.root))
    
    report_path = os.path.join(workspace_root, "reports", "fixer_done.md")
    reporter = FixerReporter(report_path)
    
    bugs_raw = parse_markdown_tables(bugs_path)
    sugs_raw = parse_markdown_tables(suggestions_path)
    
    bugs_found_path = os.path.join(workspace_root, "reports", "bugs_we_found.md")
    bugs_found_raw = parse_markdown_tables(bugs_found_path) if os.path.exists(bugs_found_path) else []
    
    all_raw = bugs_raw + sugs_raw + bugs_found_raw
    
    processed = set()
    for row in all_raw:
        raw_file = row.get('Origin File') or row.get('file') or row.get('Violating Node') or row.get('Node')
        file_rel = clean_file_path(raw_file)
        if not file_rel:
            continue
            
        loc = row.get('Location') or 'L1'
        bug_type = row.get('Bug Type') or row.get('Defect Type') or row.get('Violation') or 'Architectural Defect'
        
        key = (file_rel, loc, bug_type)
        if key in processed:
            continue
        processed.add(key)
        
        target_file_path = os.path.join(project_root, file_rel)
        if not os.path.exists(target_file_path):
            found = False
            for root_dir, _, files in os.walk(project_root):
                for f in files:
                    if f == os.path.basename(file_rel):
                        target_file_path = os.path.join(root_dir, f)
                        found = True
                        break
                if found:
                    break
            if not found:
                reporter.add_task(file_rel, loc, bug_type, f"Failed: File not found under root {project_root}")
                continue
                
        try:
            with open(target_file_path, 'r', encoding='utf-8') as f:
                orig_content = f.read()
        except Exception as e:
            reporter.add_task(file_rel, loc, bug_type, f"Failed: Read error ({e})")
            continue
            
        success, res = refactor_file(target_file_path, bug_type)
        if success:
            with open(target_file_path, 'r', encoding='utf-8') as f:
                new_content = f.read()
            reporter.add_task(file_rel, loc, bug_type, "Success", orig_content, new_content)
            print(f"Successfully refactored {file_rel} for bug {bug_type}")
        else:
            reporter.add_task(file_rel, loc, bug_type, f"Skipped: {res}")
            
    reporter.write_report()

if __name__ == '__main__':
    main()
