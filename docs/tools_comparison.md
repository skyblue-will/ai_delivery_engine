## Tools Comparison: Cursor vs. GitHub Copilot

This document evaluates how well two popular AI development assistants integrate with the **AI Delivery Engine** established in this repository. Each feature is mapped directly to a Delivery Engine requirement, then scored for each tool.

Legend: ✓ = fully supported  |  ~ = partly/indirectly supported  |  ✗ = not supported

| # | Feature / Requirement | Why It Matters to Governance ↔ Assurance Engine | Cursor | GitHub Copilot |
|---|-----------------------|-----------------------------------------------|:------:|:-------------:|
|1|**Persistent Context Wrapper**|Governance Core rules must accompany every prompt.|✓|~|
|2|**Custom System Directives**|Inject tier, compliance, or repo-specific policies.|✓|~|
|3|**Semantic Multi-File Retrieval**|Assurance Core needs full-repo reasoning to spot drift.|✓|~|
|4|**Rule-Based Conversation Control**|Deterministic behaviour; prevents rule slippage.|✓|✗|
|5|**Tier-Driven Strictness Toggle**|Switch enforcement levels without rewriting rules.|~|✗|
|6|**Assurance Test Hooks**|Run & surface test output directly from chat.|~|~|
|7|**Docker-First Workflow Support**|Facilitate container builds/tests inside the IDE.|~|~|
|8|**Local / Private Execution Option**|Operate in air-gapped or self-hosted mode.|~|✗|
|9|**Structured Diff / Patch Flow**|Highlights changes vs. intent; safe commit flow.|✓|~|
|10|**CLI / Automation APIs**|Trigger Governance ↔ Assurance loops from scripts.|~|~|

### Summary

Cursor currently aligns more closely with the Delivery Engine's disciplined, rules-first philosophy. GitHub Copilot accelerates boilerplate generation but lacks the mechanisms needed to enforce Governance standards or verify Assurance outcomes.

Future assessments should revisit this matrix periodically, as both tools evolve. 