# Implementation Plan - Automated Fixer Tool

## Proposed Architecture
The tool will consist of:
- **`src/main/fixer/parser.py`**: A markdown table parser to extract defect records from `Bugs.md` and `Suggestions.md`.
- **`src/main/fixer/engine.py`**: A code-modification engine that parses Python source files, identifies violating constructs, and applies automated refactorings.
- **`src/main/fixer/reporter.py`**: A reporter module to log successfully refactored files and code changes to `reports/fixer_done.md`.
- **`src/main/fixer_runner.py`**: The CLI wrapper runner script.

## Phase-by-Phase Plan

### Phase 1: Parsing
- Implement `MarkdownParser` to parse the Markdown tables.
- Return structured list:
  ```python
  [{
      'file': 'mathsquiz/mathsquiz.py',
      'location': 'L14',
      'bug_type': 'Infinite Waiting',
      'suggestion': 'Add timeout parameter'
  }]
  ```

### Phase 2: Refactoring Engine
- Implement code modification strategies:
  - **Infinite Waiting:** Parse code and add `timeout=10` parameter to requests, sockets, or HTTP connections.
  - **Unbounded Retries:** Detect `while True:` retry blocks and refactor them with `max_retries = 3` and `time.sleep(1)` backoff.
  - **Local State Dependency:** Refactor local dictionary state caches to use an abstract Redis class client.
  - **God Class / Coupling:** Extract large class functions into separate modules.

### Phase 3: Logging and CLI Runner
- Implement `FixerReporter` which:
  - Writes to `reports/fixer_done.md`.
  - Begins with `"This file was written by the Agent."`.
  - Formats tables of resolved bugs, locations, and code diffs.
- Create `src/main/fixer_runner.py` with standard CLI argument parsing (`bugs_file`, `suggestions_file`, `project_root`).

### Phase 4: Verification and Testing
- Create a test suite at `tests/test_fixer.py` verifying:
  - Markdown table parser correctness.
  - Injected timeouts code refactorings.
  - Backoff retry conversions.
- Run all tests to ensure correctness.
