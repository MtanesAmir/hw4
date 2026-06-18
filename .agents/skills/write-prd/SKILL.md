---
name: write-prd
description: Create a Product Requirements Document (PRD) in the docs directory using the PRD template and suffix _prd.md when the user invokes /write-prd or asks to write a PRD.
---

# Skill: Write PRD

This skill handles user requests to generate a Product Requirements Document (PRD) based on their input.

## Guidelines for the Agent:

1. **Identify Given Name and Input Text**:
   - Extract the `given name` (e.g., `feature-name`, `chat-integration`) and the `input text` / description from the user's request.
   - If the `given name` is not provided or is ambiguous, ask the user to provide a filename prefix.

2. **File Template and Path**:
   - The file must be saved in the `docs/` directory of the workspace root:
     `docs/<given_name>_prd.md`
   - Use the template from `docs/instructions/PRD.md` as the format:
     ```markdown
     # Product Requirements Document (PRD)

     ## Overview
     [Overview and description based on the user's input text]

     ## Objectives
     [Objectives and goals derived from the user's input text]

     ## Requirements
     [Detailed list of requirements parsed from the user's input text]
     ```

3. **Writing the File**:
   - Synthesize the content for each section carefully using the user's input text.
   - Write the file using the `write_to_file` tool to `docs/<given_name>_prd.md`.
   - Once written, notify the user and provide a markdown link to the created file.
