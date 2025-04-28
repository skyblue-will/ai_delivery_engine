# Delivery Tiers

The AI Delivery Framework uses a progressive rigor model that scales engineering discipline based on project maturity and risk. This aims to help early-stage projects move quickly while supporting appropriate standards for production systems.

## Tier Structure

| Tier | Use Case | Engineering Rigor | Context Wrapper |
|------|----------|-------------------|-----------------|
| **0 – Exploration** | Initial learning, chat-only exploration | None (no code committed) | [tier0_exploration_context_wrapper.md](../core/context_wrappers/tier0_exploration_context_wrapper.md) |
| **1 – Prototype** | Exploratory spikes, internal proofs | Minimal | [tier1_hobby_context_wrapper.md](../core/context_wrappers/tier1_hobby_context_wrapper.md) |
| **2 – MVP** | Early user validation | Moderate (GDPR Lite if personal data) | [tier2_mvp_context_wrapper.md](../core/context_wrappers/tier2_mvp_context_wrapper.md) |
| **3 – Beta** | Public pilots, early scaling | High | [tier3_beta_context_wrapper.md](../core/context_wrappers/tier3_beta_context_wrapper.md) |
| **4 – Production** | Launched products | Full | [tier4_production_context_wrapper.md](../core/context_wrappers/tier4_production_context_wrapper.md) |
| **5 – Enterprise** | Highly regulated, high-security | Maximum | [tier5_enterprise_context_wrapper.md](../core/context_wrappers/tier5_enterprise_context_wrapper.md) |

## Key Dimensions by Tier

The framework scales requirements across multiple engineering dimensions:

| Dimension | Tier 0 | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 |
|-----------|--------|--------|--------|--------|--------|--------|
| **Testing** | None | Basic unit tests (20%) | Unit tests (50%) | Unit + Integration (70%) | Comprehensive (85%+) | Exhaustive (95%+) |
| **Security** | None | Basic practices | OWASP Top 10 | Automated scanning | Pentesting | Advanced threat modeling |
| **CI/CD** | None | Optional | Basic | Required | Staging pipeline | Multiple environments |
| **Documentation** | Notes | Basic README | User docs | Architecture docs | Full system docs | Compliance docs |
| **Observability** | Print statements | Basic logging | Structured logging | Metrics | APM | Distributed tracing |
| **Data Management** | In-memory | SQLite | Single database | Data validation | Backup/DR | Full data governance |

## Selecting the Right Tier

Consider these factors when choosing a delivery tier:

1. **User Impact** - Who will use the system and what's at stake?
2. **Data Sensitivity** - What type of data will be processed?
3. **Scale Requirements** - How many users/transactions are expected?
4. **Regulatory Context** - What compliance standards apply?
5. **Business Criticality** - How important is the system to operations?

Projects can and should upgrade tiers as they mature. Many successful products begin at Tier 1-2 and progressively adopt more rigorous practices as they scale. 