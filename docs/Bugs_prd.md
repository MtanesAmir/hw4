# Product Requirements Document (PRD) - Architectural Bugs Detection

## Overview
This document outlines the product requirements for an Architectural Bugs Detection system. The system analyzes a codebase representation (e.g., knowledge graph, configuration, or AST) to detect five common architectural anti-patterns ("bad bugs") that degrade reliability, scalability, and maintainability.

## Objectives
- Detect five specific architectural defects in a software system:
  1. **Tight Coupling (The Domino Effect)**
  2. **The "God Class" / Monolith**
  3. **Local State Dependency (Sticky Sessions)**
  4. **Unbounded Retries (Thundering Herd)**
  5. **Infinite Resource Waiting**
- Provide automated recommendations and remediation patterns (fixes) for each detected defect.
- Generate a summary report highlighting the location of these issues within the analyzed codebase/graph.

## Requirements
1. **Defect Detectors:**
   - **Tight Coupling Detector:**
     - Identify synchronous, real-time dependencies between independent modules or microservices.
     - Highlight potential cascading failure paths where a crash in one dependency blocks/exhausts the caller.
   - **God Class / Monolith Detector:**
     - Identify classes or modules with low cohesion and high coupling (e.g., nodes in the graph with exceptionally high degree centrality that bridge unrelated functional domains).
   - **Local State Dependency Detector:**
     - Scan configuration files or memory management patterns to identify session state stored locally in-memory instead of a distributed session store.
   - **Unbounded Retries Detector:**
     - Scan automated retry configurations to flag immediate, consecutive duplicate requests lacking backoff or jitter.
   - **Infinite Resource Waiting Detector:**
     - Flag network, API, or database connection requests lacking explicitly bounded, aggressive timeouts and fallback handlers.
2. **Output Report (`Bugs.md`):**
   - Save a markdown report named `Bugs.md` containing:
     - A categorized summary of all detected architectural issues.
     - Locations/Origin files where the violations were detected.
     - Remediation guidance mapping directly to the fixes specified in this PRD.
3. **Constraints:**
   - Do not commit or push changes to the repository before the three documentation files (PRD, Plan, and Todo) are reviewed by the user.
