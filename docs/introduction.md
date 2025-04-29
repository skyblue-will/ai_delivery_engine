# Introduction

The AI Delivery Engine is a cohesive set of tools, standards, and feedback loops that lets you build software *fast* and *safely* with AI coding assistance. It lets developers tap AI coding speed without giving up traceability, security, or quality.

### Quick Summary

- **Velocity with Governance** — Ship faster while meeting security, compliance, and audit demands.
- **Binary Assurance** — A Governance Core *defines*, an Assurance Core *verifies*; no grey areas, only pass/fail.
- **Tiered Rigor** — Standards scale with risk: prototype today, regulated production tomorrow.
- **Tool & Cloud Agnostic** — Works with any language, any AI assistant, and enforces Docker-first consistency.

This document explains how the Engine works and when to use it.

---

## 1. Why the Engine Matters

Uncontrolled AI code generation creates audit, security, and reliability gaps. The Engine closes those gaps **without throttling delivery speed**.

The Engine delivers this through:

* A **Governance Core** defining **present reality**, **defined destination**, and **enforced standards**.
* An **Assurance Core** providing **action-driven verification** via human, LLM, and testing.
* **Delivery Tiers** that scale standards precisely with project risk.

---

## 2. Governance Core (Define)

| Component | Purpose | Maintained By |
|-----------|---------|--------------|
| **[Codebase Guide](../core/codebase_guide.md)** | Maps the **present reality** of the system. | Engineers after each merge |
| **[Scope Document](../core/scope_doc_template.md)** | Defines the **destination** for each release. | Product + Engineering before work |
| **Context Wrapper** | Specifies **standards** for the active Delivery Tier. | Prompt layer & CI/CD hooks |

These three components form a living contract that keeps AI-assisted work auditable and aligned with business goals.

---

## 3. Assurance Core (Verify)

| Check | Purpose | Verification Method |
|-------|---------|---------------------|
| **Scope Alignment** | Verify implementation matches scope | Human review with [prompts](../prompts/compare_scope_to_codebase.md) |
| **Structural Diff** | Compare Guide, Scope, Code & Standards | LLM analysis with [prompts](../prompts/diff_codebase_guide_vs_reality.md) |
| **Standards Compliance** | Verify Context Wrapper adherence | Automated tests with [checks](../prompts/check_context_wrapper_compliance.md) |

Assurance provides continuous verification that reality matches intent, driving progress through structured feedback.

---

## 4. Delivery Tiers (Binary Standards)

| Tier | Typical Use | Standards Profile |
|------|-------------|-------------------|
| 1 | Hobby / Prototype | Linting, smoke tests |
| 3 | Growth / Team | Full test suite, code-quality gates |
| 5 | Enterprise | Mutation testing, provenance, SBOM |

All tiers enforce standards in binary fashion - compliance is pass/fail, never "mostly compliant."

---

## 5. Target Audience

* **Individual developers & hobbyists** ready to move from side-project to production-ready code
* **Collaborating developers** seeking velocity with control
* **Startups** that must scale governance with product risk
* **Enterprises** requiring auditability and compliance in AI workflows

---

## 6. Supported AI Tools

The Engine integrates with AI-powered code editors including:

* **Cursor** - Uses the Governance Core to guide AI generation
* **Winsurf** - Leverages Context Wrappers for disciplined development
* Other AI coding assistants supporting custom context injection

---

## 7. Engine Workflow

```mermaid
graph TD
    A[Project Initialization] --> B[Scope Document Creation]
    B --> C[Context Wrapper Selection]
    C --> D[AI Augmented Development]
    D --> E[Verification Checks]
    E --> F[Deployment Pipeline]
    F --> G[Codebase Guide Update]
    G --> B
```

1. **Initialize** — Assess risk profile and set Delivery Tier
2. **Define Scope** — Document the destination in a versioned markdown file
3. **Apply Standards** — Load Context Wrapper enforcing tier-specific rules
4. **Build** — Generate code + tests via AI within defined standards
5. **Verify** — Run Assurance checks against all dimensions (scope, standards, structure)
6. **Deploy** — Ship via CI/CD with appropriate tier gates
7. **Update Guide** — Refresh [Codebase Guide](../core/codebase_guide.md) using [update prompt](../prompts/update_codebase_guide.md)

---

## 8. Core Principles

1. **Reflect Reality** — Documentation must mirror the actual system
2. **Compliance is Binary** — Pass or fail; no "mostly compliant"
3. **Tiers Drive Strictness** — Higher Tier = stricter standards
4. **Simplicity is Power** — No meta-frameworks or speculative complexity
5. **Docker-First** — Runs identically everywhere or fails fast

---

## 9. Getting Started

1. **Clone repository**
2. **Read** [Codebase Guide](../core/codebase_guide.md) and [Scope Template](../core/scope_doc_template.md)
3. **Set** your [Delivery Tier](delivery_tiers.md)
4. **Create** your first Scope Document (e.g., `v0.1.0.md`)
5. **Follow** the Engine workflow with appropriate Context Wrapper
6. **Update** the Codebase Guide after each significant change

---

## 10. Further Reading

| Topic | Document |
|-------|----------|
| Engine Theory | [Theory of Operation](theory_of_operation.md) |
| Full Workflow | [Full Workflow](../meta/full_workflow.md) |
| Roadmap | [Roadmap](../roadmap.md) |

For version history and change plans, see `roadmap.md`.