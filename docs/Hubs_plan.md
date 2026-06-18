# Implementation Plan - Hubs Analysis

## Phase 1: Setup
- [x] Initialize repository
- [x] Create base files
- [ ] Initialize hubs package files in src/ and tests/ directories

## Phase 2: Development
- [ ] **Graph JSON Loader:**
  - Parse `graph.json` format to load the nodes list and link list.
  - Build adjacency structure while preserving node metadata (`source_file`, `location`, `label`).
- [ ] **Betweenness Centrality Algorithm:**
  - Implement Brandes' algorithm for unweighted networks to compute betweenness centrality for all nodes in $O(V \cdot E)$ time.
  - Normalize centrality values.
- [ ] **Report Generator:**
  - Create function to format ranked nodes as markdown table in `Hubs.md`.
  - Filter out community and index/navigation nodes from the final report.
- [ ] **Command Line Interface:**
  - Create `hubs_analyzer.py` entry point script.

## Phase 3: Verification
- [ ] **Unit Testing:**
  - Verify Brandes' algorithm against standard network graphs (e.g., star graph where center is the hub, path graph where middle nodes have higher score).
- [ ] **Integration Testing:**
  - Run the tool on `data/BugsInPy/graphify-out/graph.json` and verify the output structure.
- [ ] **Repository Check:**
  - Request user review of the three documentation files (PRD, Plan, Todo) before making any commits.
