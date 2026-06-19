# Product Requirements Document (PRD) - Research Bugs Agent

## Overview
The Research Bugs Agent is an autonomous codebase architect orchestrator built using LangGraph or CrewAI. Its job is to automate the structural analysis and architectural bug detection process. By parsing codebase graph schemas and orchestrating centrality, hubs, and bridges calculators, the agent evaluates system coupling and anti-patterns, generating a unified report detailing its findings.

## Objectives
- Implement an agentic workflow using LangGraph or CrewAI.
- Orchestrate the existing analysis modules:
  - **Degree Centrality** (central files/nodes).
  - **Hubs** (betweenness/bottleneck nodes).
  - **Bridges** (inter-community connectors).
  - **Bugs Scanner** (the 5 architectural anti-patterns).
- Automatically compile results and write them to `result/bugs_we_found.md`.
- Document the agent's operation and architecture in the project's root `README.md`.

## Requirements
1. **Agent Framework:**
   - Implement the agent using either LangGraph or CrewAI.
   - The agent must coordinate task execution state, running analysis steps sequentially or in parallel, and handling errors gracefully.
2. **Analysis Pipeline Execution:**
   - Ingest files from the target Obsidian vault directory, specifically `index.md` and `graph.json`.
   - Execute the centrality, hubs, and bridges calculation engines to measure node metrics.
   - Run the bugs evaluation scanner on the codebase using the calculated graph metrics to locate architectural defects.
3. **Unified Report (`result/bugs_we_found.md`):**
   - Create the directory `result/` if it does not exist.
   - Generate `result/bugs_we_found.md`.
   - The file MUST begin with a header/disclaimer: `"This file was written by the Agent."`
   - It must compile:
     - The top centrality nodes.
     - The top hubs (bottlenecks).
     - The top bridge nodes (cross-community linkages).
     - Full descriptions of all detected architectural bugs (anti-patterns) with explanations and suggested remediations.
4. **README Documentation:**
   - The task list must include updating the root `README.md` file to describe:
     - The role and tasks of the `ResearchBugsAgent`.
     - Setup instructions and execution commands to run the agent.
5. **Constraints:**
   - Do not commit or push changes to the repository before all three documentation files (PRD, Plan, and Todo) are reviewed by the user.
