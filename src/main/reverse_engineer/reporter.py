import os
from .mapper import generate_block_diagram, generate_oop_diagram

def write_reverse_engineer_report(scanner, output_path: str):
    """
    Assembles the block diagram, OOP schema, and textual descriptions into a markdown report.
    """
    block_mermaid = generate_block_diagram(scanner.modules)
    oop_mermaid = generate_oop_diagram(scanner.classes)
    
    lines = [
        "This file was written by the Agent.",
        "",
        "# Codebase Reverse Engineering Report",
        "",
        "This report contains structural and object-oriented analysis of the software codebase, generated autonomously by the `ReverseEngineeringAgent`.",
        "",
        "## 1. Architectural Block Diagram",
        "The following diagram illustrates the information and dependency flow between the top-level modules in the codebase:",
        "",
        "```mermaid",
        block_mermaid,
        "```",
        "",
        "### Block Explanation",
        "The system is organized into decoupled subpackages, each handling distinct analysis concerns:"
    ]
    
    pkg_explanations = {
        'centrality': "The **Centrality Package** parses graph linkages and computes Degree Centrality, flagging highly coupled 'God Node' candidates.",
        'hubs': "The **Hubs Package** implements Brandes' algorithm to compute Betweenness Centrality, identifying bottleneck nodes through which major architectural dependencies pass.",
        'bugs': "The **Bugs Package** scans configuration patterns and source file definitions to flag five critical architectural bugs/anti-patterns.",
        'suggestions': "The **Suggestions Package** maps discovered bugs to the 10 Solution Architecture Principles, formulating concrete refactoring recommendations.",
        'agent': "The **Agent Package** orchestrates the complete analysis pipeline using a LangGraph-style State/Node state machine.",
        'reverse_engineer': "The **Reverse Engineer Package** walks Abstract Syntax Trees (AST) to generate architectural and class diagrams."
    }
    
    seen_pkgs = set()
    for mod_name in scanner.modules.keys():
        pkg = mod_name.split('.')[0]
        seen_pkgs.add(pkg)
        
    for pkg in sorted(list(seen_pkgs)):
        explanation = pkg_explanations.get(pkg, f"The **{pkg.capitalize()} Package** is a functional sub-module in the application codebase.")
        lines.append(f"- **{pkg.replace('_', ' ').capitalize()}**: {explanation}")
        
    lines.extend([
        "",
        "## 2. Object-Oriented (OOP) Class Schema",
        "The following class diagram defines class interfaces, inheritance lines, and composition boundaries detected in the codebase:",
        "",
        "```mermaid",
        oop_mermaid,
        "```",
        "",
        "### Class Relationships and Explanations"
    ])
    
    if not scanner.classes:
        lines.append("No class definitions found in the scanned codebase.")
    else:
        for class_name, info in sorted(scanner.classes.items()):
            lines.append(f"#### Class: `{class_name}`")
            lines.append(f"- **Module**: `{info['module']}`")
            
            if info['bases']:
                bases_str = ", ".join(f"`{b}`" for b in info['bases'])
                lines.append(f"- **Inherits From**: {bases_str}")
            else:
                lines.append("- **Inherits From**: None (Base class)")
                
            if info['compositions']:
                comps_str = ", ".join(f"`{c}`" for c in info['compositions'])
                lines.append(f"- **Composes (Instantiates)**: {comps_str}")
            else:
                lines.append("- **Composes**: None")
                
            clean_methods = [m for m in info['methods'] if not m.startswith('__')]
            if clean_methods:
                meth_str = ", ".join(f"`{m}()`" for m in clean_methods)
                lines.append(f"- **Methods**: {meth_str}")
            lines.append("")
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
