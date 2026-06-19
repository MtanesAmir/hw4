# Product Requirements Document (PRD) - Reverse Engineering Agent

## Overview
The Reverse Engineering Agent is designed to analyze an unfamiliar codebase's AST (Abstract Syntax Tree) to extract architectural insights. It generates two key diagrams in a single markdown report: an **Architectural Block Diagram** (subpackage structure and information flow) and an **Object-Oriented (OOP) Schema** (class relationships, inheritance, and composition), both accompanied by detailed textual explanations.

## Objectives
- Implement a parser that traverses a codebase to extract module dependencies and class hierarchies.
- Generate a unified report named `reverse_engineer_agent_result.md` in the `result/` folder.
- The report must contain:
  1. An architectural block diagram showing subpackage structures and information flow.
  2. An OOP class diagram detailing inheritance, composition, and usages.
  3. Deep explanations of the architecture, module roles, and OOP patterns rather than just file listings.

## Requirements
1. **Source Code AST Parsing:**
   - Recursively parse Python source files in the project directories.
   - Extract imports, function calls, class definitions, class parentage, and attribute instantiations.
2. **Block Diagram Construction:**
   - Group files into functional modules (e.g. by subfolder or package prefix).
   - Identify cross-module interactions (calls, imports) to map a high-level block diagram.
   - Format the diagram as a Mermaid flowchart (`graph TD`).
3. **OOP Schema Construction:**
   - Map class inheritance (e.g. `ClassA <|-- ClassB`), usage associations, and composition relationships.
   - Format the schema as a Mermaid class diagram (`classDiagram`).
4. **Unified Report (`result/reverse_engineer_agent_result.md`):**
   - Save the file under the `result/` directory.
   - The file must begin with: `"This file was written by the Agent."`
   - It must include both Mermaid diagrams.
   - For each diagram, write detailed textual analysis explaining the components, their responsibilities, and how they interact.
5. **Constraints:**
   - Do not commit or push changes to the repository before the three documentation files (PRD, Plan, and Todo) are reviewed by the user.
