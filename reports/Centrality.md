# Centrality (Subject 8)

According to subject 8 of the Lecture Summary, **Centrality** represents nodes with high connectivity (God Nodes). These nodes have a high number of incoming and outgoing relationships, serving as key hubs in the codebase architecture.

## Central Nodes in hw4

| Rank | Central Node | Connections (Degree) | Origin File | Location |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [[cli.py]] | 24 | [src/main/agent/cli.py](src/main/agent/cli.py) | L1 |
| 2 | [[reporter.py]] | 17 | [src/main/bugs/reporter.py](src/main/bugs/reporter.py) | L1 |
| 3 | [[BugsGraph]] | 15 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L5 |
| 4 | [[ResearchBugsAgentWorkflow]] | 14 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L13 |
| 5 | [[KnowledgeGraph]] | 14 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L5 |
| 6 | [[main()]] | 12 | [src/main/agent/cli.py](src/main/agent/cli.py) | L6 |
| 7 | [[HubsGraph]] | 10 | [src/main/hubs/graph.py](src/main/hubs/graph.py) | L6 |
| 8 | [[evaluators.py]] | 9 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L1 |
| 9 | [[generate_bugs_report()]] | 9 | [src/main/bugs/reporter.py](src/main/bugs/reporter.py) | L10 |
| 10 | [[TestBugs]] | 9 | [tests/test_bugs.py](tests/test_bugs.py) | L14 |
| 11 | [[graph.py]] | 8 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L1 |
| 12 | [[ASTScanner]] | 8 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L4 |
| 13 | [[.run()]] | 7 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L27 |
| 14 | [[.bugs_node()]] | 7 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L99 |
| 15 | [[check_local_state_dependency()]] | 7 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L71 |
| 16 | [[check_unbounded_retries()]] | 7 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L108 |
| 17 | [[check_infinite_waiting()]] | 7 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L146 |
| 18 | [[parse_frontmatter()]] | 7 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L3 |
| 19 | [[calculate_betweenness_centrality()]] | 7 | [src/main/hubs/analyzer.py](src/main/hubs/analyzer.py) | L1 |
| 20 | [[Phase 1: Setup]] | 7 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L3 |
| 21 | [[Phase 2: Development]] | 7 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L8 |
| 22 | [[Phase 3: Verification]] | 7 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L21 |
| 23 | [[Overview]] | 7 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L3 |
| 24 | [[Objectives]] | 7 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L6 |
| 25 | [[Requirements]] | 7 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L11 |
| 26 | [[check_tight_coupling()]] | 6 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L4 |
| 27 | [[check_god_class()]] | 6 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L40 |
| 28 | [[.load_from_json()]] | 6 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L53 |
| 29 | [[extractor.py]] | 6 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L1 |
| 30 | [[extract_all_links()]] | 6 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L42 |
| 31 | [[mapper.py]] | 6 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L1 |
| 32 | [[write_reverse_engineer_report()]] | 6 | [src/main/reverse_engineer/reporter.py](src/main/reverse_engineer/reporter.py) | L4 |
| 33 | [[README.md]] | 6 | [README.md](README.md) | L1 |
| 34 | [[workflow.py]] | 5 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L1 |
| 35 | [[.__init__()]] | 5 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L14 |
| 36 | [[analyze_file_content()]] | 5 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L59 |
| 37 | [[.add_edge()]] | 5 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L13 |
| 38 | [[.build_vault_mapping()]] | 5 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L24 |
| 39 | [[.add_node()]] | 5 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L11 |
| 40 | [[generate_report()]] | 5 | [src/main/centrality/reporter.py](src/main/centrality/reporter.py) | L3 |
| 41 | [[generate_hubs_report()]] | 5 | [src/main/hubs/reporter.py](src/main/hubs/reporter.py) | L4 |
| 42 | [[generate_block_diagram()]] | 5 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L1 |
| 43 | [[generate_oop_diagram()]] | 5 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L33 |
| 44 | [[map_bugs_to_suggestions()]] | 5 | [src/main/suggestions/mapper.py](src/main/suggestions/mapper.py) | L1 |
| 45 | [[parse_bugs_report()]] | 5 | [src/main/suggestions/parser.py](src/main/suggestions/parser.py) | L4 |
| 46 | [[generate_suggestions_report()]] | 5 | [src/main/suggestions/reporter.py](src/main/suggestions/reporter.py) | L4 |
| 47 | [[TestAgent]] | 5 | [tests/test_agent.py](tests/test_agent.py) | L8 |
| 48 | [[TestAnalyzer]] | 5 | [tests/test_analyzer.py](tests/test_analyzer.py) | L6 |
| 49 | [[TestExtractor]] | 5 | [tests/test_extractor.py](tests/test_extractor.py) | L4 |
| 50 | [[TestReverseEngineer]] | 5 | [tests/test_reverse_engineer.py](tests/test_reverse_engineer.py) | L8 |
| 51 | [[Architectural Analysis and Bugs Found]] | 5 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L3 |
| 52 | [[Implementation Plan]] | 5 | [docs/Centrality_plan.md](docs/Centrality_plan.md) | L1 |
| 53 | [[Product Requirements Document (PRD)]] | 5 | [docs/Centrality_prd.md](docs/Centrality_prd.md) | L1 |
| 54 | [[my_function()]] | 4 | [artifacts/BugsInPy/projects/PySnooper/verify.sh](artifacts/BugsInPy/projects/PySnooper/verify.sh) | L47 |
| 55 | [[graph_loader.py]] | 4 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L1 |
| 56 | [[extract_wiki_links()]] | 4 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L22 |
| 57 | [[extract_markdown_links()]] | 4 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L29 |
| 58 | [[.build_from_entry()]] | 4 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L35 |
| 59 | [[.setUp()]] | 4 | [tests/test_agent.py](tests/test_agent.py) | L9 |
| 60 | [[.tearDown()]] | 4 | [tests/test_agent.py](tests/test_agent.py) | L12 |
| 61 | [[.test_ast_scanning_rules()]] | 4 | [tests/test_reverse_engineer.py](tests/test_reverse_engineer.py) | L15 |
| 62 | [[TestSuggestions]] | 4 | [tests/test_suggestions.py](tests/test_suggestions.py) | L8 |
| 63 | [[SKILL.md]] | 4 | [.agents/skills/write-md/SKILL.md](.agents/skills/write-md/SKILL.md) | L1 |
| 64 | [[Guidelines for the Agent:]] | 4 | [.agents/skills/write-md/SKILL.md](.agents/skills/write-md/SKILL.md) | L10 |
| 65 | [[Implementation Plan - Bridges Analysis]] | 4 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L1 |
| 66 | [[Product Requirements Document (PRD) - Bridges Analysis]] | 4 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L1 |
| 67 | [[Implementation Plan - Architectural Bugs Detection]] | 4 | [docs/Bugs_plan.md](docs/Bugs_plan.md) | L1 |
| 68 | [[Product Requirements Document (PRD) - Architectural Bugs Detection]] | 4 | [docs/Bugs_prd.md](docs/Bugs_prd.md) | L1 |
| 69 | [[Implementation Plan - Hubs Analysis]] | 4 | [docs/Hubs_plan.md](docs/Hubs_plan.md) | L1 |
| 70 | [[Product Requirements Document (PRD) - Hubs Analysis]] | 4 | [docs/Hubs_prd.md](docs/Hubs_prd.md) | L1 |
| 71 | [[Implementation Plan - Research Bugs Agent]] | 4 | [docs/Research_bugs_agent_plan.md](docs/Research_bugs_agent_plan.md) | L1 |
| 72 | [[Product Requirements Document (PRD) - Research Bugs Agent]] | 4 | [docs/Research_bugs_agent_prd.md](docs/Research_bugs_agent_prd.md) | L1 |
| 73 | [[Implementation Plan - Reverse Engineering Agent]] | 4 | [docs/Reverse_engineering_agent_plan.md](docs/Reverse_engineering_agent_plan.md) | L1 |
| 74 | [[Product Requirements Document (PRD) - Reverse Engineering Agent]] | 4 | [docs/Reverse_engineering_agent_prd.md](docs/Reverse_engineering_agent_prd.md) | L1 |
| 75 | [[Implementation Plan - Architectural Improvement Suggestions]] | 4 | [docs/Suggestions_plan.md](docs/Suggestions_plan.md) | L1 |
| 76 | [[Product Requirements Document (PRD) - Architectural Improvement Suggestions]] | 4 | [docs/Suggestions_prd.md](docs/Suggestions_prd.md) | L1 |
| 77 | [[.load_graph_node()]] | 3 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L37 |
| 78 | [[.hubs_node()]] | 3 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L56 |
| 79 | [[ast_scanner.py]] | 3 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L1 |
| 80 | [[parser.py]] | 3 | [src/main/suggestions/parser.py](src/main/suggestions/parser.py) | L1 |
| 81 | [[.test_generate_report()]] | 3 | [tests/test_analyzer.py](tests/test_analyzer.py) | L111 |
| 82 | [[test_bugs.py]] | 3 | [tests/test_bugs.py](tests/test_bugs.py) | L1 |
| 83 | [[.test_tight_coupling()]] | 3 | [tests/test_bugs.py](tests/test_bugs.py) | L21 |
| 84 | [[.test_god_class()]] | 3 | [tests/test_bugs.py](tests/test_bugs.py) | L37 |
| 85 | [[.test_local_state_dependency()]] | 3 | [tests/test_bugs.py](tests/test_bugs.py) | L48 |
| 86 | [[.test_unbounded_retries()]] | 3 | [tests/test_bugs.py](tests/test_bugs.py) | L63 |
| 87 | [[.test_infinite_waiting()]] | 3 | [tests/test_bugs.py](tests/test_bugs.py) | L78 |
| 88 | [[TestHubs]] | 3 | [tests/test_hubs.py](tests/test_hubs.py) | L5 |
| 89 | [[.test_star_graph_betweenness()]] | 3 | [tests/test_hubs.py](tests/test_hubs.py) | L6 |
| 90 | [[.test_path_graph_betweenness()]] | 3 | [tests/test_hubs.py](tests/test_hubs.py) | L23 |
| 91 | [[test_reverse_engineer.py]] | 3 | [tests/test_reverse_engineer.py](tests/test_reverse_engineer.py) | L1 |
| 92 | [[test_suggestions.py]] | 3 | [tests/test_suggestions.py](tests/test_suggestions.py) | L1 |
| 93 | [[.test_parser_and_mapper()]] | 3 | [tests/test_suggestions.py](tests/test_suggestions.py) | L15 |
| 94 | [[Codebase Architecture Analysis & Research Agent]] | 3 | [README.md](README.md) | L1 |
| 95 | [[verify.sh]] | 2 | [artifacts/BugsInPy/projects/PySnooper/verify.sh](artifacts/BugsInPy/projects/PySnooper/verify.sh) | L1 |
| 96 | [[verify.sh script]] | 2 | [artifacts/BugsInPy/projects/PySnooper/verify.sh](artifacts/BugsInPy/projects/PySnooper/verify.sh) | L1 |
| 97 | [[update_readme.sh]] | 2 | [artifacts/BugsInPy/update_readme.sh](artifacts/BugsInPy/update_readme.sh) | L1 |
| 98 | [[update_readme.sh script]] | 2 | [artifacts/BugsInPy/update_readme.sh](artifacts/BugsInPy/update_readme.sh) | L1 |
| 99 | [[.centrality_node()]] | 2 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L43 |
| 100 | [[.bridges_node()]] | 2 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L69 |
| 101 | [[.compile_report_node()]] | 2 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L122 |
| 102 | [[.calculate_degrees()]] | 2 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L154 |
| 103 | [[hubs_analyzer.py]] | 2 | [src/main/hubs_analyzer.py](src/main/hubs_analyzer.py) | L1 |
| 104 | [[.scan()]] | 2 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L10 |
| 105 | [[.scan_file_node()]] | 2 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L26 |
| 106 | [[test_agent.py]] | 2 | [tests/test_agent.py](tests/test_agent.py) | L1 |
| 107 | [[.test_agent_workflow_execution()]] | 2 | [tests/test_agent.py](tests/test_agent.py) | L15 |
| 108 | [[test_analyzer.py]] | 2 | [tests/test_analyzer.py](tests/test_analyzer.py) | L1 |
| 109 | [[.test_graph_degrees()]] | 2 | [tests/test_analyzer.py](tests/test_analyzer.py) | L7 |
| 110 | [[.test_load_from_json()]] | 2 | [tests/test_analyzer.py](tests/test_analyzer.py) | L55 |
| 111 | [[test_extractor.py]] | 2 | [tests/test_extractor.py](tests/test_extractor.py) | L1 |
| 112 | [[.test_parse_frontmatter()]] | 2 | [tests/test_extractor.py](tests/test_extractor.py) | L5 |
| 113 | [[.test_parse_frontmatter_empty()]] | 2 | [tests/test_extractor.py](tests/test_extractor.py) | L20 |
| 114 | [[.test_extract_wiki_links()]] | 2 | [tests/test_extractor.py](tests/test_extractor.py) | L25 |
| 115 | [[.test_extract_markdown_links()]] | 2 | [tests/test_extractor.py](tests/test_extractor.py) | L35 |
| 116 | [[test_hubs.py]] | 2 | [tests/test_hubs.py](tests/test_hubs.py) | L1 |
| 117 | [[graphify.md]] | 2 | [.agents/rules/graphify.md](.agents/rules/graphify.md) | L1 |
| 118 | [[Skill: Write MD (Orchestrated Pipeline)]] | 2 | [.agents/skills/write-md/SKILL.md](.agents/skills/write-md/SKILL.md) | L6 |
| 119 | [[Skill: Write Plan]] | 2 | [.agents/skills/write-plan/SKILL.md](.agents/skills/write-plan/SKILL.md) | L6 |
| 120 | [[Skill: Write PRD]] | 2 | [.agents/skills/write-prd/SKILL.md](.agents/skills/write-prd/SKILL.md) | L6 |
| 121 | [[Skill: Write TODO]] | 2 | [.agents/skills/write-todo/SKILL.md](.agents/skills/write-todo/SKILL.md) | L6 |
| 122 | [[Autonomous Research Agent (`run_agent.py`)]] | 2 | [README.md](README.md) | L17 |
| 123 | [[Todo List]] | 2 | [docs/Centrality_todo.md](docs/Centrality_todo.md) | L1 |
| 124 | [[Centrality (Subject 8)]] | 2 | [reports/Centrality_test.md](reports/Centrality_test.md) | L1 |
| 125 | [[run_test.sh]] | 1 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh) | L1 |
| 126 | [[run_test.sh script]] | 1 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh) | L1 |
| 127 | [[setup.sh]] | 1 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh) | L1 |
| 128 | [[setup.sh script]] | 1 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh) | L1 |
| 129 | [[fuzz_target.py]] | 1 | [artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py](artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py) | L1 |
| 130 | [[fuzz()]] | 1 | [artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py](artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py) | L7 |
| 131 | [[Identifies nodes with high ratio of cross-community connections.]] | 1 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L5 |
| 132 | [[Identifies God Classes/Monoliths based on node degree.]] | 1 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L41 |
| 133 | [[Helper to safely read file content.]] | 1 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L60 |
| 134 | [[Scans files for local memory session stores without distributed persistence.]] | 1 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L72 |
| 135 | [[Checks for automated retry mechanisms lacking exponential backoff or jitter.]] | 1 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L109 |
| 136 | [[Detects network requests (requests.get/post) that miss the timeout argument.]] | 1 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L147 |
| 137 | [[Evaluates rules and generates the architectural bugs report.]] | 1 | [src/main/bugs/reporter.py](src/main/bugs/reporter.py) | L11 |
| 138 | [[bugs_analyzer.py]] | 1 | [src/main/bugs_analyzer.py](src/main/bugs_analyzer.py) | L1 |
| 139 | [[Parses basic YAML frontmatter from markdown content.]] | 1 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L4 |
| 140 | [[Extracts all wiki-links of the form [[Node Name]] from the content.]] | 1 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L23 |
| 141 | [[Extracts all relative internal markdown links.]] | 1 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L30 |
| 142 | [[Extracts and merges wiki-links and markdown links.]] | 1 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L43 |
| 143 | [[Calculates the degree (connections) of each node.         Returns a dict mapping]] | 1 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L155 |
| 144 | [[Generates the Centrality.md report based on the computed graph degrees.]] | 1 | [src/main/centrality/reporter.py](src/main/centrality/reporter.py) | L4 |
| 145 | [[centrality_analyzer.py]] | 1 | [src/main/centrality_analyzer.py](src/main/centrality_analyzer.py) | L1 |
| 146 | [[Calculates Betweenness Centrality for all nodes in the graph using Brandes' algo]] | 1 | [src/main/hubs/analyzer.py](src/main/hubs/analyzer.py) | L2 |
| 147 | [[Generates the Hubs.md report listing ranked bottleneck nodes.]] | 1 | [src/main/hubs/reporter.py](src/main/hubs/reporter.py) | L5 |
| 148 | [[Groups modules by top-level package and creates cross-package flowchart links.]] | 1 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L2 |
| 149 | [[Constructs class definitions, methods, inheritance, and compositions in Mermaid]] | 1 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L34 |
| 150 | [[Assembles the block diagram, OOP schema, and textual descriptions into a markdow]] | 1 | [src/main/reverse_engineer/reporter.py](src/main/reverse_engineer/reporter.py) | L5 |
| 151 | [[run_agent.py]] | 1 | [src/main/run_agent.py](src/main/run_agent.py) | L1 |
| 152 | [[run_reverse_engineer.py]] | 1 | [src/main/run_reverse_engineer.py](src/main/run_reverse_engineer.py) | L1 |
| 153 | [[Translates parsed categories of architectural bugs to a list of suggestions]] | 1 | [src/main/suggestions/mapper.py](src/main/suggestions/mapper.py) | L2 |
| 154 | [[Parses the Bugs.md report and returns a dict mapping bug categories (1-5) to a l]] | 1 | [src/main/suggestions/parser.py](src/main/suggestions/parser.py) | L5 |
| 155 | [[Builds the Suggestions.md report table mapping defects to Solution Architecture]] | 1 | [src/main/suggestions/reporter.py](src/main/suggestions/reporter.py) | L5 |
| 156 | [[suggestions_generator.py]] | 1 | [src/main/suggestions_generator.py](src/main/suggestions_generator.py) | L1 |
| 157 | [[graphify]] | 1 | [.agents/rules/graphify.md](.agents/rules/graphify.md) | L6 |
| 158 | [[Workflow: graphify]] | 1 | [.agents/workflows/graphify.md](.agents/workflows/graphify.md) | L6 |
| 159 | [[Features]] | 1 | [README.md](README.md) | L5 |
| 160 | [[Usage]] | 1 | [README.md](README.md) | L25 |
| 161 | [[BugsInPy]] | 1 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L1 |
| 162 | [[Steps to set up BugsInPy]] | 1 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L5 |
| 163 | [[Use Docker]] | 1 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L11 |
| 164 | [[BugsInPy Command]] | 1 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L32 |
| 165 | [[Example BugsInPy Command]] | 1 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L43 |
| 166 | [[bugs_we_found.md]] | 1 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L1 |
| 167 | [[1. Central Nodes (Degree Centrality - Subject 8)]] | 1 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L7 |
| 168 | [[2. Hubs (Betweenness Centrality - Subject 10)]] | 1 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L23 |
| 169 | [[3. Bridge Nodes (Cross-Community Links)]] | 1 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L39 |
| 170 | [[4. Architectural Bugs and Anti-Patterns Found]] | 1 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L48 |
| 171 | [[Bridges_plan.md]] | 1 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L1 |
| 172 | [[Bridges_prd.md]] | 1 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L1 |
| 173 | [[Bridges_todo.md]] | 1 | [docs/Bridges_todo.md](docs/Bridges_todo.md) | L1 |
| 174 | [[Todo List - Bridges Analysis]] | 1 | [docs/Bridges_todo.md](docs/Bridges_todo.md) | L1 |
| 175 | [[Bugs_plan.md]] | 1 | [docs/Bugs_plan.md](docs/Bugs_plan.md) | L1 |
| 176 | [[Bugs_prd.md]] | 1 | [docs/Bugs_prd.md](docs/Bugs_prd.md) | L1 |
| 177 | [[Bugs_todo.md]] | 1 | [docs/Bugs_todo.md](docs/Bugs_todo.md) | L1 |
| 178 | [[Todo List - Architectural Bugs Detection]] | 1 | [docs/Bugs_todo.md](docs/Bugs_todo.md) | L1 |
| 179 | [[Centrality_plan.md]] | 1 | [docs/Centrality_plan.md](docs/Centrality_plan.md) | L1 |
| 180 | [[Centrality_prd.md]] | 1 | [docs/Centrality_prd.md](docs/Centrality_prd.md) | L1 |
| 181 | [[Centrality_todo.md]] | 1 | [docs/Centrality_todo.md](docs/Centrality_todo.md) | L1 |
| 182 | [[Hubs_plan.md]] | 1 | [docs/Hubs_plan.md](docs/Hubs_plan.md) | L1 |
| 183 | [[Hubs_prd.md]] | 1 | [docs/Hubs_prd.md](docs/Hubs_prd.md) | L1 |
| 184 | [[Hubs_todo.md]] | 1 | [docs/Hubs_todo.md](docs/Hubs_todo.md) | L1 |
| 185 | [[Todo List - Hubs Analysis]] | 1 | [docs/Hubs_todo.md](docs/Hubs_todo.md) | L1 |
| 186 | [[Research_bugs_agent_plan.md]] | 1 | [docs/Research_bugs_agent_plan.md](docs/Research_bugs_agent_plan.md) | L1 |
| 187 | [[Research_bugs_agent_prd.md]] | 1 | [docs/Research_bugs_agent_prd.md](docs/Research_bugs_agent_prd.md) | L1 |
| 188 | [[Research_bugs_agent_todo.md]] | 1 | [docs/Research_bugs_agent_todo.md](docs/Research_bugs_agent_todo.md) | L1 |
| 189 | [[Todo List - Research Bugs Agent]] | 1 | [docs/Research_bugs_agent_todo.md](docs/Research_bugs_agent_todo.md) | L1 |
| 190 | [[Reverse_engineering_agent_plan.md]] | 1 | [docs/Reverse_engineering_agent_plan.md](docs/Reverse_engineering_agent_plan.md) | L1 |
| 191 | [[Reverse_engineering_agent_prd.md]] | 1 | [docs/Reverse_engineering_agent_prd.md](docs/Reverse_engineering_agent_prd.md) | L1 |
| 192 | [[Reverse_engineering_agent_todo.md]] | 1 | [docs/Reverse_engineering_agent_todo.md](docs/Reverse_engineering_agent_todo.md) | L1 |
| 193 | [[Todo List - Reverse Engineering Agent]] | 1 | [docs/Reverse_engineering_agent_todo.md](docs/Reverse_engineering_agent_todo.md) | L1 |
| 194 | [[Suggestions_plan.md]] | 1 | [docs/Suggestions_plan.md](docs/Suggestions_plan.md) | L1 |
| 195 | [[Suggestions_prd.md]] | 1 | [docs/Suggestions_prd.md](docs/Suggestions_prd.md) | L1 |
| 196 | [[Suggestions_todo.md]] | 1 | [docs/Suggestions_todo.md](docs/Suggestions_todo.md) | L1 |
| 197 | [[Todo List - Architectural Improvement Suggestions]] | 1 | [docs/Suggestions_todo.md](docs/Suggestions_todo.md) | L1 |
| 198 | [[PLAN.md]] | 1 | [docs/instructions/PLAN.md](docs/instructions/PLAN.md) | L1 |
| 199 | [[PRD.md]] | 1 | [docs/instructions/PRD.md](docs/instructions/PRD.md) | L1 |
| 200 | [[TODO.md]] | 1 | [docs/instructions/TODO.md](docs/instructions/TODO.md) | L1 |
| 201 | [[research_question.md]] | 1 | [docs/research_question.md](docs/research_question.md) | L1 |
| 202 | [[Research Questions]] | 1 | [docs/research_question.md](docs/research_question.md) | L1 |
| 203 | [[Centrality_test.md]] | 1 | [reports/Centrality_test.md](reports/Centrality_test.md) | L1 |
| 204 | [[Central Nodes in BugsInPy]] | 1 | [reports/Centrality_test.md](reports/Centrality_test.md) | L5 |
| 205 | [[__init__.py]] | 0 | [src/main/agent/__init__.py](src/main/agent/__init__.py) | L1 |
