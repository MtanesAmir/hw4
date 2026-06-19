import argparse
import os
import sys
from .graph_loader import BugsGraph
from .reporter import generate_bugs_report

def main():
    parser = argparse.ArgumentParser(description="Analyze architectural bugs/smells in code & configuration.")
    parser.add_argument("graph_json", help="Path to the graph.json file")
    parser.add_argument("-o", "--output", help="Path to save the output report (defaults to Bugs.md)")
    parser.add_argument("-v", "--vault", help="Path to the Obsidian vault directory (default inferred from graph_json)")
    parser.add_argument("-r", "--root", help="Project root directory for scanning source code (default workspace root)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.graph_json):
        print(f"Error: graph.json file '{args.graph_json}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    input_abs = os.path.abspath(args.graph_json)
    input_dir = os.path.dirname(input_abs)
    
    # Resolve vault directory
    if args.vault:
        vault_dir = os.path.abspath(args.vault)
    else:
        obsidian_dir = os.path.join(input_dir, 'obsidian')
        if os.path.exists(obsidian_dir) and os.path.isdir(obsidian_dir):
            vault_dir = obsidian_dir
        else:
            vault_dir = input_dir
            
    # Resolve project root
    if args.root:
        project_root = os.path.abspath(args.root)
    else:
        # Find directory matching BugsInPy
        current = input_dir
        while current and os.path.basename(current) not in ('BugsInPy', 'hw4') and os.path.dirname(current) != current:
            current = os.path.dirname(current)
        if current and os.path.basename(current) == 'BugsInPy':
            project_root = current
        else:
            project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
            
    # Resolve output path
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        proj_root_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
        reports_dir = os.path.join(proj_root_dir, 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        output_path = os.path.join(reports_dir, "Bugs.md")
        
    print(f"Initializing Bugs Graph with vault: {vault_dir}")
    graph = BugsGraph(vault_dir)
    
    print(f"Loading graph: {input_abs}")
    graph.load_from_json(input_abs)
    
    print(f"Project scanning root: {project_root}")
    print(f"Generating architectural bugs report to: {output_path}")
    generate_bugs_report(graph, output_path, project_root)
    print("Done!")

if __name__ == "__main__":
    main()
