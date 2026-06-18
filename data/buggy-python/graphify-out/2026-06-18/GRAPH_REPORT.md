# Graph Report - data/buggy-python  (2026-06-18)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 16 nodes · 14 edges · 4 communities (0 shown, 4 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]

## God Nodes (most connected - your core abstractions)
1. `foo()` - 3 edges
2. `Buggy Python Project` - 2 edges
3. `The purpose of this snippet is to test your knowledge of default arguments for f` - 1 edges
4. `Simple python script to read a json file of loan then add perform some calculati` - 1 edges
5. `Simple array of lambda functions that is used to calculate the addition of a num` - 1 edges
6. `Python3` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (4 total, 4 thin omitted)

## Knowledge Gaps
- **1 isolated node(s):** `Python3`
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `foo()` connect `Community 1` to `Community 2`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **What connects `The purpose of this snippet is to test your knowledge of default arguments for f`, `Simple python script to read a json file of loan then add perform some calculati`, `Simple array of lambda functions that is used to calculate the addition of a num` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._