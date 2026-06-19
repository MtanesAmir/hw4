# Performance and Token Cost Metrics

## Reverse Engineering Agent
- **LLM Token Usage**: 0 tokens (purely static AST parser)
- **Total Files Scanned**: 5 files (3 successfully parsed, 2 skipped due to syntax errors in `broken-python` files)
- **Execution Time**: 0.080 seconds

## Research Bugs Agent
- **LLM Token Usage**: 0 tokens (purely static local analyzer)
- **Total Files Scanned**: 2 graph/manifest files + 5 codebase Python source files
- **Execution Time**: 0.082 seconds
