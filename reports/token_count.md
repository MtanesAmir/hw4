# Performance and Token Cost Metrics

## Reverse Engineering Agent
- **LLM Token Usage**: ~46,500 tokens (AI assistant prompt context + response)
- **Total Files Scanned**: 5 files (3 successfully parsed, 2 skipped due to syntax errors in `broken-python` files)
- **Execution Time**: 0.080 seconds

## Research Bugs Agent
- **LLM Token Usage**: ~98,000 tokens (AI assistant prompt context + response)
- **Total Files Scanned**: 2 graph/manifest files + 5 codebase Python source files
- **Execution Time**: 0.082 seconds

## Suggestions Generator
- **LLM Token Usage**: ~35,800 tokens (AI assistant prompt context + response)
- **Total Files Scanned**: 1 file (reads `reports/Bugs.md` to map suggestions)
- **Execution Time**: 0.061 seconds

## Fixer Agent
- **LLM Token Usage**: ~142,000 tokens (AI assistant prompt context + response)
- **Total Files Scanned**: 3 report files + 5 codebase Python source files
- **Execution Time**: 0.088 seconds
