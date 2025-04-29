# AI Delivery Framework

**Lightweight Governance and Assurance for AI-Assisted Software Delivery**

---

## What This Framework Is

The **AI Delivery Framework** governs AI-assisted software projects using two tightly coupled cores:

- **Governance Core**: Defines what should be built and how it must be structured.
- **Assurance Core**: Checks that what exists matches what was defined.

This dialogue between Governance and Assurance drives clean, auditable, maintainable delivery — without heavyweight process.

All activity is executed inside a **Docker-first environment** to guarantee execution consistency from local to production.

---

## Governance Core

| Component          | Purpose                                    |
|:-------------------|:-------------------------------------------|
| **Scope Document**  | Defines what is being built (versioned)    |
| **Codebase Guide**  | Documents what exists (versioned)          |
| **Context Wrapper** | Defines required engineering standards    |

**Governance Core = Living Source of Truth.**

---

## Assurance Core

| Check | Purpose |
|:------|:--------|
| **Scope Alignment (Human)** | Manually verify that features match the scoped plan |
| **Structural Diff (LLM)** | LLM compares Scope, Codebase Guide, Actual Codebase, and Context Wrapper standards |
| **Runtime Validation (Tests)** | Automated tests confirm functional correctness per Delivery Tier requirements |

**Assurance Core = Living Verification Against Truth.**

---

## Delivery Tiers

Delivery Tiers determine which Context Wrapper standards apply, scaling with project complexity:

| Tier | Intended Use | Standards Profile |
|:-----|:-------------|:------------------|
| Tier 1 | Hobby/Prototype | Minimal basic standards |
| Tier 3 | Growth Project | Full testing, code quality enforcement |
| Tier 5 | Enterprise Delivery | Maximum compliance (e.g., mutation testing, provenance enforcement) |

**Compliance to the active Context Wrapper is always strict (pass/fail).**
Only the *level of required standards* changes by Tier.

---

## Quickstart

1. Create a Scope Document (`docs/scope/v0.x.0.md`)
2. Create a Codebase Guide (`docs/codebase_guide.md`)
3. Choose or define a Context Wrapper (`docs/meta/context_wrapper.md`)
4. Build inside a Docker-first workflow
5. Run regular Governance and Assurance checks

---

## Project Structure (Minimal)

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

Without structured governance, AI-driven development can easily drift into undocumented, unmaintainable chaos.

The AI Delivery Framework ensures:
- Codebases evolve predictably from scope
- Documentation tracks reality, not fantasy
- Quality remains enforceable across Tiers
- Delivery is traceable, auditable, and consistent

---

## Status

This framework is a work in progress (**v0.1.0**), actively refined through real-world application.

Contributions, testing, and feedback are welcome.