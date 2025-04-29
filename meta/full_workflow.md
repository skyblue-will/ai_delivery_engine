# AI Project Full Workflow

## Purpose
This document defines the end-to-end workflow for delivering technology solutions with an **AI-first delivery approach** using the **AI Delivery Framework**. It maps each lifecycle phase to the framework's governance artefacts—**Codebase Guide**, **Scope Documents**, and **Context Wrappers**—so teams can maintain engineering discipline, compliance, and executive-grade transparency.

> **When to use this file**: Refer to it as the canonical, high-level playbook when kicking off a new project or auditing progress against framework standards.

### Engine Alignment

Every phase is powered by the Delivery Engine's twin cores:

* **Governance Core** — *defines* present reality, desired destination, and mandatory standards.
* **Assurance Core** — *verifies* that reality matches the definition through human review, LLM diff, and automated tests.

Compliance is always **binary** (pass/fail). Delivery Tiers scale *which* standards apply, never **how strictly** they are enforced.

### Pre-flight Checklist (Before Day-1 Code)

1. **Choose Delivery Tier** and load its Context Wrapper.
2. **Draft a Scope Document** (`v0.x.0.md`) capturing objectives, boundaries, and acceptance criteria.
3. **Create / Update the Codebase Guide** so it accurately reflects the starting codebase (or empty stub).
4. **Wire up CI** to run Assurance checks aligned with the selected tier.

---

## Table of Contents
1. [Discovery Phase](#discovery-phase)
2. [Planning Phase](#planning-phase)
3. [Development Phase](#development-phase)
4. [Testing Phase](#testing-phase)
5. [Deployment Phase](#deployment-phase)
6. [Monitoring Phase](#monitoring-phase)
7. [Summary](#summary)

---

## Discovery Phase

| Objective | Key Activities | Gov & Assurance Gates | Primary Outputs |
|-----------|----------------|-----------------------|-----------------|
| Validate that a digital/software solution is the right answer to the business problem, and if so, determine the appropriate approach. | • Stakeholder interviews<br>• Current-state analysis<br>• Process vs. technology assessment<br>• Data feasibility assessment | • Initial **Scope Document** stub created<br>• Compliance constraints (e.g., GDPR Lite) captured | • Discovery Report<br>• Initial Scope Document |

### Recommended AI Models
- **Primary**: GPT-4o (o3) - Excels at complex stakeholder insight analysis and business case validation
- **Alternative**: Claude 3.7 Opus - Strong reasoning capabilities for assessing alternative approaches

### Real-World Connection
The discovery artefacts ensure decision-makers have a clear **business case** before engineering resources are committed, including validation that a digital solution (vs. process change, policy, etc.) is actually needed.

---

## Planning Phase

| Objective | Key Activities | Gov & Assurance Gates | Primary Outputs |
|-----------|----------------|-----------------------|-----------------|
| Convert discovery insights into a scoped, budgeted, and time-boxed delivery plan. | • Define MVP vs. future scope<br>• Select Delivery Tier<br>• Establish success metrics<br>• Architecture & risk assessment | • `v0.x.0.md` plan drafted and approved<br>• Context Wrapper template selected | • Approved Version Plan (`v0.x.0.md`)<br>• Architecture Decision Records (ADRs)<br>• Updated Scope Document |

### Recommended AI Models
- **Primary**: Claude 3.7 Opus - Exceptional architecture reasoning and technical planning
- **Alternative**: GPT-4o - Strong for breaking down large initiatives into structured phases

### Compliance Note
Security and legal teams validate data-handling requirements _before_ development begins.

---

## Development Phase

| Objective | Key Activities | Gov & Assurance Gates | Primary Outputs |
|-----------|----------------|-----------------------|-----------------|
| Build the solution iteratively with disciplined, AI-assisted development practices. | • Implement features in short cycles (feature branches)<br>• Apply **Context Wrappers** based on Delivery Tier<br>• Continuous code review & linting<br>• Update **Codebase Guide** with each significant change | • Automated CI checks green<br>• Codebase Guide updated in PRs<br>• Scope creep flagged in weekly triage | • Incremental feature branches<br>• Updated Codebase Guide<br>• Technical documentation |

### Recommended AI Models
- **Primary**: Claude 3.7 Sonnet - Optimal balance of code quality and development speed
- **Alternative**: GPT-4o - Particularly strong for cross-language development and complex refactoring

### Framework Tie-in
Context Wrappers enforce branch discipline, test coverage thresholds, and documentation completeness, preventing drift from the approved plan.

---

## Testing Phase

| Objective | Key Activities | Gov & Assurance Gates | Primary Outputs |
|-----------|----------------|-----------------------|-----------------|
| Validate that the implementation meets functional, non-functional, and compliance requirements. | • Unit & integration testing<br>• Model performance validation<br>• Security & privacy audits | • Test matrices approved<br>• CI pipeline enforces required coverage<br>• Privacy impact assessment signed off | • Test Reports<br>• Model Evaluation Metrics<br>• Compliance Sign-off |

### Recommended AI Models
- **Primary**: Claude 3.5 Sonnet - Excels at generating comprehensive test cases
- **Alternative**: GPT-4o - Strong for security vulnerability analysis and test scenario generation

### Best Practice (2025)
Shift-left testing: integrate synthetic data generation for edge-case coverage early in development.

---

## Deployment Phase

| Objective | Key Activities | Gov & Assurance Gates | Primary Outputs |
|-----------|----------------|-----------------------|-----------------|
| Release the solution safely into the target environment with rollback capability. | • Infrastructure-as-Code (IaC) updates<br>• Blue/green or canary releases<br>• Release notes & change log | • Deployment runbooks reviewed<br>• Release approved by change authority | • Deployed artefacts<br>• Release Notes<br>• Updated runbooks |

### Recommended AI Models
- **Primary**: Claude 3.5 Sonnet - Effective for generating deployment scripts and release documentation
- **Alternative**: Llama 3 70B - Cost-effective for routine deployment assistance and runbook generation

### Compliance Trigger
Data residency and user-consent mechanisms go live; legal signs off on production deployment.

---

## Monitoring Phase

| Objective | Key Activities | Gov & Assurance Gates | Primary Outputs |
|-----------|----------------|-----------------------|-----------------|
| Ensure the solution remains reliable, performant, and compliant in production. | • Implement observability (logs, metrics, traces)<br>• Model drift detection<br>• Post-release incident reviews | • SLO dashboards reviewed weekly<br>• Monthly compliance health check | • Monitoring Dashboards<br>• Incident Reports<br>• Continuous Improvement Tasks |

### Recommended AI Models
- **Primary**: GPT-4o - Superior pattern recognition for anomaly detection and incident analysis
- **Alternative**: Claude 3.5 Sonnet - Strong for generating monitoring dashboards and SLO documentation

### Feedback Loop
Findings feed back into the **Planning** and **Development** phases for iterative improvement.

---

## Summary
The AI Project Full Workflow provides a disciplined, end-to-end roadmap anchored by the AI Delivery Framework's governance artefacts:

- **Codebase Guide**: Live technical truth-source.
- **Scope Documents & Version Plans**: Contract between business and engineering.
- **Context Wrappers**: Enforce delivery discipline commensurate with risk.

Follow this workflow to deliver solutions that are **scalable, compliant, and trusted by executives and engineers alike**. 