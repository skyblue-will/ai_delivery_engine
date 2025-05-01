# **Assurance Core — AI Product Delivery Engine**

---

## **Overview**

The Assurance Core works in **lock-step** with the Governance Core:

* Governance **defines** intention (Scope → Context → Guide).
* Assurance **verifies** reality (Code → Tests → Docs).

This closed loop ensures the project stays continuously aligned with its defined goals, standards, and compliance obligations.

> **Binary Compliance** — A deliverable either passes or fails. "Mostly compliant" is a fail.
>
> **Tier-Aware** — Which checks are required is determined by the active Delivery Tier (1–5). Strictness is never lowered.
>
> **Watermark Enforcement** — From **Tier 2 upward**, every AI-generated artifact must include provenance watermarking; Assurance validates this automatically.

---

## **1. Human Verification**

| Purpose | Mechanism | Trigger |
|---------|-----------|---------|
| Confirm implementation matches scope intent | Manual PR review, paired walkthroughs | Before merge to `main` |

*Reviewers use the Scope Document checklist to ensure features, acceptance criteria, and non-functional requirements are met.*

---

## **2. LLM Structural Diff**

| Purpose | Mechanism | Trigger |
|---------|-----------|---------|
| Detect drift between documentation, code, and standards | Run `prompts/diff_codebase_guide_vs_reality.md` + `prompts/compare_scope_to_codebase.md` | Nightly or on demand |

LLM diff checks:

1. Codebase ↔ **Codebase Guide**
2. Implemented features ↔ **Scope Document**
3. Standards adherence ↔ **Context Wrapper**
4. **Watermark** presence in AI-generated files (Tier ≥ 2)

Any deviation produces a FAIL report that blocks release until resolved.

---

## **3. Automated Testing**

| Purpose | Mechanism | Tier Threshold |
|---------|-----------|----------------|
| Enforce functional correctness, security, and quality gates | Unit, integration, mutation tests; static analysis; secret scanning | Coverage & depth scale by tier |

CI pipeline stages (example Tier 3):

```
lint → test → mutation → sbom + scan → diff-check → build
```

Failure anywhere breaks the build.

---

## **Assurance Loop**

| Stage | Action |
|-------|--------|
| Plan | Derive test matrix and diff checks from Scope & Context Wrapper |
| Build | Run tests & diff checks on every push / PR |
| Merge | Human reviewers gate merges based on PASS/FAIL |
| Release | CI signs artifacts; watermark validation passes |
| Reflect | Results feed back into next Scope & Guide update |

---

## **Responsibilities**

* Configure CI pipelines to run all tier-required checks.
* Keep prompts (`prompts/`) updated as standards evolve.
* Ensure reviewers have clear PASS/FAIL criteria.
* Document any temporary overrides and schedule follow-up.

---

## **Summary**

The Assurance Core provides **action-driven verification** that reality matches intention — continuously and unequivocally.   
By combining human insight, LLM analysis, and automated tests, it prevents drift, enforces watermark provenance, and maintains trust in every release. 