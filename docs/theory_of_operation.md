# Theory of Operation

## Genesis & Philosophy

The AI Delivery Engine emerged in response to a critical challenge: harnessing the extraordinary speed of AI-assisted development while maintaining engineering discipline, governance, and compliance.

Many AI-generated codebases suffer from common issues:
- Lack of clear structure and documentation
- Insufficient testing and verification
- Inconsistent compliance with requirements
- Difficulty scaling beyond initial implementation

Rather than constraining AI's generative power, the Engine provides a structured engine that guides AI generation toward maintainable, professional, and compliant results.

## Core Mechanisms: The Engine Model

The Engine operates through two integrated cores with continuous interaction:

### Governance Core (Define)

1. **Codebase Guide** — Maps the **present reality** of the system, providing an accurate reference to the current state that all team members and AI tools can comprehend.

2. **Scope Documents** — Define the **destination** for each version, with clear acceptance criteria and traceability to business requirements.

3. **Context Wrappers** — Specify **enforced standards** based on the project's Delivery Tier, ensuring discipline matches the project's maturity.

### Assurance Core (Verify)

1. **Human Verification** — Expert review confirms that implementation matches scope intent.

2. **LLM Analysis** — Structured diff between documentation, code, and standards.

3. **Automated Testing** — Technical validation of functional correctness and compliance.

The continuous interaction between these cores creates a self-reinforcing system that drives development forward while maintaining alignment.

### Practical Driving Analogy

To illustrate how the Engine works in day-to-day delivery:

| Engine Component | Driving Analogy | Responsibility |
|-------------------|-----------------|----------------|
| **Scope Documents** | The **GPS & route** — clearly defining destination and path | Sets direction and measures progress |
| **Codebase Guide** | The **real-time dashboard** — showing current system state | Provides visibility of present reality |
| **Context Wrappers** | The **vehicle safety systems** — enforcing guardrails | Maintains standards appropriate to tier |
| **Assurance Checks** | The **"Are we there yet?"** verification | Drives progress through feedback |
| **AI + Human Implementation** | The **driver + vehicle** partnership | Makes tactical decisions within governed boundaries |

This analogy underscores that the Engine is not bureaucratic overhead — it's an integrated control system guiding every step toward defined outcomes.

## Progressive Rigor Model

A key innovation is the progressive rigor model that scales engineering standards with project maturity:

- Tier 1: Hobby/prototype projects need minimal structure
- Tier 3: Growth/team projects require solid quality gates
- Tier 5: Enterprise/regulated systems demand comprehensive governance

This prevents over-engineering early-stage work while ensuring mature systems meet necessary standards. Critically, at every tier, compliance is binary (pass/fail) — only the standards themselves scale, not the strictness of their enforcement.

## Implementation Strategy

While designed to be tool and model agnostic, the Engine is optimised for integration with AI-powered code editors like **Cursor** and **Winsurf**, which provide ideal environments to apply governance in real-time as code is generated.

The Engine works with:
- Any AI coding model or assistant
- Any development toolchain
- Any programming language
- Any cloud or on-premises infrastructure

This flexibility enables incremental adoption, applying first to critical governance areas and expanding as projects mature.

## Core Principles

1. **Reflect Reality** — Documentation must mirror the system's true state
2. **Compliance is Binary** — Pass or fail; no "mostly compliant" state
3. **Tiers Control Standards** — The active tier determines *which* standards apply; enforcement is always binary.
4. **Simplicity is Power** — No meta-frameworks or speculation
5. **Docker-First Discipline** — Runs identically everywhere or fails early 