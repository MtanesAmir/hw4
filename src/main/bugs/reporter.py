import os
from .evaluators import (
    check_tight_coupling,
    check_god_class,
    check_local_state_dependency,
    check_unbounded_retries,
    check_infinite_waiting
)

def generate_bugs_report(graph, output_path: str, project_root: str):
    """
    Evaluates rules and generates the architectural bugs report.
    """
    tc_violations = check_tight_coupling(graph)
    gc_violations = check_god_class(graph)
    ls_violations = check_local_state_dependency(graph, project_root)
    ur_violations = check_unbounded_retries(graph, project_root)
    iw_violations = check_infinite_waiting(graph, project_root)
    
    lines = [
        "# Architectural Bugs Report",
        "",
        "This report summarizes critical architectural anti-patterns and defects detected in the codebase representation.",
        ""
    ]
    
    sections = [
        ("1. Tight Coupling (The Domino Effect)", tc_violations),
        ("2. The \"God Class\" / Monolith", gc_violations),
        ("3. Local State Dependency (Sticky Sessions)", ls_violations),
        ("4. Unbounded Retries (Thundering Herd)", ur_violations),
        ("5. Infinite Resource Waiting", iw_violations),
    ]
    
    for title, violations in sections:
        lines.append(f"## {title}")
        lines.append("")
        if not violations:
            lines.append("No violations detected in this category.")
            lines.append("")
            continue
            
        lines.append("| Node | Origin File | Location | Details | Fix Recommendation |")
        lines.append("| :--- | :--- | :--- | :--- | :--- |")
        
        for v in violations:
            node_name = v['node']
            src_file = v['file']
            loc = v['location']
            details = v['details']
            fix = v['fix']
            
            if src_file and src_file != 'N/A':
                origin_link = f"[{src_file}]({src_file})"
            else:
                origin_link = "N/A"
                
            lines.append(f"| [[{node_name}]] | {origin_link} | {loc} | {details} | {fix} |")
        lines.append("")
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
