# Graph Report - data/BugsInPy  (2026-06-18)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 58 nodes · 58 edges · 13 communities (1 shown, 12 thin omitted)
- Extraction: 69% EXTRACTED · 31% INFERRED · 0% AMBIGUOUS · INFERRED: 18 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)
1. `BugsInPy README` - 24 edges
2. `verify.sh script` - 2 edges
3. `my_function()` - 2 edges
4. `verify.sh script` - 2 edges
5. `my_function()` - 2 edges
6. `verify.sh script` - 2 edges
7. `my_function()` - 2 edges
8. `verify.sh script` - 2 edges
9. `my_function()` - 2 edges
10. `verify.sh script` - 2 edges

## Surprising Connections (you probably didn't know these)
- `youtube-dl Project` --conceptually_related_to--> `BugsInPy README`  [INFERRED]
  projects/youtube-dl/youtube-dl-pass.txt → README.md
- `Ansible Project` --conceptually_related_to--> `BugsInPy README`  [INFERRED]
  projects/ansible/ansible-pass.txt → README.md
- `Black Project` --conceptually_related_to--> `BugsInPy README`  [INFERRED]
  projects/black/black-pass.txt → README.md
- `Cookiecutter Project` --conceptually_related_to--> `BugsInPy README`  [INFERRED]
  projects/cookiecutter/cookiecutter-pass.txt → README.md
- `FastAPI Project` --conceptually_related_to--> `BugsInPy README`  [INFERRED]
  projects/fastapi/fastapi-pass.txt → README.md

## Import Cycles
- None detected.

## Communities (13 total, 12 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.09
Nodes (23): Ansible Project, Black Project, bugsinpy-compile, bugsinpy-coverage, bugsinpy-fuzz, bugsinpy-info, bugsinpy-mutation, BugsInPy README (+15 more)

## Knowledge Gaps
- **22 isolated node(s):** `bugsinpy-compile`, `bugsinpy-test`, `bugsinpy-info`, `bugsinpy-coverage`, `bugsinpy-mutation` (+17 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BugsInPy README` connect `Community 0` to `Community 12`?**
  _High betweenness centrality (0.172) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `BugsInPy README` (e.g. with `Ansible Project` and `Black Project`) actually correct?**
  _`BugsInPy README` has 17 INFERRED edges - model-reasoned connections that need verification._
- **What connects `bugsinpy-compile`, `bugsinpy-test`, `bugsinpy-info` to the rest of the system?**
  _22 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.08695652173913043 - nodes in this community are weakly interconnected._