---
name: write-md
description: Run the complete document generation pipeline (PRD -> Implementation Plan -> TODO list) in the docs directory when the user invokes /write-md or asks to generate all document types.
---

# Skill: Write MD (Orchestrated Pipeline)

This skill automates the complete pipeline of writing a PRD, followed by an Implementation Plan, and finally a Developer TODO list, all using the same prefix name.

## Guidelines for the Agent:

1. **Extract Name and Details**:
   - Extract the `given name` (file prefix) and the project details / description from the user's request.
   - If the `given name` is not provided, ask the user for a filename prefix first.

2. **Step 1: Write the PRD**:
   - Follow the instructions in `write-prd` skill.
   - Generate the PRD file at `docs/<given_name>_prd.md` based on the user's description and the template at `docs/instructions/PRD.md`.

3. **Step 2: Write the Plan**:
   - Follow the instructions in `write-plan` skill.
   - Use the written `docs/<given_name>_prd.md` file to generate the Implementation Plan at `docs/<given_name>_plan.md` using the template at `docs/instructions/PLAN.md`.

4. **Step 3: Write the TODO List**:
   - Follow the instructions in `write-todo` skill.
   - Use the written `docs/<given_name>_plan.md` file to generate the TODO list at `docs/<given_name>_todo.md` using the template at `docs/instructions/TODO.md`.

5. **Report Completion**:
   - Present the links to all three files in a structured list:
     - **PRD**: [docs/<given_name>_prd.md](file:///Users/amirmt/Desktop/ME/Me/MSC-ComputerScience/2025-B/agent%20AI/hw4/docs/<given_name>_prd.md)
     - **Plan**: [docs/<given_name>_plan.md](file:///Users/amirmt/Desktop/ME/Me/MSC-ComputerScience/2025-B/agent%20AI/hw4/docs/<given_name>_plan.md)
     - **TODO**: [docs/<given_name>_todo.md](file:///Users/amirmt/Desktop/ME/Me/MSC-ComputerScience/2025-B/agent%20AI/hw4/docs/<given_name>_todo.md)
