# Architectural Bugs Report

This report summarizes critical architectural anti-patterns and defects detected in the codebase representation.

## 1. Tight Coupling (The Domino Effect)

No violations detected in this category.

## 2. The "God Class" / Monolith

| Node | Origin File | Location | Details | Fix Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| [[ResearchBugsAgentWorkflow]] | N/A | N/A | Class/module degree: 11 (exceeds threshold of 8) | Adhere to the Single Responsibility Principle; split functionality into discrete, domain-specific modules. |
| [[evaluators.py]] | N/A | N/A | Class/module degree: 8 (exceeds threshold of 8) | Adhere to the Single Responsibility Principle; split functionality into discrete, domain-specific modules. |
| [[BugsGraph]] | N/A | N/A | Class/module degree: 9 (exceeds threshold of 8) | Adhere to the Single Responsibility Principle; split functionality into discrete, domain-specific modules. |

## 3. Local State Dependency (Sticky Sessions)

No violations detected in this category.

## 4. Unbounded Retries (Thundering Herd)

No violations detected in this category.

## 5. Infinite Resource Waiting

No violations detected in this category.

