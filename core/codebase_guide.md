# Codebase Guide

*Generated: 2023-09-22*

This guide provides an authoritative description of the current codebase state. All contributors should update this document after significant changes.

## Core Repository Structure

| Category | Location | Purpose |
|----------|----------|---------|
| **Governance Core** | `codebase_guide.md` | Current system state reference |
| | `meta/scope_doc_template.md` | Versioned plans for future changes |
| | `meta/context_wrappers/*` | Delivery tier-specific disciplinary controls |
| **Documentation** | `docs/introduction.md` | Framework onboarding |
| | `docs/theory_of_operation.md` | Conceptual foundation |
| | `docs/delivery_tiers.md` | Progressive rigor model details |
| **Tools & Examples** | `tools/` | Reference material on AI tooling landscape |
| | `examples/` | Sample implementations |
| **Operational** | `.github/workflows/` | CI/CD configurations |

## Key Components

| Component | Purpose | Update Frequency |
|-----------|---------|------------------|
| **Context Wrappers** | Structure AI development by delivery tier | When new practices emerge |
| **Scope Template** | Guide versioned evolution plans | When planning process evolves |
| **Documentation** | Explain framework mechanisms | When significant features change |

## Development Flow

```
Contributor → Selects Delivery Tier → Creates Scope Doc → Uses Context Wrapper with AI →
            → Implements Code → Updates Codebase Guide → Repeats
```

## Update Process

This guide should be regenerated whenever:

1. **Structure Changes** - New directories or significant organization changes
2. **Component Updates** - New context wrappers, templates, or tools added
3. **Workflow Evolution** - Process changes that affect how the framework is used

Updates should be performed as the final step in a contribution lifecycle, ensuring this guide remains the authoritative "as-is" reference.

## Areas for Improvement

1. **Automation** - Diagram generation is currently manual; CI/CD integration planned
2. **Testing** - Future integration tests for context wrappers would be valuable
3. **Documentation** - Expanded examples of the framework in real-world use