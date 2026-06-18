# Implementation Plan

## Phase 1: Setup
- [x] Initialize repository
- [x] Create base files
- [x] Set up local python virtual environment
- [x] Initialize src/ and tests/ directory structures

## Phase 2: Development
- [x] **Markdown Link Extractor:**
  - Implement parsing for standard markdown links `[label](path)` and Obsidian wiki-links `[[NodeName]]`.
  - Resolve relative paths and link references to target files.
- [x] **Graph Construction & JSON Loader:**
  - Build a directed or undirected graph representation (adjacency list) of files and code artifacts from a starting `index.md` entry point.
  - Implement a JSON loader that parses `graph.json` directly, mapping AST node IDs to matching Obsidian note names using label and location tags to avoid name collisions.
  - Maintain mapping between node label and origin file path.
- [x] **Degree Centrality Calculation:**
  - Implement algorithm to compute degree centrality (incoming + outgoing connections) for each node.
  - Rank nodes in descending order of centrality degree.
- [x] **Report Generator:**
  - Create function to write `Centrality.md` listing the top central nodes in a markdown table format.
  - Formulate relative links back to origin vault files for each node.
  - Filter out metadata and community/navigation nodes.
- [x] **Command Line Interface:**
  - Build `centrality_analyzer.py` CLI script that accepts either `index.md` or `graph.json` as input.

## Phase 3: Verification
- [x] **Unit Testing:**
  - Test link extraction logic and JSON loader with various mock scenarios.
  - Test centrality calculation with simple mock graphs (star, line, ring topologies).
- [x] **Integration testing:**
  - Run the tool on `graph.json` and verify the generated `Centrality.md` matches the expected ranks and links.
- [ ] **Repository State Check:**
  - Verify all output documentation matches the user request.
  - Request user review of the three markdown files before any git commits or pushes.
