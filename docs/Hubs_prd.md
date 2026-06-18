# Product Requirements Document (PRD) - Hubs Analysis

## Overview
The Hubs Analysis Tool is designed to identify bottleneck nodes within a knowledge graph or codebase architecture. Based on Subject 10 of the Lecture 07 summary, a Hub (or bottleneck) is a critical node through which a significant portion of information flows. Identifying these nodes helps developers detect critical architectural dependencies and single points of failure.

## Objectives
- Implement a Hub identification mechanism based on Betweenness Centrality (as described in Subject 10 of Lecture 07).
- Parse the codebase graph representation from a `graph.json` file (node-link format) containing nodes and edges.
- Generate a ranked summary report (`Hubs.md`) listing the top Hub nodes, their calculated betweenness scores, and relative links back to their origin files in the vault.

## Requirements
1. **Input Parser:**
   - The tool must accept a `graph.json` file as input.
   - It must parse the `"nodes"` and `"links"` lists to construct an internal graph representation.
2. **Hub Centrality Computation:**
   - Implement an algorithm (e.g., Brandes' algorithm for unweighted graphs) to calculate **Betweenness Centrality** for all nodes.
   - Nodes with high betweenness centrality values represent the bottlenecks/hubs.
   - Rank the nodes in descending order of their betweenness centrality.
3. **Output Document (`Hubs.md`):**
   - Automatically write a new Markdown file named `Hubs.md` in the target vault directory.
   - The file must contain a table with the following columns:
     - **Rank**: Numeric ranking of betweenness centrality.
     - **Hub Node**: The name of the node, formatted as a wiki-link (e.g., `[[Node Name]]`).
     - **Betweenness Score**: The calculated centrality score (normalized or raw).
     - **Origin File**: A relative link to the source file (e.g., `[README.md](README.md)`).
     - **Location/Context**: Line numbers or context metadata (e.g., `L1` or `N/A`).
4. **Constraints:**
   - Adhere to the architectural definitions specified in Subject 10 of L07-Lesson-Summary.pdf.
   - Do not commit or push changes to the repository before all three documentation files (PRD, Plan, and Todo) are reviewed by the user.
