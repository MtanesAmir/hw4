import argparse
import os
import sys
from .graph import HubsGraph
from .reporter import generate_hubs_report

def main():
    parser = argparse.ArgumentParser(description="Analyze hubs/bottlenecks in an Obsidian/Graphify vault.")
    parser.add_argument("graph_json", help="Path to the graph.json file")
    parser.add_argument("-o", "--output", help="Path to save the output report (defaults to Hubs.md)")
    parser.add_argument("-v", "--vault", help="Path to the Obsidian vault directory (default inferred from graph_json path)")
    parser.add_argument("-p", "--project", help="Name of the project (default inferred from path)")
    
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
            
    # Resolve output path
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
        reports_dir = os.path.join(project_root, 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        output_path = os.path.join(reports_dir, "Hubs.md")
        
    print(f"Initializing Hubs Graph with vault directory: {vault_dir}")
    graph = HubsGraph(vault_dir)
    
    print(f"Loading graph from JSON: {input_abs}")
    graph.load_from_json(input_abs)
    
    print(f"Found {len(graph.nodes)} nodes and calculated relationships.")
    print(f"Generating hubs report to: {output_path}")
    generate_hubs_report(graph, output_path, args.project)
    print("Done!")

if __name__ == "__main__":
    main()
