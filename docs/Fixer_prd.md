# Product Requirements Document (PRD) - Automated Fixer Tool

## Overview
The Automated Fixer Tool parses the `reports/Bugs.md` and `reports/Suggestions.md` reports, identifies the target violating files, locations, and refactoring guidelines, and automatically applies the standard architectural fixes to the source code. Upon completion, it generates a summary report at `reports/fixer_done.md`.

## Objectives
- Build an automated refactoring engine in Python.
- Parse the parsed defect tables from:
  - `reports/Bugs.md` (identifies architectural violations).
  - `reports/Suggestions.md` (identifies corresponding improvement principles).
- Apply refactoring templates to fix the five common architectural bugs:
  - Synchronous tight coupling.
  - God class / Monolithic modules.
  - Local state sticky sessions.
  - Unbounded retry storms.
  - Infinite request waiting (missing timeouts).
- Generate a summary log at `reports/fixer_done.md` describing the applied refactoring steps.

## Requirements
1. **Report Parsing Engine:**
   - Parse Markdown tables from both `reports/Bugs.md` and `reports/Suggestions.md`.
   - Extract:
     - Target source file path (relative to project root).
     - Violating node label and line number location.
     - Defect category and suggestion guidelines.
2. **Automated Refactoring Engine:**
   - Scan target files at the designated line numbers and apply structural changes.
   - Refactor:
     - **Infinite Waiting:** Locate socket or request library calls and append a default `timeout=N` parameter if missing.
     - **Unbounded Retries:** Rewrite unbounded `while True` retry loops to include backoff delay and a maximum retry cap.
     - **Local State Dependency:** Replace local memory dictionaries with Redis client session storage calls.
     - **God Class & Tight Coupling:** Split class definitions or extract modular functions to decouple interfaces.
3. **Execution Summary (`reports/fixer_done.md`):**
   - Save the file under the `reports/` folder.
   - The file must begin with: `"This file was written by the Agent."`
   - Include:
     - A table of resolved violations with target file, location, and bug type.
     - A diff summary of applied code fixes.
4. **Constraints:**
   - Do not commit or push changes to the repository before the three documentation files (PRD, Plan, and Todo) are reviewed by the user.
