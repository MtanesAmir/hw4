---
name: write-plan
description: Generate an Implementation Plan in the docs directory based on a PRD using the PLAN template and suffix _plan.md when the user invokes /write-plan or asks to write a plan.
---

# Skill: Write Plan

This skill handles user requests to generate an Implementation Plan based on a Product Requirements Document (PRD).

## Guidelines for the Agent:

1. **Identify the PRD File and Prefix**:
   - Identify the source PRD file (e.g., `docs/login-feature_prd.md` or just the prefix `login-feature`).
   - The output file prefix must match the PRD file prefix. E.g., if the PRD file is `docs/xyz_prd.md`, the plan filename must be `docs/xyz_plan.md`.
   - Read the contents of the target PRD file in the `docs/` folder to understand its requirements.

2. **Generate the Project Plan**:
   - Act as a technical project manager creating an architectural and actionable implementation plan for a team of developers.
   - Use the template from `docs/instructions/PLAN.md` as the format structure:
     ```markdown
     # Implementation Plan

     ## Phase 1: Setup
     - [ ] Task 1 (e.g., Initialize repository)
     - [ ] Task 2 (e.g., Create base files)

     ## Phase 2: Development
     - [ ] Detailed developer task 1
     - [ ] Detailed developer task 2
     - [ ] ...

     ## Phase 3: Verification
     - [ ] Verification task 1 (e.g., test cases, validation checks)
     - [ ] Verification task 2
     ```
   - Elaborate each phase with clear, checkbox-style (`- [ ]`) developer tasks. Make Phase 2 (Development) and Phase 3 (Verification) highly specific to the requirements stated in the PRD.

3. **Writing the File**:
   - Write the plan file using the `write_to_file` tool to `docs/<prefix>_plan.md`.
   - Once written, notify the user and provide a markdown link to the created file.
