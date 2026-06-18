def map_bugs_to_suggestions(categories):
    """
    Translates parsed categories of architectural bugs to a list of suggestions 
    mapped to the 10 Solution Architecture Principles.
    """
    suggestions = []
    
    # 1. Tight Coupling (The Domino Effect)
    if categories.get(1):
        for v in categories[1]:
            suggestions.append({
                'category': "Tight Coupling (The Domino Effect)",
                'node': v['node'],
                'file': v['file'],
                'location': v['location'],
                'principle': "Decoupling of Application Architecture",
                'description': "Decoupling components improves flexibility, scalability, and performance. This separation allows for independent updates, reducing the impact of failures.",
                'actionable_advice': f"Refactor [[{v['node']}]] to decouple direct synchronous dependencies. Integrate an asynchronous communication pattern like message queues or employ a Circuit Breaker wrapper to isolate faults."
            })
            
    # 2. The "God Class" / Monolith
    if categories.get(2):
        for v in categories[2]:
            suggestions.append({
                'category': "The \"God Class\" / Monolith",
                'node': v['node'],
                'file': v['file'],
                'location': v['location'],
                'principle': "Clear Components & Standardized Application Development",
                'description': "All components must have clear ownership and define responsibility. Standardizing application development reduces complexity, ensuring high cohesion.",
                'actionable_advice': f"Refactor [[{v['node']}]] to adhere to the Single Responsibility Principle. Break this monolith class down into smaller, domain-specific modules with clear interface boundaries."
            })
            
    # 3. Local State Dependency (Sticky Sessions)
    if categories.get(3):
        for v in categories[3]:
            suggestions.append({
                'category': "Local State Dependency (Sticky Sessions)",
                'node': v['node'],
                'file': v['file'],
                'location': v['location'],
                'principle': "Scalability of IT Solutions",
                'description': "IT solutions must be designed for horizontal scalability to accommodate growth. In-memory session state blocks horizontal scaling.",
                'actionable_advice': f"Make [[{v['node']}]] stateless. Decouple user session storage by persisting state into a distributed cache (e.g., Redis) or a central persistence layer."
            })
            
    # 4. Unbounded Retries (Thundering Herd)
    if categories.get(4):
        for v in categories[4]:
            suggestions.append({
                'category': "Unbounded Retries (Thundering Herd)",
                'node': v['node'],
                'file': v['file'],
                'location': v['location'],
                'principle': "Scalability of IT Solutions & Contextual Relevance",
                'description': "Resource capacity must be managed effectively. Unbounded retries cause thundering herd failures that overwhelm recovering services.",
                'actionable_advice': f"Modify retry logic in [[{v['node']}]] to implement exponential backoff algorithms and randomized delay jitter when attempting API connections."
            })
            
    # 5. Infinite Resource Waiting
    if categories.get(5):
        for v in categories[5]:
            suggestions.append({
                'category': "Infinite Resource Waiting",
                'node': v['node'],
                'file': v['file'],
                'location': v['location'],
                'principle': "Scalability of IT Solutions & Contextual Relevance",
                'description': "System capacity must be protected. Infinite wait states starve thread pools and freeze the calling service.",
                'actionable_advice': f"Enforce aggressive, bounded timeouts (e.g. timeout=5.0) and fallbacks on all network/API requests in [[{v['node']}]]."
            })
            
    return suggestions
