# Codebase Architecture Analysis & Research Agent

This project contains a suite of static analysis tools and an autonomous agent to evaluate a codebase's dependency structure, identify key components, and detect common architectural design flaws.

## Features

1. **Centrality Analysis**: Measures degree centrality to identify highly connected nodes (God Classes/Monoliths).
2. **Hubs Detection**: Computes Betweenness Centrality using Brandes' algorithm to pinpoint critical architectural passage points and bottlenecks.
3. **Bridges Detection**: Identifies nodes linking separate functional communities/modules together.
4. **Architectural Bugs Detection**: Scans the codebase for five specific anti-patterns:
   - Synchronous Tight Coupling (Domino Effect risk)
   - "God Class" / Monolith patterns
   - Local State Dependency (Sticky Sessions)
   - Unbounded Retries (Thundering Herd retry storms)
   - Infinite Resource Waiting (missing request timeouts)

## Autonomous Research Agent (`run_agent.py`)

The `ResearchBugsAgent` is an autonomous workflow that automates the entire analysis pipeline:
- **Inbound Data Ingestion**: Parses the codebase graph (`graph.json`) and Obsidian index coordinates.
- **Metric Computation Nodes**: Sequentially executes the Degree Centrality, Betweenness Hubs, and Cross-Community Bridges analysis nodes.
- **Defect Evaluation Node**: Evaluates codebase heuristics to detect the five architectural anti-patterns.
- **Unified Reporting**: Generates a detailed findings summary file at `result/bugs_we_found.md`.

### Usage

Run the agent on a target graph schema:
```bash
./run_agent.py path/to/graphify-out/graph.json
```
