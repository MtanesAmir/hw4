---
name: write-todo
description: Generate a TODO list in the docs directory based on an Implementation Plan using the TODO template and suffix _todo.md when the user invokes /write-todo or asks to write a TODO list.
---

# Skill: Write TODO

This skill handles user requests to generate a Developer TODO list based on an Implementation Plan.

## Guidelines for the Agent:

1. **Identify the Plan File and Prefix**:
   - Identify the source plan file (e.g., `docs/login-feature_plan.md` or just the prefix `login-feature`).
   - The output file prefix must match the plan file prefix. E.g., if the plan file is `docs/xyz_plan.md`, the todo filename must be `docs/xyz_todo.md`.
   - Read the contents of the target plan file in the `docs/` folder to extract the tasks.

2. **Generate the TODO List**:
   - Extract all the development and verification tasks from the plan.
   - Formulate them into a clean, flat, checkbox-style list (`- [ ]`) representing exactly what the developer needs to do.
   - Use the template from `docs/instructions/TODO.md` as the format structure:
     ```markdown
     # Todo List

     - [ ] Task 1 (e.g., Complete base setup)
     - [ ] Task 2 (e.g., Implement backend API endpoints)
     - [ ] Task 3 (e.g., Write unit tests for API)
     - [ ] ...
     ```

3. **Writing the File**:
   - Write the TODO list using the `write_to_file` tool to `docs/<prefix>_todo.md`.
   - Once written, notify the user and provide a markdown link to the created file.
