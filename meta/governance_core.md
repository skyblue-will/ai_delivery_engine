# **Governance Core — AI Delivery Engine**

---

## **Overview**

The AI Delivery Engine is governed by three active, living mechanisms:

- A continuously updated map of the codebase's current structure (`codebase_guide.md`)
- A versioned plan for each next targeted iteration (`v0.x.0.md`, `v0.x.1.md`, etc.)
- Context Wrappers that enforce development discipline at each stage based on the assigned Delivery Tier

Together, these components ensure that every project built using the engine remains **structured, controlled, and continuously improving** — without drifting into chaos or technical debt.

---

## **1. Codebase Guide (`codebase_guide.md`)**

**Purpose:**  
The single source of truth describing the *current* state of the codebase.

**Characteristics:**
- Version-controlled alongside the codebase.
- Updated only after real, approved changes are merged.
- Every section must map directly to real code — no speculative or aspirational content.
- Acts as the foundation for onboarding, auditing, and further development.

**Responsibilities:**
- Whenever major features, refactors, or reorganisations occur, the Codebase Guide must be updated.
- If an LLM or developer proposes a major change, they must explicitly update or note updates needed in the Codebase Guide.

---

## **2. Versioned Scope Documents (`v0.x.0.md`)**

**Purpose:**  
A structured, versioned record of the *next planned iteration* of the project.

**Characteristics:**
- Clearly defines the goals, features, refactors, compliance upgrades, and improvements targeted for a specific semantic version.
- Defines the boundary of what \"done\" means for each version.
- Written before major iteration begins; reviewed and locked once approved.

**Responsibilities:**
- New development is guided by the current active Scope Document.
- Any scope creep or divergence must result in an updated Scope Document — not informal project drift.
- Scope Documents should be auditable against the resulting commits and PRs.

---

## **3. Context Wrappers**

**Purpose:**  
An enforced AI system prompt (or equivalent ruleset) that governs how development is approached during an iteration.

**Characteristics:**
- Sets standards for modularity, testing, compliance, documentation, and CI/CD discipline.
- Tailored to the Delivery Tier assigned to the project or iteration (Tier 1–5).
- Applied inside tools like Cursor, Windsurf, Continue, or any LLM coding interface.
- Explicitly defines how AI outputs must be structured, verified, and documented.

**Responsibilities:**
- Context Wrapper must be activated at project/iteration start.
- Any override or adjustment to the Context Wrapper must be documented and reviewed.
- Context Wrappers evolve as the engine matures.

---

# **Governance Loop**

The three governance elements operate in a continuous loop:

| Phase | Action |
|:------|:-------|
| Plan | Write a versioned Scope Document (`v0.x.0.md`) |
| Build | Enforce rules via Context Wrapper during development |
| Update | Update Codebase Guide (`codebase_guide.md`) to reflect changes |
| Reflect | Lessons learned inform the next Scope Document |

This loop ensures every project evolves deliberately — with **clear intentions, real outputs, and constant accountability**.

---

# **Summary**

> **The Codebase Guide, Scope Documents, and Context Wrappers together form the beating heart of the AI Delivery Engine’s discipline, agility, and long-term scalability.**

By respecting and updating these elements continuously, teams maintain momentum without losing structure or trust.