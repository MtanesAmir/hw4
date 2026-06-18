import os
from .analyzer import calculate_betweenness_centrality

def generate_hubs_report(graph, output_path: str, project_name: str = None):
    """
    Generates the Hubs.md report listing ranked bottleneck nodes.
    """
    if not project_name:
        vault_name = os.path.basename(os.path.abspath(graph.vault_dir))
        if vault_name.lower() in ('obsidian', 'graphify-out') and os.path.dirname(graph.vault_dir):
            parent = os.path.basename(os.path.dirname(os.path.abspath(graph.vault_dir)))
            if parent.lower() == 'graphify-out':
                grandparent = os.path.dirname(os.path.dirname(os.path.abspath(graph.vault_dir)))
                project_name = os.path.basename(grandparent)
            else:
                project_name = parent
        else:
            project_name = vault_name
            
    cb = calculate_betweenness_centrality(graph)
    sorted_nodes = sorted(cb.items(), key=lambda x: x[1], reverse=True)
    
    lines = [
        "# Hubs (Subject 10)",
        "",
        "According to subject 10 of the Lecture Summary, **Hubs** represent bottleneck nodes in the codebase architecture. All information flows through these nodes. Although they may have few direct outgoing transitions, they are critical passage points and represent significant architectural dependencies.",
        "",
        f"## Top Hubs in {project_name}",
        "",
        "| Rank | Hub Node | Betweenness Score | Origin File | Location |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    
    rank = 1
    for node_name, score in sorted_nodes:
        node_info = graph.nodes[node_name]
        
        # Skip community/navigation metadata nodes
        if node_name.startswith('_COMMUNITY_') or node_name.lower() in ('index', 'graph_report'):
            continue
        if node_info.get('type') == 'community':
            continue
            
        src_file = node_info.get('source_file', 'N/A')
        loc = node_info.get('location', 'N/A')
        
        if src_file and src_file != 'N/A':
            origin_link = f"[{src_file}]({src_file})"
        else:
            origin_link = "N/A"
            
        # Format score to 3 decimal places
        formatted_score = f"{score:.3f}"
        
        lines.append(f"| {rank} | [[{node_name}]] | {formatted_score} | {origin_link} | {loc} |")
        rank += 1
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
