import argparse
import os
import sys
from .graph import KnowledgeGraph
from .reporter import generate_report

def main():
    parser = argparse.ArgumentParser(description="Analyze centrality in an Obsidian/Graphify vault.")
    parser.add_argument("entry_file", help="Path to the starting index markdown file (e.g., index.md or README.md)")
    parser.add_argument("-o", "--output", help="Path to save the output report (defaults to Centrality.md in the vault directory)")
    parser.add_argument("-p", "--project", help="Name of the project (default inferred from path)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.entry_file):
        print(f"Error: Entry file '{args.entry_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    vault_dir = os.path.dirname(os.path.abspath(args.entry_file))
    
    # If output is not specified, write to Centrality.md in the vault directory
    if args.output:
        output_path = args.output
    else:
        output_path = os.path.join(vault_dir, "Centrality.md")
        
    print(f"Initializing Knowledge Graph from vault directory: {vault_dir}")
    graph = KnowledgeGraph(vault_dir)
    
    print(f"Building graph starting from entry file: {args.entry_file}")
    graph.build_from_entry(args.entry_file)
    
    print(f"Found {len(graph.nodes)} nodes and {len(graph.edges)} unique edges.")
    print(f"Generating centrality report to: {output_path}")
    generate_report(graph, output_path, args.project)
    print("Done!")

if __name__ == "__main__":
    main()
