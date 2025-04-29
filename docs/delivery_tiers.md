# Delivery Tiers

The AI Delivery Engine employs a progressive rigor model that scales standards with project maturity and risk. This enables early-stage projects to move quickly while ensuring appropriate governance for production systems.

## Tier Structure

| Tier | Use Case | Standards Level | Context Wrapper |
|------|----------|-----------------|-----------------|
| **0 – Exploration** | Learning, chat-only exploration | None (no code committed) | [tier0_exploration_context_wrapper.md](../core/context_wrappers/tier0_exploration_context_wrapper.md) |
| **1 – Hobby** | Personal projects, internal proofs | Minimal | [tier1_hobby_context_wrapper.md](../core/context_wrappers/tier1_hobby_context_wrapper.md) |
| **2 – MVP** | Early user validation | Moderate | [tier2_mvp_context_wrapper.md](../core/context_wrappers/tier2_mvp_context_wrapper.md) |
| **3 – Beta** | Public pilots, initial scaling | High | [tier3_beta_context_wrapper.md](../core/context_wrappers/tier3_beta_context_wrapper.md) |
| **4 – Production** | Launched products | Comprehensive | [tier4_production_context_wrapper.md](../core/context_wrappers/tier4_production_context_wrapper.md) |
| **5 – Enterprise** | Regulated, high-security | Maximum | [tier5_enterprise_context_wrapper.md](../core/context_wrappers/tier5_enterprise_context_wrapper.md) |

## Binary Compliance Principle

**Important**: At all tiers, compliance is binary (pass/fail). Only the *level* of required standards changes by tier—never the strictness of enforcement.

A Tier 1 project with minimal standards must still meet 100% of Tier 1 requirements to be compliant.

## Key Dimensions by Tier

The Engine scales requirements across these dimensions:

| Dimension | Tier 1 | Tier 3 | Tier 5 |
|-----------|--------|--------|--------|
| **Testing** | Basic unit tests (20%) | Unit + Integration (70%) | Exhaustive (95%+) |
| **Security** | Basic practices | Automated scanning | Advanced threat modeling |
| **CI/CD** | Optional | Required | Multiple environments |
| **Documentation** | Basic README | Architecture docs | Compliance docs |
| **Observability** | Basic logging | Metrics | Distributed tracing |
| **Data Management** | SQLite | Data validation | Full data governance |

## Selecting Your Tier

Consider these factors when choosing a delivery tier:

1. **User Impact** — Who will use the system and what's at stake?
2. **Data Sensitivity** — What types of data will be processed?
3. **Scale Requirements** — Expected user/transaction volume?
4. **Regulatory Context** — Applicable compliance standards?
5. **Business Criticality** — Importance to operations?

Projects should upgrade tiers as they mature. Many successful products begin at Tier 1-2 and progressively adopt stricter standards as they scale.

## Tier Transition

When upgrading tiers:

1. Select the new Context Wrapper
2. Document the transition in the next Scope Document
3. Conduct a gap analysis using the [compliance checker](../prompts/check_context_wrapper_compliance.md)
4. Implement required standards to achieve binary compliance with the new tier

The Engine accelerates this transition by providing clear, executable standards at each tier. 