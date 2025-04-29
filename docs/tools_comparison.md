## Tools Comparison: Cursor vs. GitHub Copilot

This document evaluates how well two popular AI development assistants integrate with the **AI Delivery Engine** established in this repository. Each feature is mapped directly to a Delivery Engine requirement, then scored for each tool.

Legend: ✓ = fully supported  |  ~ = partly/indirectly supported  |  ✗ = not supported

| # | Feature / Requirement | Why It Matters to Governance ↔ Assurance Engine | Cursor | GitHub Copilot |
|---|-----------------------|-----------------------------------------------|:------:|:-------------:|
|1|**Context Wrapper Injection**|Governance Core standards must ride with every prompt.|✓|✗|
|2|**Custom System Directives**|Allows repository-specific rules (tiers, compliance gates).|✓|✗|
|3|**Semantic Multi-File Retrieval**|Assurance Core needs accurate, on-demand code context.|✓|~|
|4|**Rule-based Conversation Control**|Engine requires deterministic behaviour; rules must bind the assistant.|✓|✗|
|5|**Tier-Driven Strictness Toggle**|Supports graduated enforcement without code changes.|✓|✗|
|6|**Assurance Test Hooks**|Seamless execution of unit/integration tests from the chat.|~|✗|
|7|**Docker-First Workflow Support**|Reproducible builds & tests across environments.|~|✗|
|8|**Local / Private Operation**|Sensitive codebases may forbid cloud completion.|✓ (self-host option)|✗|
|9|**Structured Diff Visualisation**|Rapid drift detection between intent and reality.|✓|~|
|10|**CLI / Automation APIs**|Automate Governance ↔ Assurance loops outside the IDE.|✓|✗|

### Summary

Cursor currently aligns more closely with the Delivery Engine's disciplined, rules-first philosophy. GitHub Copilot accelerates boilerplate generation but lacks the mechanisms needed to enforce Governance standards or verify Assurance outcomes.

Future assessments should revisit this matrix periodically, as both tools evolve. 