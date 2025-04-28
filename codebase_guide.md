# Codebase Guide

*Generated: {{DATE}}*

---

## 1. Project Structure

| Directory / File | Purpose |
|------------------|---------|
| `README.md` | High-level overview of the AI Delivery Framework. |
| `meta/` | Governance core templates (`codebase_guide_template.md`, `scope_doc_template.md`) and context wrapper definitions. |
| `docs/` | Framework reference documentation. Holds introduction, FAQ, lessons learned, and architecture diagrams. |
| `tools/` | Reference material on current AI tooling landscape and recommended criteria. |
| `examples/` | Sample projects demonstrating the framework (e.g. `flowerpot_booking_form/`). |
| `branding/` | Logo and brand assets. |
| `docs/architecture/` | C4 diagrams and generation script (`generate_c4_diagrams.py`). |
| `CONTRIBUTING.md` | Contribution guidelines. |
| `CODE_OF_CONDUCT.md` | Community behaviour standards. |
| `roadmap.md` | Planned framework evolution. |

---

## 2. Key Modules & Components

| Path | Component | One-liner Description |
|------|-----------|-----------------------|
| `meta/codebase_guide_template.md` | Template | Skeleton for future codebase guides. |
| `meta/scope_doc_template.md` | Template | Versioned scope document template. |
| `meta/context_wrappers/` | Markdown Wrappers | Delivery-tier specific prompt wrappers that enforce engineering discipline. |
| `meta/governance_core.md` | Governance Doc | Explains the live governance loop: Codebase Guide, Scope Docs, and Context Wrappers. |
| `docs/introduction.md` | Intro Doc | Detailed rationale and onboarding guidance for new engineers. |
| `docs/architecture/generate_c4_diagrams.py` | Utility Script | Generates C4 Context, Container, and Component diagrams using the `diagrams` library. |

---

## 3. Data Flow

```
Contributor ➜ edits markdown / code
          ➜ commits & pushes to GitHub repository
          ➜ CI/CD (external) generates artefacts and triggers docs/architecture script (optional)
          ➜ Updated documentation & diagrams stored in repo
```
*All artefacts are version-controlled; no runtime application code or persistence layer exists in this repository.*

---

## 4. Entry Points & Core Logic

| Entry Point | Location | Function |
|-------------|----------|----------|
| Diagram generation | `docs/architecture/generate_c4_diagrams.py` | Produces `c4_context.png`, `c4_container.png`, `c4_component.png`. Requires local Graphviz (`dot`) on PATH. |
| Context Wrappers | `meta/context_wrappers/*` | Read by external AI tooling to apply Delivery Tier rules. |

There are **no executables, services, or CLIs** beyond these helper scripts.

---

## 5. Known Quirks / Tech Debt

1. **Graphviz Dependency** – The diagram script fails if `dot` is not installed (see current error stack in commit history).
2. **Manual Diagram Refresh** – Diagrams must be regenerated locally and committed; no automation yet.
3. **Documentation-Heavy Repo** – No code compilation or tests exist; future integration tests for context wrappers are desirable but absent.

---

## 6. C4 Diagrams

| Level | Image |
|-------|--------|
| Context | ![Context Diagram](docs/architecture/c4_context.png) |
| Container | ![Container Diagram](docs/architecture/c4_container.png) |
| Component | ![Component Diagram](docs/architecture/c4_component.png) |

*Diagrams generated via `docs/architecture/generate_c4_diagrams.py`.* 