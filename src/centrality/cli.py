import argparse
import os
import sys
from .graph import KnowledgeGraph
from .reporter import generate_report

def main():
    parser = argparse.ArgumentParser(description="Analyze centrality in an Obsidian/Graphify vault.")
    parser.add_argument("input_file", help="Path to the starting markdown file (e.g., index.md) or graph.json file")
    parser.add_argument("-o", "--output", help="Path to save the output report (defaults to Centrality.md)")
    parser.add_argument("-v", "--vault", help="Path to the Obsidian vault directory (default inferred from input path)")
    parser.add_argument("-p", "--project", help="Name of the project (default inferred from path)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    input_abs = os.path.abspath(args.input_file)
    input_dir = os.path.dirname(input_abs)
    
    # Resolve vault directory
    if args.vault:
        vault_dir = os.path.abspath(args.vault)
    else:
        if args.input_file.lower().endswith('.json'):
            # If graph.json is in graphify-out/, check for graphify-out/obsidian/
            obsidian_dir = os.path.join(input_dir, 'obsidian')
            if os.path.exists(obsidian_dir) and os.path.isdir(obsidian_dir):
                vault_dir = obsidian_dir
            else:
                vault_dir = input_dir
        else:
            vault_dir = input_dir
            
    # Resolve output path
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        output_path = os.path.join(vault_dir, "Centrality.md")
        
    print(f"Initializing Knowledge Graph with vault directory: {vault_dir}")
    graph = KnowledgeGraph(vault_dir)
    
    if args.input_file.lower().endswith('.json'):
        print(f"Loading graph from JSON: {input_abs}")
        graph.load_from_json(input_abs)
    else:
        print(f"Building graph starting from entry file: {input_abs}")
        graph.build_from_entry(input_abs)
        
    print(f"Found {len(graph.nodes)} nodes and {len(graph.edges)} unique edges.")
    print(f"Generating centrality report to: {output_path}")
    generate_report(graph, output_path, args.project)
    print("Done!")

if __name__ == "__main__":
    main()
