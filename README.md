# AI Delivery Engine

Lightweight, binary governance **and** assurance for AI-assisted software delivery.

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

Assurance = **living verification of truth**.

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
3. **Tiers Drive Strictness** — Higher Tier → stricter Context Wrapper.  
4. **Simplicity is Power** — No meta-frameworks or speculative complexity.  
5. **Docker-First Discipline** — Runs the same everywhere, or fails early.

---

## Quickstart

```bash
# clone & enter
git clone <repo>
cd ai_delivery_framework

# build baseline image
docker compose build
```

1. Create a **Scope Document**: `docs/scope/v0.x.y.md`  
2. Write the **Codebase Guide**: `docs/codebase_guide.md`  
3. Choose or author a **Context Wrapper**: `docs/meta/context_wrapper.md`  
4. Run Governance & Assurance checks:
   - Human review: scope ↔︎ features.
   - LLM prompts in `prompts/` or `scripts/`.
   - CI tests inside Docker.

---

## Repository Skeleton

```
/docs
   /scope
       v0.1.0.md
   /meta
       context_wrapper.md
   codebase_guide.md
/prompts
   compare_scope_to_codebase.md
   check_context_wrapper_compliance.md
/src
   (application code)
```

---

## Why It Matters

Unchecked AI-generated code drifts fast. The AI Delivery Engine keeps:

- Scope, documentation, and code in **permanent alignment**
- Quality **enforceable** across Delivery Tiers
- Delivery **traceable, auditable, and consistent**

---

## Status

**v0.1.0** — actively refined through real-world use.

Contributions and feedback are welcome.