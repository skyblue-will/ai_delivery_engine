# AI Delivery Engine

Lightweight, binary governance **and** assurance for AI-assisted software delivery.

---

## Why Now?

Modern AI coding assistants (e.g. **Cursor**, **Winsurf**, GitHub Copilot Chat) can scaffold an entire repository in minutes.  
That velocity is a double-edged sword:

* Pros — dramatic reduction in boilerplate and prototype time.
* Cons — unchecked drift, security holes, and compliance gaps appear just as quickly.

The AI Delivery Engine provides the **professional management layer** that keeps this firepower under control — so you ship fast *and* meet engineering standards.

## Integrations

The Engine is editor-agnostic but already optimised for:

| Tool | How the Engine Integrates |
|------|---------------------------|
| **Cursor** | Loads Context Wrapper into every prompt; enforces Tier rules in real-time |
| **Winsurf** | Applies Governance + Assurance prompts while generating/refactoring code |
| Any LLM IDE | Use the provided prompts/scripts to inject the same governance controls |

As new tools emerge, extending the Engine is just a matter of adding a tailored Context Wrapper or CI check.

---

## Engine Overview

Governance Core **defines** what to build and how it must be built.  
Assurance Core **verifies** that reality matches that definition.  
Their continuous interaction is the **Delivery Engine**.

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

---

## Where to Start

1. **Read the Overview** — Start with [`docs/introduction.md`](docs/introduction.md) for an end-to-end orientation.
2. **Understand the Engine** — Dive into [`