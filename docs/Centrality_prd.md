# Product Requirements Document (PRD)

## Overview
The Centrality Analysis Tool is designed to analyze the connectivity of nodes (Markdown files and code artifacts) within a knowledge graph or Obsidian vault. By computing centrality metrics for each node, the tool identifies key hubs ("God Nodes" or "leaders" in the graph), helping developers understand the system architecture, find critical entry points, and locate potential single points of failure.

## Objectives
- Implement a centrality calculation mechanism based on Graph Theory (specifically Degree Centrality) as described in Subject 8 of Lecture 07.
- Parse a given `index.md` file (which serves as the entry point listing/linking other nodes) or an Obsidian vault to construct a graph of notes and code symbols.
- Generate a ranked summary report (`Centrality.md`) listing the central nodes, their connectivity count (degree), and clickable relative links to their origin files in the vault.

## Requirements
1. **Input Parser:**
   - The tool must accept a starting markdown file, typically `index.md`, representing the entry point of the vault.
   - It must recursively parse internal links (e.g., wiki-links like `[[Node]]` or markdown links) from the input file and its dependents to construct a node-link graph structure.
2. **Centrality Computation:**
   - Calculate the **Degree Centrality** (total number of incoming and outgoing links/edges) for each resolved node.
   - Rank all nodes in descending order based on their connectivity degree.
3. **Output Document (`Centrality.md`):**
   - Automatically write a new Markdown file named `Centrality.md` in the target vault directory.
   - The file must contain a table with the following columns:
     - **Rank**: Numeric ranking of centrality.
     - **Central Node**: The name of the node, formatted as a wiki-link (e.g., `[[Node Name]]`).
     - **Connections (Degree)**: The total connection count.
     - **Origin File**: A relative link to the source file (e.g., `[README.md](README.md)` or `[verify.sh](projects/ansible/verify.sh)`).
     - **Location/Context**: Additional metadata indicating specific functions or line context (e.g., line numbers or N/A).
4. **Constraints:**
   - Adhere to the graph-guided analysis concepts specified in L07-Lesson-Summary.pdf.
   - Do not commit or push changes to the repository before all three documentation files (PRD, Plan, and Todo) are reviewed by the user.
