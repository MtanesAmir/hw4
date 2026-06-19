# Hubs (Subject 10)

According to subject 10 of the Lecture Summary, **Hubs** represent bottleneck nodes in the codebase architecture. All information flows through these nodes. Although they may have few direct outgoing transitions, they are critical passage points and represent significant architectural dependencies.

## Top Hubs in hw4

| Rank | Hub Node | Betweenness Score | Origin File | Location |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [[cli.py]] | 0.131 | [src/main/agent/cli.py](src/main/agent/cli.py) | L1 |
| 2 | [[graph.py]] | 0.066 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L1 |
| 3 | [[reporter.py]] | 0.054 | [src/main/bugs/reporter.py](src/main/bugs/reporter.py) | L1 |
| 4 | [[ResearchBugsAgentWorkflow]] | 0.037 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L13 |
| 5 | [[KnowledgeGraph]] | 0.036 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L5 |
| 6 | [[BugsGraph]] | 0.035 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L5 |
| 7 | [[main()]] | 0.022 | [src/main/agent/cli.py](src/main/agent/cli.py) | L6 |
| 8 | [[parse_frontmatter()]] | 0.021 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L3 |
| 9 | [[extractor.py]] | 0.020 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L1 |
| 10 | [[extract_all_links()]] | 0.020 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L42 |
| 11 | [[generate_bugs_report()]] | 0.019 | [src/main/bugs/reporter.py](src/main/bugs/reporter.py) | L10 |
| 12 | [[ASTScanner]] | 0.019 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L4 |
| 13 | [[HubsGraph]] | 0.015 | [src/main/hubs/graph.py](src/main/hubs/graph.py) | L6 |
| 14 | [[calculate_betweenness_centrality()]] | 0.012 | [src/main/hubs/analyzer.py](src/main/hubs/analyzer.py) | L1 |
| 15 | [[write_reverse_engineer_report()]] | 0.011 | [src/main/reverse_engineer/reporter.py](src/main/reverse_engineer/reporter.py) | L4 |
| 16 | [[extract_wiki_links()]] | 0.010 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L22 |
| 17 | [[extract_markdown_links()]] | 0.010 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L29 |
| 18 | [[parse_bugs_report()]] | 0.010 | [src/main/suggestions/parser.py](src/main/suggestions/parser.py) | L4 |
| 19 | [[check_local_state_dependency()]] | 0.009 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L71 |
| 20 | [[check_unbounded_retries()]] | 0.009 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L108 |
| 21 | [[check_infinite_waiting()]] | 0.009 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L146 |
| 22 | [[generate_suggestions_report()]] | 0.008 | [src/main/suggestions/reporter.py](src/main/suggestions/reporter.py) | L4 |
| 23 | [[TestBugs]] | 0.008 | [tests/test_bugs.py](tests/test_bugs.py) | L14 |
| 24 | [[.build_vault_mapping()]] | 0.008 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L24 |
| 25 | [[generate_report()]] | 0.008 | [src/main/centrality/reporter.py](src/main/centrality/reporter.py) | L3 |
| 26 | [[map_bugs_to_suggestions()]] | 0.007 | [src/main/suggestions/mapper.py](src/main/suggestions/mapper.py) | L1 |
| 27 | [[check_tight_coupling()]] | 0.007 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L4 |
| 28 | [[check_god_class()]] | 0.007 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L40 |
| 29 | [[workflow.py]] | 0.007 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L1 |
| 30 | [[evaluators.py]] | 0.007 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L1 |
| 31 | [[generate_hubs_report()]] | 0.007 | [src/main/hubs/reporter.py](src/main/hubs/reporter.py) | L4 |
| 32 | [[generate_block_diagram()]] | 0.006 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L1 |
| 33 | [[generate_oop_diagram()]] | 0.006 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L33 |
| 34 | [[.bugs_node()]] | 0.006 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L99 |
| 35 | [[analyze_file_content()]] | 0.006 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L59 |
| 36 | [[.calculate_degrees()]] | 0.005 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L154 |
| 37 | [[.__init__()]] | 0.005 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L14 |
| 38 | [[mapper.py]] | 0.005 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L1 |
| 39 | [[TestAgent]] | 0.004 | [tests/test_agent.py](tests/test_agent.py) | L8 |
| 40 | [[parser.py]] | 0.004 | [src/main/suggestions/parser.py](src/main/suggestions/parser.py) | L1 |
| 41 | [[TestReverseEngineer]] | 0.004 | [tests/test_reverse_engineer.py](tests/test_reverse_engineer.py) | L8 |
| 42 | [[ast_scanner.py]] | 0.003 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L1 |
| 43 | [[.build_from_entry()]] | 0.003 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L35 |
| 44 | [[graph_loader.py]] | 0.003 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L1 |
| 45 | [[.add_edge()]] | 0.003 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L13 |
| 46 | [[.test_star_graph_betweenness()]] | 0.003 | [tests/test_hubs.py](tests/test_hubs.py) | L6 |
| 47 | [[.test_path_graph_betweenness()]] | 0.003 | [tests/test_hubs.py](tests/test_hubs.py) | L23 |
| 48 | [[.test_parser_and_mapper()]] | 0.002 | [tests/test_suggestions.py](tests/test_suggestions.py) | L15 |
| 49 | [[.setUp()]] | 0.002 | [tests/test_agent.py](tests/test_agent.py) | L9 |
| 50 | [[.tearDown()]] | 0.002 | [tests/test_agent.py](tests/test_agent.py) | L12 |
| 51 | [[.test_parse_frontmatter()]] | 0.002 | [tests/test_extractor.py](tests/test_extractor.py) | L5 |
| 52 | [[.test_parse_frontmatter_empty()]] | 0.002 | [tests/test_extractor.py](tests/test_extractor.py) | L20 |
| 53 | [[.test_ast_scanning_rules()]] | 0.002 | [tests/test_reverse_engineer.py](tests/test_reverse_engineer.py) | L15 |
| 54 | [[.run()]] | 0.002 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L27 |
| 55 | [[test_suggestions.py]] | 0.002 | [tests/test_suggestions.py](tests/test_suggestions.py) | L1 |
| 56 | [[.add_node()]] | 0.002 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L11 |
| 57 | [[.hubs_node()]] | 0.002 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L56 |
| 58 | [[.load_from_json()]] | 0.002 | [src/main/bugs/graph_loader.py](src/main/bugs/graph_loader.py) | L53 |
| 59 | [[TestSuggestions]] | 0.002 | [tests/test_suggestions.py](tests/test_suggestions.py) | L8 |
| 60 | [[test_hubs.py]] | 0.002 | [tests/test_hubs.py](tests/test_hubs.py) | L1 |
| 61 | [[.test_local_state_dependency()]] | 0.002 | [tests/test_bugs.py](tests/test_bugs.py) | L48 |
| 62 | [[.test_unbounded_retries()]] | 0.002 | [tests/test_bugs.py](tests/test_bugs.py) | L63 |
| 63 | [[.test_infinite_waiting()]] | 0.002 | [tests/test_bugs.py](tests/test_bugs.py) | L78 |
| 64 | [[Phase 1: Setup]] | 0.002 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L3 |
| 65 | [[Phase 2: Development]] | 0.002 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L8 |
| 66 | [[Phase 3: Verification]] | 0.002 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L21 |
| 67 | [[Overview]] | 0.002 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L3 |
| 68 | [[Objectives]] | 0.002 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L6 |
| 69 | [[Requirements]] | 0.002 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L11 |
| 70 | [[Implementation Plan]] | 0.002 | [docs/Centrality_plan.md](docs/Centrality_plan.md) | L1 |
| 71 | [[Product Requirements Document (PRD)]] | 0.002 | [docs/Centrality_prd.md](docs/Centrality_prd.md) | L1 |
| 72 | [[README.md]] | 0.001 | [README.md](README.md) | L1 |
| 73 | [[TestExtractor]] | 0.001 | [tests/test_extractor.py](tests/test_extractor.py) | L4 |
| 74 | [[.test_tight_coupling()]] | 0.001 | [tests/test_bugs.py](tests/test_bugs.py) | L21 |
| 75 | [[.test_god_class()]] | 0.001 | [tests/test_bugs.py](tests/test_bugs.py) | L37 |
| 76 | [[test_extractor.py]] | 0.001 | [tests/test_extractor.py](tests/test_extractor.py) | L1 |
| 77 | [[Codebase Architecture Analysis & Research Agent]] | 0.001 | [README.md](README.md) | L1 |
| 78 | [[hubs_analyzer.py]] | 0.001 | [src/main/hubs_analyzer.py](src/main/hubs_analyzer.py) | L1 |
| 79 | [[Implementation Plan - Architectural Bugs Detection]] | 0.001 | [docs/Bugs_plan.md](docs/Bugs_plan.md) | L1 |
| 80 | [[Product Requirements Document (PRD) - Architectural Bugs Detection]] | 0.001 | [docs/Bugs_prd.md](docs/Bugs_prd.md) | L1 |
| 81 | [[Implementation Plan - Hubs Analysis]] | 0.001 | [docs/Hubs_plan.md](docs/Hubs_plan.md) | L1 |
| 82 | [[Product Requirements Document (PRD) - Hubs Analysis]] | 0.001 | [docs/Hubs_prd.md](docs/Hubs_prd.md) | L1 |
| 83 | [[Implementation Plan - Research Bugs Agent]] | 0.001 | [docs/Research_bugs_agent_plan.md](docs/Research_bugs_agent_plan.md) | L1 |
| 84 | [[Product Requirements Document (PRD) - Research Bugs Agent]] | 0.001 | [docs/Research_bugs_agent_prd.md](docs/Research_bugs_agent_prd.md) | L1 |
| 85 | [[Implementation Plan - Reverse Engineering Agent]] | 0.001 | [docs/Reverse_engineering_agent_plan.md](docs/Reverse_engineering_agent_plan.md) | L1 |
| 86 | [[Product Requirements Document (PRD) - Reverse Engineering Agent]] | 0.001 | [docs/Reverse_engineering_agent_prd.md](docs/Reverse_engineering_agent_prd.md) | L1 |
| 87 | [[Implementation Plan - Architectural Improvement Suggestions]] | 0.001 | [docs/Suggestions_plan.md](docs/Suggestions_plan.md) | L1 |
| 88 | [[Product Requirements Document (PRD) - Architectural Improvement Suggestions]] | 0.001 | [docs/Suggestions_prd.md](docs/Suggestions_prd.md) | L1 |
| 89 | [[Implementation Plan - Bridges Analysis]] | 0.001 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L1 |
| 90 | [[Product Requirements Document (PRD) - Bridges Analysis]] | 0.001 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L1 |
| 91 | [[.test_generate_report()]] | 0.001 | [tests/test_analyzer.py](tests/test_analyzer.py) | L111 |
| 92 | [[test_reverse_engineer.py]] | 0.001 | [tests/test_reverse_engineer.py](tests/test_reverse_engineer.py) | L1 |
| 93 | [[test_bugs.py]] | 0.001 | [tests/test_bugs.py](tests/test_bugs.py) | L1 |
| 94 | [[TestAnalyzer]] | 0.000 | [tests/test_analyzer.py](tests/test_analyzer.py) | L6 |
| 95 | [[Architectural Analysis and Bugs Found]] | 0.000 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L3 |
| 96 | [[Autonomous Research Agent (`run_agent.py`)]] | 0.000 | [README.md](README.md) | L17 |
| 97 | [[test_analyzer.py]] | 0.000 | [tests/test_analyzer.py](tests/test_analyzer.py) | L1 |
| 98 | [[.load_graph_node()]] | 0.000 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L37 |
| 99 | [[.test_extract_wiki_links()]] | 0.000 | [tests/test_extractor.py](tests/test_extractor.py) | L25 |
| 100 | [[.test_extract_markdown_links()]] | 0.000 | [tests/test_extractor.py](tests/test_extractor.py) | L35 |
| 101 | [[TestHubs]] | 0.000 | [tests/test_hubs.py](tests/test_hubs.py) | L5 |
| 102 | [[my_function()]] | 0.000 | [artifacts/BugsInPy/projects/PySnooper/verify.sh](artifacts/BugsInPy/projects/PySnooper/verify.sh) | L47 |
| 103 | [[SKILL.md]] | 0.000 | [.agents/skills/write-md/SKILL.md](.agents/skills/write-md/SKILL.md) | L1 |
| 104 | [[Guidelines for the Agent:]] | 0.000 | [.agents/skills/write-md/SKILL.md](.agents/skills/write-md/SKILL.md) | L10 |
| 105 | [[test_agent.py]] | 0.000 | [tests/test_agent.py](tests/test_agent.py) | L1 |
| 106 | [[graphify.md]] | 0.000 | [.agents/rules/graphify.md](.agents/rules/graphify.md) | L1 |
| 107 | [[Todo List]] | 0.000 | [docs/Centrality_todo.md](docs/Centrality_todo.md) | L1 |
| 108 | [[Centrality (Subject 8)]] | 0.000 | [reports/Centrality_test.md](reports/Centrality_test.md) | L1 |
| 109 | [[Skill: Write MD (Orchestrated Pipeline)]] | 0.000 | [.agents/skills/write-md/SKILL.md](.agents/skills/write-md/SKILL.md) | L6 |
| 110 | [[Skill: Write Plan]] | 0.000 | [.agents/skills/write-plan/SKILL.md](.agents/skills/write-plan/SKILL.md) | L6 |
| 111 | [[Skill: Write PRD]] | 0.000 | [.agents/skills/write-prd/SKILL.md](.agents/skills/write-prd/SKILL.md) | L6 |
| 112 | [[Skill: Write TODO]] | 0.000 | [.agents/skills/write-todo/SKILL.md](.agents/skills/write-todo/SKILL.md) | L6 |
| 113 | [[run_test.sh]] | 0.000 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh) | L1 |
| 114 | [[run_test.sh script]] | 0.000 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/run_test.sh) | L1 |
| 115 | [[setup.sh]] | 0.000 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh) | L1 |
| 116 | [[setup.sh script]] | 0.000 | [artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh](artifacts/BugsInPy/projects/PySnooper/bugs/1/setup.sh) | L1 |
| 117 | [[verify.sh]] | 0.000 | [artifacts/BugsInPy/projects/PySnooper/verify.sh](artifacts/BugsInPy/projects/PySnooper/verify.sh) | L1 |
| 118 | [[verify.sh script]] | 0.000 | [artifacts/BugsInPy/projects/PySnooper/verify.sh](artifacts/BugsInPy/projects/PySnooper/verify.sh) | L1 |
| 119 | [[fuzz_target.py]] | 0.000 | [artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py](artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py) | L1 |
| 120 | [[fuzz()]] | 0.000 | [artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py](artifacts/BugsInPy/projects/black/bugs/4/fuzz_target.py) | L7 |
| 121 | [[update_readme.sh]] | 0.000 | [artifacts/BugsInPy/update_readme.sh](artifacts/BugsInPy/update_readme.sh) | L1 |
| 122 | [[update_readme.sh script]] | 0.000 | [artifacts/BugsInPy/update_readme.sh](artifacts/BugsInPy/update_readme.sh) | L1 |
| 123 | [[__init__.py]] | 0.000 | [src/main/agent/__init__.py](src/main/agent/__init__.py) | L1 |
| 124 | [[.centrality_node()]] | 0.000 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L43 |
| 125 | [[.bridges_node()]] | 0.000 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L69 |
| 126 | [[.compile_report_node()]] | 0.000 | [src/main/agent/workflow.py](src/main/agent/workflow.py) | L122 |
| 127 | [[Identifies nodes with high ratio of cross-community connections.]] | 0.000 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L5 |
| 128 | [[Identifies God Classes/Monoliths based on node degree.]] | 0.000 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L41 |
| 129 | [[Helper to safely read file content.]] | 0.000 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L60 |
| 130 | [[Scans files for local memory session stores without distributed persistence.]] | 0.000 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L72 |
| 131 | [[Checks for automated retry mechanisms lacking exponential backoff or jitter.]] | 0.000 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L109 |
| 132 | [[Detects network requests (requests.get/post) that miss the timeout argument.]] | 0.000 | [src/main/bugs/evaluators.py](src/main/bugs/evaluators.py) | L147 |
| 133 | [[Evaluates rules and generates the architectural bugs report.]] | 0.000 | [src/main/bugs/reporter.py](src/main/bugs/reporter.py) | L11 |
| 134 | [[bugs_analyzer.py]] | 0.000 | [src/main/bugs_analyzer.py](src/main/bugs_analyzer.py) | L1 |
| 135 | [[Parses basic YAML frontmatter from markdown content.]] | 0.000 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L4 |
| 136 | [[Extracts all wiki-links of the form [[Node Name]] from the content.]] | 0.000 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L23 |
| 137 | [[Extracts all relative internal markdown links.]] | 0.000 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L30 |
| 138 | [[Extracts and merges wiki-links and markdown links.]] | 0.000 | [src/main/centrality/extractor.py](src/main/centrality/extractor.py) | L43 |
| 139 | [[Calculates the degree (connections) of each node.         Returns a dict mapping]] | 0.000 | [src/main/centrality/graph.py](src/main/centrality/graph.py) | L155 |
| 140 | [[Generates the Centrality.md report based on the computed graph degrees.]] | 0.000 | [src/main/centrality/reporter.py](src/main/centrality/reporter.py) | L4 |
| 141 | [[centrality_analyzer.py]] | 0.000 | [src/main/centrality_analyzer.py](src/main/centrality_analyzer.py) | L1 |
| 142 | [[Calculates Betweenness Centrality for all nodes in the graph using Brandes' algo]] | 0.000 | [src/main/hubs/analyzer.py](src/main/hubs/analyzer.py) | L2 |
| 143 | [[Generates the Hubs.md report listing ranked bottleneck nodes.]] | 0.000 | [src/main/hubs/reporter.py](src/main/hubs/reporter.py) | L5 |
| 144 | [[.scan()]] | 0.000 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L10 |
| 145 | [[.scan_file_node()]] | 0.000 | [src/main/reverse_engineer/ast_scanner.py](src/main/reverse_engineer/ast_scanner.py) | L26 |
| 146 | [[Groups modules by top-level package and creates cross-package flowchart links.]] | 0.000 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L2 |
| 147 | [[Constructs class definitions, methods, inheritance, and compositions in Mermaid]] | 0.000 | [src/main/reverse_engineer/mapper.py](src/main/reverse_engineer/mapper.py) | L34 |
| 148 | [[Assembles the block diagram, OOP schema, and textual descriptions into a markdow]] | 0.000 | [src/main/reverse_engineer/reporter.py](src/main/reverse_engineer/reporter.py) | L5 |
| 149 | [[run_agent.py]] | 0.000 | [src/main/run_agent.py](src/main/run_agent.py) | L1 |
| 150 | [[run_reverse_engineer.py]] | 0.000 | [src/main/run_reverse_engineer.py](src/main/run_reverse_engineer.py) | L1 |
| 151 | [[Translates parsed categories of architectural bugs to a list of suggestions]] | 0.000 | [src/main/suggestions/mapper.py](src/main/suggestions/mapper.py) | L2 |
| 152 | [[Parses the Bugs.md report and returns a dict mapping bug categories (1-5) to a l]] | 0.000 | [src/main/suggestions/parser.py](src/main/suggestions/parser.py) | L5 |
| 153 | [[Builds the Suggestions.md report table mapping defects to Solution Architecture]] | 0.000 | [src/main/suggestions/reporter.py](src/main/suggestions/reporter.py) | L5 |
| 154 | [[suggestions_generator.py]] | 0.000 | [src/main/suggestions_generator.py](src/main/suggestions_generator.py) | L1 |
| 155 | [[.test_agent_workflow_execution()]] | 0.000 | [tests/test_agent.py](tests/test_agent.py) | L15 |
| 156 | [[.test_graph_degrees()]] | 0.000 | [tests/test_analyzer.py](tests/test_analyzer.py) | L7 |
| 157 | [[.test_load_from_json()]] | 0.000 | [tests/test_analyzer.py](tests/test_analyzer.py) | L55 |
| 158 | [[graphify]] | 0.000 | [.agents/rules/graphify.md](.agents/rules/graphify.md) | L6 |
| 159 | [[Workflow: graphify]] | 0.000 | [.agents/workflows/graphify.md](.agents/workflows/graphify.md) | L6 |
| 160 | [[Features]] | 0.000 | [README.md](README.md) | L5 |
| 161 | [[Usage]] | 0.000 | [README.md](README.md) | L25 |
| 162 | [[BugsInPy]] | 0.000 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L1 |
| 163 | [[Steps to set up BugsInPy]] | 0.000 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L5 |
| 164 | [[Use Docker]] | 0.000 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L11 |
| 165 | [[BugsInPy Command]] | 0.000 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L32 |
| 166 | [[Example BugsInPy Command]] | 0.000 | [artifacts/BugsInPy/README.md](artifacts/BugsInPy/README.md) | L43 |
| 167 | [[bugs_we_found.md]] | 0.000 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L1 |
| 168 | [[1. Central Nodes (Degree Centrality - Subject 8)]] | 0.000 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L7 |
| 169 | [[2. Hubs (Betweenness Centrality - Subject 10)]] | 0.000 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L23 |
| 170 | [[3. Bridge Nodes (Cross-Community Links)]] | 0.000 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L39 |
| 171 | [[4. Architectural Bugs and Anti-Patterns Found]] | 0.000 | [artifacts/BugsInPy/result/bugs_we_found.md](artifacts/BugsInPy/result/bugs_we_found.md) | L48 |
| 172 | [[Bridges_plan.md]] | 0.000 | [docs/Bridges_plan.md](docs/Bridges_plan.md) | L1 |
| 173 | [[Bridges_prd.md]] | 0.000 | [docs/Bridges_prd.md](docs/Bridges_prd.md) | L1 |
| 174 | [[Bridges_todo.md]] | 0.000 | [docs/Bridges_todo.md](docs/Bridges_todo.md) | L1 |
| 175 | [[Todo List - Bridges Analysis]] | 0.000 | [docs/Bridges_todo.md](docs/Bridges_todo.md) | L1 |
| 176 | [[Bugs_plan.md]] | 0.000 | [docs/Bugs_plan.md](docs/Bugs_plan.md) | L1 |
| 177 | [[Bugs_prd.md]] | 0.000 | [docs/Bugs_prd.md](docs/Bugs_prd.md) | L1 |
| 178 | [[Bugs_todo.md]] | 0.000 | [docs/Bugs_todo.md](docs/Bugs_todo.md) | L1 |
| 179 | [[Todo List - Architectural Bugs Detection]] | 0.000 | [docs/Bugs_todo.md](docs/Bugs_todo.md) | L1 |
| 180 | [[Centrality_plan.md]] | 0.000 | [docs/Centrality_plan.md](docs/Centrality_plan.md) | L1 |
| 181 | [[Centrality_prd.md]] | 0.000 | [docs/Centrality_prd.md](docs/Centrality_prd.md) | L1 |
| 182 | [[Centrality_todo.md]] | 0.000 | [docs/Centrality_todo.md](docs/Centrality_todo.md) | L1 |
| 183 | [[Hubs_plan.md]] | 0.000 | [docs/Hubs_plan.md](docs/Hubs_plan.md) | L1 |
| 184 | [[Hubs_prd.md]] | 0.000 | [docs/Hubs_prd.md](docs/Hubs_prd.md) | L1 |
| 185 | [[Hubs_todo.md]] | 0.000 | [docs/Hubs_todo.md](docs/Hubs_todo.md) | L1 |
| 186 | [[Todo List - Hubs Analysis]] | 0.000 | [docs/Hubs_todo.md](docs/Hubs_todo.md) | L1 |
| 187 | [[Research_bugs_agent_plan.md]] | 0.000 | [docs/Research_bugs_agent_plan.md](docs/Research_bugs_agent_plan.md) | L1 |
| 188 | [[Research_bugs_agent_prd.md]] | 0.000 | [docs/Research_bugs_agent_prd.md](docs/Research_bugs_agent_prd.md) | L1 |
| 189 | [[Research_bugs_agent_todo.md]] | 0.000 | [docs/Research_bugs_agent_todo.md](docs/Research_bugs_agent_todo.md) | L1 |
| 190 | [[Todo List - Research Bugs Agent]] | 0.000 | [docs/Research_bugs_agent_todo.md](docs/Research_bugs_agent_todo.md) | L1 |
| 191 | [[Reverse_engineering_agent_plan.md]] | 0.000 | [docs/Reverse_engineering_agent_plan.md](docs/Reverse_engineering_agent_plan.md) | L1 |
| 192 | [[Reverse_engineering_agent_prd.md]] | 0.000 | [docs/Reverse_engineering_agent_prd.md](docs/Reverse_engineering_agent_prd.md) | L1 |
| 193 | [[Reverse_engineering_agent_todo.md]] | 0.000 | [docs/Reverse_engineering_agent_todo.md](docs/Reverse_engineering_agent_todo.md) | L1 |
| 194 | [[Todo List - Reverse Engineering Agent]] | 0.000 | [docs/Reverse_engineering_agent_todo.md](docs/Reverse_engineering_agent_todo.md) | L1 |
| 195 | [[Suggestions_plan.md]] | 0.000 | [docs/Suggestions_plan.md](docs/Suggestions_plan.md) | L1 |
| 196 | [[Suggestions_prd.md]] | 0.000 | [docs/Suggestions_prd.md](docs/Suggestions_prd.md) | L1 |
| 197 | [[Suggestions_todo.md]] | 0.000 | [docs/Suggestions_todo.md](docs/Suggestions_todo.md) | L1 |
| 198 | [[Todo List - Architectural Improvement Suggestions]] | 0.000 | [docs/Suggestions_todo.md](docs/Suggestions_todo.md) | L1 |
| 199 | [[PLAN.md]] | 0.000 | [docs/instructions/PLAN.md](docs/instructions/PLAN.md) | L1 |
| 200 | [[PRD.md]] | 0.000 | [docs/instructions/PRD.md](docs/instructions/PRD.md) | L1 |
| 201 | [[TODO.md]] | 0.000 | [docs/instructions/TODO.md](docs/instructions/TODO.md) | L1 |
| 202 | [[research_question.md]] | 0.000 | [docs/research_question.md](docs/research_question.md) | L1 |
| 203 | [[Research Questions]] | 0.000 | [docs/research_question.md](docs/research_question.md) | L1 |
| 204 | [[Centrality_test.md]] | 0.000 | [reports/Centrality_test.md](reports/Centrality_test.md) | L1 |
| 205 | [[Central Nodes in BugsInPy]] | 0.000 | [reports/Centrality_test.md](reports/Centrality_test.md) | L5 |
