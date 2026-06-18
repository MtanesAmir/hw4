import argparse
import os
import sys
from .parser import parse_bugs_report
from .reporter import generate_suggestions_report

def main():
    parser = argparse.ArgumentParser(description="Generate architectural improvements based on Bugs.md")
    parser.add_argument("bugs_md", help="Path to the Bugs.md report file")
    parser.add_argument("-o", "--output", help="Path to save the output report (defaults to Suggestions.md in the same folder)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.bugs_md):
        print(f"Error: Bugs.md file '{args.bugs_md}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    input_abs = os.path.abspath(args.bugs_md)
    input_dir = os.path.dirname(input_abs)
    
    # Resolve output path
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        output_path = os.path.join(input_dir, "Suggestions.md")
        
    print(f"Parsing Bugs report: {input_abs}")
    categories = parse_bugs_report(input_abs)
    
    total_violations = sum(len(vlist) for vlist in categories.values())
    print(f"Found {total_violations} violations across categories.")
    
    print(f"Generating suggestions report to: {output_path}")
    generate_suggestions_report(categories, output_path)
    print("Done!")

if __name__ == "__main__":
    main()
