import os

def estimate_tokens(char_count):
    return char_count // 4

def run_simulation():
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    source_root = os.path.join(workspace_root, 'artifacts', 'broken-python')
    reports_dir = os.path.join(workspace_root, 'reports')
    
    # 1. Gather all files in the raw codebase (Bases for Naive)
    naive_files = []
    for root, _, files in os.walk(source_root):
        if 'graphify-out' in root or '.git' in root:
            continue
        for file in files:
            naive_files.append(os.path.join(root, file))
            
    # 2. Calculate Naive metrics
    naive_total_chars = 0
    naive_file_count = len(naive_files)
    for fpath in naive_files:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                naive_total_chars += len(f.read())
        except Exception:
            pass
            
    naive_tokens = estimate_tokens(naive_total_chars)
    # Overhead for 5 prompt-response iterations (conversational history accumulation)
    naive_overhead = 15000 * 5  
    naive_total_input_tokens = naive_tokens + naive_overhead
    
    # 3. Calculate Graph-Guided metrics
    guided_files = [
        os.path.join(reports_dir, 'index.md'),
        os.path.join(reports_dir, 'graph.json'),
        os.path.join(reports_dir, 'hot.md'),
        os.path.join(source_root, 'mathsquiz', 'mathsquiz.py'),
        os.path.join(source_root, 'polygons', 'polygons.py')
    ]
    
    guided_total_chars = 0
    guided_file_count = len(guided_files)
    for fpath in guided_files:
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                guided_total_chars += len(f.read())
        except Exception:
            pass
            
    guided_tokens = estimate_tokens(guided_total_chars)
    # Overhead for 2 prompt-response iterations (structured direct lookup)
    guided_overhead = 15000 * 2  
    guided_total_input_tokens = guided_tokens + guided_overhead
    
    # Print results
    print("# Token Efficiency Simulation Results")
    print("")
    print("| Metric | Naive (Baseline) | Graphify + Obsidian (Guided) | Savings (%) |")
    print("| :--- | :--- | :--- | :--- |")
    print(f"| **Context Footprint (Chars)** | {naive_total_chars:,} | {guided_total_chars:,} | {((naive_total_chars - guided_total_chars) / naive_total_chars * 100):.1f}% |")
    print(f"| **Estimated Input Tokens** | {naive_total_input_tokens:,} | {guided_total_input_tokens:,} | {((naive_total_input_tokens - guided_total_input_tokens) / naive_total_input_tokens * 100):.1f}% |")
    print(f"| **Files Scanned / Read** | {naive_file_count} | {guided_file_count} | {((naive_file_count - guided_file_count) / naive_file_count * 100):.1f}% |")
    print(f"| **Search Iterations** | 5 | 2 | 60.0% |")
    print(f"| **Estimated API Cost ($)** | ${naive_total_input_tokens * 0.000075 / 1000:.4f} | ${guided_total_input_tokens * 0.000075 / 1000:.4f} | {((naive_total_input_tokens - guided_total_input_tokens) / naive_total_input_tokens * 100):.1f}% |")

if __name__ == '__main__':
    run_simulation()
