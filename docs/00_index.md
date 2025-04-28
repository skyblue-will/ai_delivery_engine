# AI Delivery Framework Documentation

Welcome to the AI Delivery Framework documentation. This framework provides a structured, governance-first approach to building software with AI assistance.

## What the Framework Solves

Modern AI development tools enable rapid software creation, but often lead to unstructured, unmaintainable codebases lacking proper engineering discipline. The AI Delivery Framework solves this by:

1. **Providing Structure** - Enforces organization and best practices even during rapid development
2. **Ensuring Compliance** - Scales regulatory requirements based on project maturity
3. **Maintaining Auditability** - Creates clear documentation trail for all development choices
4. **Enabling Speed with Control** - Allows teams to move quickly without sacrificing governance

## Governance Core Overview

The framework is built around three critical governance components:

| Component | Purpose | How to Use |
|-----------|---------|------------|
| **Codebase Guide** | Documents the current "as-is" state of the system | Regenerate when significant changes occur |
| **Versioned Scope Documents** | Defines the "to-be" state for each iteration | Create before starting new development |
| **Context Wrappers** | Enforces delivery discipline by tier | Include in AI prompting sessions |

## Documentation Sections

### Guides
- [Introduction](introduction.md) - Getting started with the framework
- [Theory of Operation](theory_of_operation.md) - Philosophy and core concepts
- [Delivery Tiers](delivery_tiers.md) - Understanding the progressive rigor model

### Workflows
- [Shipping Plan](shipping_plan.md) - Step-by-step delivery workflow

### Context Wrappers
- [Tier 0: Exploration](../meta/context_wrappers/tier0_exploration_context_wrapper.md)
- [Tier 1: Hobby](../meta/context_wrappers/tier1_hobby_context_wrapper.md)
- [Tier 2: MVP](../meta/context_wrappers/tier2_mvp_context_wrapper.md)
- [Tier 3: Beta](../meta/context_wrappers/tier3_beta_context_wrapper.md)
- [Tier 4: Production](../meta/context_wrappers/tier4_production_context_wrapper.md)
- [Tier 5: Enterprise](../meta/context_wrappers/tier5_enterprise_context_wrapper.md)

### Compliance Modules
- GDPR Lite (Tier 2+)
- GDPR Full (Tier 4+)
- HIPAA (Tier 4+)
- SOC2 (Tier 4+)
- PCI-DSS (Tier 4+)

### Reference
- [Appendices](appendices/)
  - [FAQ](appendices/faq.md)
  - [Lessons Learned](appendices/lessons_learned.md) 