---
version: "0.0.0"
apply_to_component: "component_name"
delivery_tier: 0
prepared_by: "Author (Recommended model: GPT-4o)"
date: "YYYY-MM-DD"
---

# Project Name

## Version X.Y.Z — *[Phase] Scope* (Stakeholder-approved)

> **Purpose:**  [One-sentence description of what this version will achieve for users/stakeholders]

---

## 1. Business Goals
| # | Goal | Measure of Success |
|---|------|-------------------|
| G1 | [Specific goal] | [Quantifiable metric with baseline → target] |
| G2 | [Specific goal] | [Quantifiable metric with baseline → target] |
| G3 | [Specific goal] | [Quantifiable metric with baseline → target] |

---

## 2. Scope Boundaries

### 2.1. In-Scope
1. **[Feature Area 1]** - [Brief description]
   • [Sub-feature detail]
   • [Sub-feature detail]
2. **[Feature Area 2]** - [Brief description]
3. **[Feature Area 3]** - [Brief description]
4. **[Implementation Constraints]** - [Brief description, reference to Context Wrapper/Delivery Tier]

### 2.2. Out-of-Scope (this version)
* [Feature that will be addressed in future versions]
* [Feature that will be addressed in future versions]
* [Feature that will be addressed in future versions]

---

## 3. User Stories
| ID | As a … | I want … | So that … | Acceptance Criteria |
|----|--------|---------|-----------|--------------------|
| US-01 | [Role] | [Action] | [Benefit] | [List of verification points] |
| US-02 | [Role] | [Action] | [Benefit] | [List of verification points] |
| US-03 | [Role] | [Action] | [Benefit] | [List of verification points] |
| US-04 | System | [Action] | [Benefit] | [List of verification points] |

---

## 4. Data Model
| Entity | Attributes | Relationships | Notes |
|--------|------------|--------------|-------|
| [Entity 1] | [Key attributes] | [Relations to other entities] | [Special considerations] |
| [Entity 2] | [Key attributes] | [Relations to other entities] | [Special considerations] |

---

## 5. External Interfaces
| Interface | Type | Purpose | Data Exchange Format |
|-----------|------|---------|---------------------|
| [Interface 1] | [REST API, File Import, etc.] | [Brief description] | [JSON, CSV, etc.] |
| [Interface 2] | [REST API, File Import, etc.] | [Brief description] | [JSON, CSV, etc.] |

---

## 6. Architecture & Tech Stack
| Layer | Tech | Rationale |
|-------|------|-----------|
| Front-end | [Technology] | [Why selected] |
| API | [Technology] | [Why selected] |
| Database | [Technology] | [Why selected] |
| Processing | [Technology] | [Why selected] |
| Authentication | [Technology] | [Why selected] |
| Containerisation | [Technology] | [Why selected] |
| CI/CD | [Technology] | [Why selected] |
| Observability | [Technology] | [Why selected] |
| Hosting | [Technology] | [Why selected] |

---

## 7. API Contracts
### 7.1. [Endpoint Name]
```jsonc
// Request
{
  "property1": "value",
  "property2": "value"
}

// Response
{
  "property1": "value",
  "property2": "value"
}
```

### 7.2. Error Codes
| Code | Meaning |
|------|---------|
| [Status Code] | [Description] |
| [Status Code] | [Description] |

---

## 8. Non-Functional Requirements
* **Performance** — [Specific requirements with metrics]
* **Reliability** — [Availability/reliability target]
* **Security** — [Security requirements]
* **Compliance** — [Regulatory/legal requirements]
* **Accessibility** — [Accessibility standards]
* **Scalability** — [Scalability requirements]

---

## 9. Open Questions & Assumptions
1. [Question or assumption that needs resolution]
2. [Question or assumption that needs resolution]
3. [Question or assumption that needs resolution]

---

## 10. Traceability Matrix
| Business Goal | User Stories | Components | Risk Level |
|---------------|--------------|------------|------------|
| G1 | US-01, US-02 | [Component] | Low/Medium/High |
| G2 | US-03 | [Component] | Low/Medium/High |
| G3 | US-04 | [Component] | Low/Medium/High |

---

## 11. Acceptance Criteria (Definition of Done)
* All user stories pass their acceptance criteria.
* [End-to-end test scenario passes]
* [Quality gate passes - reference to Context Wrapper rules]
* [Documentation requirement]
* [Performance requirement met]

---

## 12. Codebase Guide Updates

The following sections of the [Codebase Guide](./codebase_guide.md) will need updates after implementing this scope:

* **Project Structure** - [New directories or significant changes]
* **Key Modules & Components** - [New modules or updated functionality]
* **Data Flow** - [Changes to data processing pipelines]
* **Entry Points & Core Logic** - [New or modified entry points]
* **Known Quirks / Tech Debt** - [New or resolved technical debt items]
* **Diagrams** - [Required updates to system diagrams]

Follow the detailed instructions in the [Codebase Guide Update Template](../meta/codebase_guide_update_template.md) to ensure a complete and accurate guide update.

---

*Prepared by: [Author Name/Role] ([AI Assistant Model] if applicable)*  
*Date: [Date of preparation/approval]*  
*Delivery Tier: [Tier level]* 