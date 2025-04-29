# AI Delivery Engine

Lightweight, binary governance **and** assurance for AI-assisted software delivery.

---

## Why Now?

Modern AI coding assistants (e.g. **Cursor**, **Winsurf**, GitHub Copilot Chat) can scaffold an entire repository in minutes.  
That velocity is a double-edged sword:

* Pros — dramatic reduction in boilerplate and prototype time.
* Cons — unchecked drift, security holes, and compliance gaps appear just as quickly.
* Cons — potential *IP infringement* risk when provenance metadata is missing or obscured.

The AI Delivery Engine provides the **professional management layer** that keeps this firepower under control — so you ship fast *and* meet engineering standards.

## Integrations

Use these AI coding tools to apply the Delivery Engine in your workflow:

- **Cursor**
- **Winsurf**
- Any LLM-based IDE (via provided prompts and scripts)

---

## Engine Overview

The Delivery Engine consists of two tightly integrated cores that work in a continuous loop:

- **Governance Core (Define)** — Maintains the living contract for development: it keeps the Codebase Guide up to date, drafts versioned Scope Documents outlining goals and acceptance criteria, and applies Context Wrappers that enforce tier-specific engineering standards.
- **Assurance Core (Verify)** — Provides structured verification: human reviews align implementation to scope, automated tests validate functional requirements, and LLM-driven structural diffs ensure documentation and code remain in sync.

By continuously defining intentions and verifying reality, the Delivery Engine drives fast, compliant, and auditable AI-assisted software delivery.

All execution occurs in a **Docker-first** pipeline to guarantee identical behaviour across dev, CI, and production.

---

## Governance Core (Define)

| Component | Purpose |
|-----------|---------|
| **Scope Document** | Declares intended features and boundaries (versioned) |
| **Codebase Guide** | Maps the current codebase (versioned) |
| **Context Wrapper** | Specifies mandatory engineering standards (Tier-aware) |

Governance = **present reality** (gemba) with **defined destination** through **enforced standards**.

---

## Assurance Core (Verify)

| Check | Purpose |
|-------|---------|
| **Scope Alignment — Human** | Confirm delivered features match scoped intent |
| **Structural Diff — LLM** | Compare Scope, Guide, Codebase, and Standards |
| **Runtime Validation — Tests** | Automated tests enforce functional correctness per Tier |

Assurance = **action-driven verification** ("Are we there yet?") powering progress via **human**, **LLM**, and **testing**.

---

## Delivery Tiers

The active **Tier** selects *which* standards apply — never *how* strictly they are enforced. Compliance is always **pass/fail**.

| Tier | Typical Use | Standards Snapshot |
|------|-------------|--------------------|
| 1 | Hobby / Prototype | Linting, smoke tests |
| 3 | Growth / Team | Full test suite, code-quality gates |
| 5 | Enterprise | Mutation testing, provenance, SBOM |

---

## Core Principles

1. **Reflect Reality** — Documents match the actual system, always.  
2. **Compliance is Binary** — Pass or fail; no "mostly compliant."  
3. **Tiers Control Standards** — The active Tier selects *which* standards apply; enforcement is always binary.  
4. **Simplicity is Power** — No meta-frameworks or speculative complexity.  
5. **Docker-First Discipline** — Runs the same everywhere, or fails early.
6. **IP Risk Mitigation** — Watermarking and provenance tracking ensure every AI-generated artifact carries verifiable attribution, preventing IP infringement.

---

## Where to Start

1. **Read the Overview** — Start with [`docs/introduction.md`](docs/introduction.md) for an end-to-end orientation.
2. **Understand the Engine** — Dive into [`docs/theory_of_operation.md`](docs/theory_of_operation.md) to see how Governance and Assurance interact.
3. **Follow the Workflow** — Use the high-level step-by-step in [`meta/full_workflow.md`](meta/full_workflow.md).
4. **Pick Your Tier** — Select a Delivery Tier in [`docs/delivery_tiers.md`](docs/delivery_tiers.md) and load its Context Wrapper.
5. **Create Scope & Guide** — Scaffold your first Scope Document (`docs/scopes/v0.x.0.md`) and update `core/codebase_guide.md`.

After those five steps you're ready to clone, build, and start shipping.

---