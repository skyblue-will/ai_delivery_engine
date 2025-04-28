# **AI Delivery Framework**

_A professional method for AI-assisted software delivery._

---

## 1. Purpose

The **AI Delivery Framework** enables teams to deliver real-world software with the speed of AI tooling **without compromising engineering discipline, compliance, or scalability**.

The framework is governed by three living assets:

1. **Codebase Guide** – authoritative description of the _current_ codebase.
2. **Versioned Scope Documents** – describe the _target_ state for each iteration (e.g. `v0.x.0.md`).
3. **Context Wrappers** – enforce delivery discipline according to **Delivery Tiers**.

Together these assets form the governance core that keeps fast-moving AI work predictable and auditable.

---

## 2. Core Governance Components

| Component | Purpose | Location |
|-----------|---------|----------|
| **Codebase Guide** | Live reference for the "as-is" system. | `meta/codebase_guide_template.md` |
| **Scope Document** | Defines the "to-be" functionality for each version. | `meta/scope_doc_template.md` |
| **Context Wrapper** | Applies delivery rules based on Delivery Tier. | Applied via prompting layer |

---

## 3. Operating Principles

1. **Scope Before Code** – every change begins with a versioned scope document.
2. **Modular & Testable** – AI-generated code must be small, composable, and covered by tests.
3. **Environment Discipline** – Docker-based dev environments and CI/CD from day one.
4. **Adaptive Rigor** – delivery standards scale through **Delivery Tiers**.
5. **Tool & Model Agnostic** – compatible with any AI model or tech stack.
6. **Compliance When Required** – bolt-on modules (GDPR, HIPAA, etc.) only when the project stage demands.

---

## 4. Delivery Workflow (High Level)

1. **Project Initialisation** – assess risk and set Delivery Tier.
2. **Scoping** – write or update the versioned scope document.
3. **Model & Tool Selection** – choose LLMs and dev tools that fit the tier.
4. **Prompt Structuring** – decompose work into modular, testable prompts.
5. **Implementation & Testing** – code + tests generated via AI within the governed context.
6. **Review & Merge** – human review reinforced by automated checks.
7. **Continuous Delivery** – CI/CD pipeline ships artefacts appropriate to the tier.
8. **Governance Update** – update Codebase Guide and plan next scope.

---

## 5. Delivery Tiers

| Tier | Use Case | Engineering Rigor |
|------|----------|-------------------|
| **1 – Prototype** | Exploratory spikes, internal proofs | Minimal |
| **2 – MVP** | Early user validation | Moderate (GDPR Lite if personal data) |
| **3 – Beta** | Public pilots, early scaling | High |
| **4 – Production** | Launched products | Full |
| **5 – Enterprise** | Highly regulated, high-security | Maximum |

Delivery standards (testing depth, code review, compliance gates) **increase progressively** with each tier.

---

## 6. Compliance Integration

The framework keeps compliance _modular_:

- **GDPR Lite** is required from **Tier 2** if personal data is processed.
- Additional modules (GDPR Full, HIPAA, SOC2, PCI-DSS) are integrated _only_ when legally or contractually required.
- Internal security guidelines inherit from company policy at Tier 3 and above.

This staged model protects early-stage agility while guaranteeing auditability for production systems.

---

## 7. Repository Map

```text
/framework-delivery/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── meta/
│   ├── delivery_tiers.md
│   ├── full_workflow.md
│   ├── model_strategy.md
│   ├── codebase_guide_template.md
│   └── scope_doc_template.md
├── tools/
│   ├── current_tooling_landscape.md
│   └── recommended_tool_criteria.md
├── examples/
│   └── flowerpot_booking_form/
├── docs/
│   ├── introduction.md
│   ├── why_framework.md
│   ├── faq.md
│   ├── shipping_plan.md
│   └── lessons_learned.md
├── branding/
│   ├── logo.png
│   └── brand_sheet.pdf
└── roadmap.md
```

---

## 8. Getting Started

1. **Clone / Fork** the repository.
2. **Select a Delivery Tier** based on project risk.
3. **Draft a Scope Document** for your first version.
4. **Generate Code** using the Context Wrapper for your tier.
5. **Commit, Test, and Ship** via the prescribed workflow.

_For detailed guidance see `docs/introduction.md`._

---

## 9. Roadmap (Snapshot)

- **Fine-Tuned Agents** – automate scoping and tier assignment.
- **Interactive Scoping Tools** – Q&A workflow.
- **Expanded Compliance Modules** – GDPR, HIPAA, PCI-DSS, SOC2 templates.
- **Enhanced Delivery Tiers** – deeper maturity models for enterprise scale.

Roadmap items are tracked in [`roadmap.md`](roadmap.md) and governed by scope documents per release.

---

## 10. License

MIT License. See [`LICENSE`](LICENSE) for full terms.