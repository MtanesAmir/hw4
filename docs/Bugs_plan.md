# Implementation Plan - Architectural Bugs Detection

## Phase 1: Setup
- [x] Initialize repository
- [x] Create base files
- [x] Initialize architectural bugs detection package files in src/ and tests/ directories

## Phase 2: Development
- [x] **Code & Config Parser:**
  - Build scanners to parse python/bash code and project configurations for retry rules, network timeouts, and local state configurations.
  - Integrate with the parsed codebase graph (`graph.json`) to analyze coupling and node degree metrics.
- [x] **Defect Evaluator Engine:**
  - Implement heuristic rules to identify:
    - Tight coupling paths between services.
    - Highly connected "God Class" modules (large degree nodes).
    - Stateful session setups (sticky sessions).
    - Unbounded/storm-prone retries (missing backoff/jitter).
    - Starvation-prone connections (missing timeouts).
- [x] **Report Generator:**
  - Format detected bugs as a table or list in `Bugs.md` detailing the violating node, file reference, problem description, and standard fix advice.
- [x] **Command Line Interface:**
  - Create `bugs_analyzer.py` entry point script.

## Phase 3: Verification
- [x] **Unit Testing:**
  - Test each rule evaluator with mock graph elements and configuration values to verify positive/negative detection.
- [x] **Integration Testing:**
  - Run the tool on the workspace and verify `Bugs.md` output generation.
- [ ] **Repository Check:**
  - Request user review of the three documentation files (PRD, Plan, Todo) before making any commits.
