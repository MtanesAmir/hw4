import os
import difflib

class FixerReporter:
    def __init__(self, output_path):
        self.output_path = output_path
        self.tasks = []
        
    def add_task(self, file_name, location, bug_type, status, original_code=None, modified_code=None):
        diff = ""
        if original_code and modified_code and status == 'Success':
            diff_lines = difflib.unified_diff(
                original_code.splitlines(keepends=True),
                modified_code.splitlines(keepends=True),
                fromfile=f"a/{file_name}",
                tofile=f"b/{file_name}"
            )
            diff = "".join(diff_lines)
            
        self.tasks.append({
            'file': file_name,
            'location': location,
            'bug_type': bug_type,
            'status': status,
            'diff': diff
        })
        
    def write_report(self):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        
        lines = [
            "This file was written by the Agent.",
            "",
            "# Automated Fixer Execution Log",
            "",
            "This report logs all automated refactoring modifications applied by the `Fixer` tool to resolve architectural bugs and suggestions.",
            "",
            "## 1. Summary of Resolved Violations",
            "",
            "| File | Location | Bug Type | Status |",
            "| :--- | :--- | :--- | :--- |"
        ]
        
        for task in self.tasks:
            lines.append(f"| `{task['file']}` | {task['location']} | {task['bug_type']} | **{task['status']}** |")
            
        lines.append("")
        lines.append("## 2. Refactoring Diffs")
        lines.append("")
        
        has_diffs = False
        for task in self.tasks:
            if task['diff']:
                has_diffs = True
                lines.append(f"### {task['file']} ({task['location']})")
                lines.append("```diff")
                lines.append(task['diff'].strip())
                lines.append("```")
                lines.append("")
                
        if not has_diffs:
            lines.append("No code modifications were made (all files clean or skipped).")
            
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))
        print(f"Generated execution report to: {self.output_path}")
