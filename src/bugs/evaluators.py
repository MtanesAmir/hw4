import os
import re

def check_tight_coupling(graph):
    """
    Identifies nodes with high ratio of cross-community connections.
    """
    violations = []
    for node_name, node_info in graph.nodes.items():
        if node_name.startswith('_COMMUNITY_') or node_info.get('type') == 'community':
            continue
        my_comm = node_info.get('community')
        if my_comm is None:
            continue
            
        neighbors = graph.adjacency.get(node_name, [])
        if not neighbors:
            continue
            
        cross_comm_count = 0
        for neighbor in neighbors:
            neighbor_info = graph.nodes.get(neighbor)
            if neighbor_info:
                n_comm = neighbor_info.get('community')
                if n_comm is not None and n_comm != my_comm:
                    cross_comm_count += 1
                    
        # If more than 50% of connections go to other communities, it is a tight coupling risk
        ratio = cross_comm_count / len(neighbors)
        if cross_comm_count >= 2 and ratio > 0.5:
            violations.append({
                'node': node_name,
                'file': node_info.get('source_file', 'N/A'),
                'location': node_info.get('location', 'N/A'),
                'details': f"Coupling ratio: {ratio:.2f} ({cross_comm_count}/{len(neighbors)} links lead to external communities)",
                'fix': "Implement asynchronous communication via message queues (e.g., RabbitMQ) or isolate dependencies with Circuit Breakers."
            })
    return violations

def check_god_class(graph, threshold=8):
    """
    Identifies God Classes/Monoliths based on node degree.
    """
    violations = []
    for node_name, node_info in graph.nodes.items():
        if node_name.startswith('_COMMUNITY_') or node_info.get('type') == 'community':
            continue
        degree = len(graph.adjacency.get(node_name, []))
        if degree >= threshold:
            violations.append({
                'node': node_name,
                'file': node_info.get('source_file', 'N/A'),
                'location': node_info.get('location', 'N/A'),
                'details': f"Class/module degree: {degree} (exceeds threshold of {threshold})",
                'fix': "Adhere to the Single Responsibility Principle; split functionality into discrete, domain-specific modules."
            })
    return violations

def analyze_file_content(file_path):
    """
    Helper to safely read file content.
    """
    if not file_path or file_path == 'N/A' or not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception:
        return None

def check_local_state_dependency(graph, project_root):
    """
    Scans files for local memory session stores without distributed persistence.
    """
    violations = []
    seen_files = set()
    for node_name, node_info in graph.nodes.items():
        src_file = node_info.get('source_file')
        if not src_file or src_file == 'N/A':
            continue
            
        full_path = os.path.join(project_root, src_file)
        if full_path in seen_files:
            continue
        seen_files.add(full_path)
        
        content = analyze_file_content(full_path)
        if content is None:
            continue
            
        # Detect local session dict or state storage
        has_local_session = re.search(r'\bsession\s*=\s*\{\s*\}|\bself\.session\s*=\s*\{\s*\}', content)
        has_sticky_session = re.search(r'\bsticky\b', content, re.IGNORECASE)
        
        # Detect distributed store libraries
        has_distributed_store = re.search(r'\b(redis|memcache|pymemcache|database|session_store)\b', content, re.IGNORECASE)
        
        if (has_local_session or has_sticky_session) and not has_distributed_store:
            violations.append({
                'node': node_name,
                'file': src_file,
                'location': node_info.get('location', 'L1'),
                'details': "Uses in-memory session/state storage without importing Redis or memcached.",
                'fix': "Decouple session state into a distributed cache (e.g., Redis) or central persistence layer."
            })
    return violations

def check_unbounded_retries(graph, project_root):
    """
    Checks for automated retry mechanisms lacking exponential backoff or jitter.
    """
    violations = []
    seen_files = set()
    for node_name, node_info in graph.nodes.items():
        src_file = node_info.get('source_file')
        if not src_file or src_file == 'N/A':
            continue
            
        full_path = os.path.join(project_root, src_file)
        if full_path in seen_files:
            continue
        seen_files.add(full_path)
        
        content = analyze_file_content(full_path)
        if content is None:
            continue
            
        # Search for retry loop or function calls
        retry_matches = list(re.finditer(r'\bretry\b|\bretrying\b', content, re.IGNORECASE))
        if retry_matches:
            # Check if retry includes backoff/jitter/random delays
            has_backoff = re.search(r'\b(backoff|exponential|jitter|random|sleep\(\s*\d+\s*\*\s*\d+)\b', content, re.IGNORECASE)
            if not has_backoff:
                # Find line number of the first retry keyword match
                match_index = retry_matches[0].start()
                line_no = content[:match_index].count('\n') + 1
                violations.append({
                    'node': node_name,
                    'file': src_file,
                    'location': f"L{line_no}",
                    'details': "Automated retry mechanism detected without exponential backoff or jitter delay.",
                    'fix': "Implement exponential backoff and randomized delays (jitter) to prevent thundering herd failures."
                })
    return violations

def check_infinite_waiting(graph, project_root):
    """
    Detects network requests (requests.get/post) that miss the timeout argument.
    """
    violations = []
    seen_files = set()
    for node_name, node_info in graph.nodes.items():
        src_file = node_info.get('source_file')
        if not src_file or src_file == 'N/A':
            continue
            
        full_path = os.path.join(project_root, src_file)
        if full_path in seen_files:
            continue
        seen_files.add(full_path)
        
        content = analyze_file_content(full_path)
        if content is None:
            continue
            
        # Search for HTTP calls: requests.get, requests.post, requests.delete, requests.put, requests.patch, requests.request
        http_matches = re.finditer(r'\brequests\.(get|post|delete|put|patch|request)\s*\(', content)
        for match in http_matches:
            start_pos = match.end()
            # Extract arguments by balancing parentheses
            paren_count = 1
            args_str = ""
            for char in content[start_pos:]:
                if char == '(':
                    paren_count += 1
                elif char == ')':
                    paren_count -= 1
                    if paren_count == 0:
                        break
                args_str += char
                
            if 'timeout' not in args_str:
                line_no = content[:match.start()].count('\n') + 1
                violations.append({
                    'node': node_name,
                    'file': src_file,
                    'location': f"L{line_no}",
                    'details': f"Unsafe network request: '{match.group(0)}...' missing explicit timeout parameter.",
                    'fix': "Always enforce bounded timeouts (e.g., timeout=5) for network or database requests."
                })
    return violations
