import os
from .mapper import map_bugs_to_suggestions

def generate_suggestions_report(parsed_categories, output_path: str):
    """
    Builds the Suggestions.md report table mapping defects to Solution Architecture Principles.
    """
    suggestions = map_bugs_to_suggestions(parsed_categories)
    
    lines = [
        "# Architectural Improvement Suggestions",
        "",
        "Based on the architectural defects parsed from `Bugs.md`, the following improvements are recommended in accordance with the **10 Solution Architecture Principles**.",
        "",
        "## Top Recommended Improvements",
        "",
        "| Rank | Violating Node | Origin File | Location | Defect Type | Solution Architecture Principle | Actionable Suggestion |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
    ]
    
    if not suggestions:
        lines.append("| - | None | - | - | - | - | All checks clean. No improvements required. |")
    else:
        for idx, sug in enumerate(suggestions, 1):
            node_name = sug['node']
            src_file = sug['file']
            loc = sug['location']
            defect_type = sug['category']
            principle = sug['principle']
            advice = sug['actionable_advice']
            
            if src_file and src_file != 'N/A':
                origin_link = f"[{src_file}]({src_file})"
            else:
                origin_link = "N/A"
                
            lines.append(f"| {idx} | [[{node_name}]] | {origin_link} | {loc} | {defect_type} | {principle} | {advice} |")
            
    lines.append("")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
