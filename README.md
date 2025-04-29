# AI Delivery Engine

End-to-end, tiered governance and automated assurance for AI-accelerated software delivery.

---

## Why Now?

Modern AI coding assistants (e.g. **Cursor**, **Winsurf**, **GitHub Copilot**) can scaffold an entire repository in minutes.  
That velocity is a double-edged sword:

* Pros — dramatic reduction in boilerplate and prototyping overhead; unleashes unprecedented productivity, fuels rapid innovation, and unlocks unknown upside with incredible potential.
* Cons — unchecked drift, security holes, compliance gaps, and potential IP infringement.

The AI Delivery Engine provides the **professional management layer** that keeps this firepower under control — so you ship fast *and* meet engineering standards.

## Integrations

Use these AI coding tools to apply the Delivery Engine in your workflow:

- **Cursor**
- **Winsurf**
- **GitHub Copilot**
- Any LLM-based IDE (via provided prompts and scripts)

---

## Engine Overview

The Delivery Engine consists of two tightly integrated cores that work in a continuous loop:

- **Governance Core (Define)** — Maintains the living contract for development: it keeps the Codebase Guide up to date, drafts versioned Scope Documents outlining goals and acceptance criteria, and applies Context Wrappers that enforce tier-specific engineering standards.
- **Assurance Core (Verify)** — Provides structured verification: human reviews align implementation to scope, automated tests validate functional requirements, and LLM-driven structural diffs ensure documentation and code remain in sync.

By continuously defining intentions and verifying reality, the Delivery Engine drives fast, compliant, and auditable AI-assisted software delivery.

All execution occurs in a **Docker-first**, IDE-contained pipeline—scoping through shipping lives inside this mono-repo, guaranteeing identical behaviour across dev, CI, and production.

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
7. **Privacy & Telemetry-Off** — All work and data stay inside the repo; outbound telemetry is disabled unless explicitly permitted.

---

## Workflow Overview

> The Delivery Engine moves in a six-stage, repeatable cycle that pairs Governance definition with Assurance verification **— all inside the IDE workspace and this mono-repo.**

| Stage | Purpose |
|-------|---------|
| **Scope** | Define goals and acceptance criteria in a versioned **in-repo** Scope Document |
| **Engine Setup** | Select Delivery Tier, load Context Wrapper, ensure Codebase Guide is accurate |
| **Modular Build** | Implement features in small branches using AI prompts within governance guardrails |
| **Governance Check** | Run Assurance Core checks (human review, LLM diff, automated tests) until binary compliance passes |
| **Ship** | Merge & release via tier-appropriate CI/CD |
| **Repeat** | Start the next scoped cycle, upgrading tiers as risk/scale grows |

A fuller explanation lives in [`docs/workflow.md`](docs/workflow.md).

---

## Where to Start

1. **Read the Overview** — Start with [`docs/introduction.md`](docs/introduction.md) for an end-to-end orientation.
2. **Understand the Engine** — Dive into [`docs/theory_of_operation.md`](docs/theory_of_operation.md) to see how Governance and Assurance interact.
3. **Follow the Workflow** — See the high-level roll-up in [`docs/workflow.md`](docs/workflow.md).
4. **Pick Your Tier** — Select a Delivery Tier in [`docs/delivery_tiers.md`](docs/delivery_tiers.md) and load its Context Wrapper.
5. **Create Scope & Guide** — Scaffold your first Scope Document (`docs/scopes/v0.x.0.md`) and update `core/codebase_guide.md`.

After those five steps you're ready to clone, build, and start shipping.

---