import os

def generate_report(graph, output_path: str, project_name: str = None):
    """
    Generates the Centrality.md report based on the computed graph degrees.
    """
    if not project_name:
        # Infer project name from vault directory name or parent
        vault_name = os.path.basename(os.path.abspath(graph.vault_dir))
        if vault_name.lower() in ('obsidian', 'graphify-out') and os.path.dirname(graph.vault_dir):
            parent = os.path.basename(os.path.dirname(os.path.abspath(graph.vault_dir)))
            if parent.lower() == 'graphify-out':
                # Go up one more level
                grandparent = os.path.dirname(os.path.dirname(os.path.abspath(graph.vault_dir)))
                project_name = os.path.basename(grandparent)
            else:
                project_name = parent
        else:
            project_name = vault_name
            
    # Calculate degrees and sort nodes
    degrees = graph.calculate_degrees()
    sorted_nodes = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
    
    lines = [
        "# Centrality (Subject 8)",
        "",
        "According to subject 8 of the Lecture Summary, **Centrality** represents nodes with high connectivity (God Nodes). These nodes have a high number of incoming and outgoing relationships, serving as key hubs in the codebase architecture.",
        "",
        f"## Central Nodes in {project_name}",
        "",
        "| Rank | Central Node | Connections (Degree) | Origin File | Location |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    
    rank = 1
    for node_name, degree in sorted_nodes:
        node_info = graph.nodes[node_name]
        
        # Skip community/navigation metadata nodes
        if node_name.startswith('_COMMUNITY_') or node_name.lower() in ('index', 'graph_report'):
            continue
        if node_info.get('type') == 'community':
            continue
            
        src_file = node_info.get('source_file', 'N/A')
        loc = node_info.get('location', 'N/A')
        
        # Format Origin File as markdown link if not N/A
        if src_file and src_file != 'N/A':
            origin_link = f"[{src_file}]({src_file})"
        else:
            origin_link = "N/A"
            
        lines.append(f"| {rank} | [[{node_name}]] | {degree} | {origin_link} | {loc} |")
        rank += 1
        
    # Write report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
