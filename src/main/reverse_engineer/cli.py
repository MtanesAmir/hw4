import argparse
import os
import sys
from .ast_scanner import ASTScanner
from .reporter import write_reverse_engineer_report

def main():
    parser = argparse.ArgumentParser(description="Run the ReverseEngineeringAgent on a package.")
    parser.add_argument("source_dir", help="Path to the python package or src directory to analyze")
    parser.add_argument("-o", "--output", help="Path to save the output report (defaults to reverse_engineer_agent_result.md in result/)")
    parser.add_argument("-r", "--root", help="Project root directory for storing output (default workspace root)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.source_dir):
        print(f"Error: source directory '{args.source_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    src_abs = os.path.abspath(args.source_dir)
    
    if args.root:
        project_root = os.path.abspath(args.root)
    else:
        project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
        
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        reports_dir = os.path.join(project_root, 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        output_path = os.path.join(reports_dir, "reverse_engineer_agent_result.md")
        
    print(f"Initializing AST Scanner for directory: {src_abs}")
    scanner = ASTScanner(src_abs)
    
    print("Scanning source code files...")
    scanner.scan()
    
    print(f"Found {len(scanner.modules)} modules and {len(scanner.classes)} classes.")
    print(f"Generating reverse engineering report to: {output_path}")
    write_reverse_engineer_report(scanner, output_path)
    print("Done!")

if __name__ == "__main__":
    main()
