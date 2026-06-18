import re

def parse_frontmatter(content: str) -> dict:
    """
    Parses basic YAML frontmatter from markdown content.
    """
    metadata = {}
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                parts = line.split(':', 1)
                key = parts[0].strip()
                val = parts[1].strip().strip('"').strip("'")
                metadata[key] = val
    return metadata

def extract_wiki_links(content: str) -> list:
    """
    Extracts all wiki-links of the form [[Node Name]] from the content.
    """
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return [match.strip() for match in re.findall(pattern, content)]

def extract_markdown_links(content: str) -> list:
    """
    Extracts all relative internal markdown links.
    """
    pattern = r'\[[^\]]+\]\(([^)]+)\)'
    links = []
    for link in re.findall(pattern, content):
        link = link.strip()
        # Filter out external links or anchors
        if not (link.startswith('http://') or link.startswith('https://') or link.startswith('#') or link.startswith('mailto:')):
            links.append(link)
    return links

def extract_all_links(content: str) -> list:
    """
    Extracts and merges wiki-links and markdown links.
    """
    wiki = extract_wiki_links(content)
    markdown = extract_markdown_links(content)
    # Return unique values in order of appearance
    seen = set()
    result = []
    for item in (wiki + markdown):
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
