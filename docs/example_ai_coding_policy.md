# Example AI Coding Policy

**Status**: Template

This document provides an example policy framework for organisations implementing AI-assisted software development while maintaining compliance with ISO27001 and Cyber Essentials security standards. It demonstrates how the AI Product Delivery Engine can be used as the technical enforcement layer for organisational security and compliance requirements.

## Policy Overview

| Component | Description |
|-----------|-------------|
| Purpose | Define secure, compliant practices for AI-assisted development |
| Scope | All AI-assisted software engineering activities |
| Compliance | ISO27001 (Information Security) and Cyber Essentials |
| Implementation | AI Product Delivery Engine (AIPDE) with appropriate Delivery Tier |
| Philosophy | Product-first, "Think before you code" approach to development |

## 1. Information Security Requirements (ISO27001)

| Requirement | Policy Statement | Implementation via AIPDE |
|-------------|-----------------|-------------------------|
| A.14.2.1 Secure Development | All AI-assisted development must occur within controlled environments with appropriate access controls and monitoring. | AIPDE enforces Docker-first development with controlled contexts and workspace boundaries. |
| A.14.2.5 Secure System Engineering | AI coding assistants must operate within defined guardrails that enforce security principles. | AIPDE Governance Core defines standards based on Delivery Tier; Assurance Core verifies compliance. |
| A.14.2.6 Secure Development Environment | Development environments must include segregation of duties and access controls. | AIPDE workflow includes separation between Scope, Build, and Governance Check phases. |
| A.14.2.8 System Security Testing | All code, regardless of origin (human or AI-generated), must undergo security testing. | AIPDE Assurance Core implements binary verification of all security requirements. |
| A.12.4.1 Logging & Monitoring | AI interactions that produce code must be logged and attributable. | AIPDE implements watermarking and provenance tracking for all AI-generated artefacts. |
| A.18.1.3 Protection of Records | Evidence of compliance must be maintained. | AIPDE maintains immutable scope documents, governance artefacts, and verification records. |

## 2. Cyber Essentials Requirements

| Requirement | Policy Statement | Implementation via AIPDE |
|-------------|-----------------|-------------------------|
| Secure Configuration | AI tools must use secure configurations prohibiting vulnerable patterns. | AIPDE Governance Core defines secure coding standards, while Context Wrappers provide implementation guidance. |
| Boundary Firewalls | AI assistants must not exfiltrate sensitive data. | AIPDE enforces privacy-first approach with telemetry-off by default and boundaries around data access. |
| Access Control | AI tool access must be limited to authorised personnel. | AIPDE workflow integrates with existing authentication and authorisation systems. |
| Malware Protection | AI-generated code must be scanned for security vulnerabilities. | AIPDE Assurance Core includes automated scanning in the verification process. |
| Patch Management | Dependencies used must be current and vulnerability-free. | AIPDE enforces SBOM creation and dependency validation in higher Delivery Tiers. |

## 3. Implementation Using AI Product Delivery Engine

### Core Philosophy: Think Before You Code

Before initiating any development work, teams must evaluate whether the proposed code is truly necessary by asking:

1. Does this code directly address a verified user/customer need?
2. Is there an existing solution that could be reused or modified instead?
3. Will this code deliver measurable value to the product?
4. Does the business value justify the maintenance cost?
5. Is this solution aligned with our product strategy?

Only after answering these questions should the team proceed to implementation.

### Required Delivery Tier Selection

| Risk Level | Example System | Required AIPDE Tier |
|------------|---------------|----------------------|
| Low | Internal tools, non-sensitive data | Tier 2-3 |
| Medium | Customer-facing, non-regulated | Tier 3-4 |
| High | Regulated, sensitive data | Tier 5 |

### Implementation Steps

1. Deploy the AI Product Delivery Engine as your development framework
2. Select appropriate Delivery Tier based on system risk level and product requirements
3. Customize Context Wrappers to include specific organisational security requirements
4. Enable appropriate Assurance Core checks (both automated and manual)
5. Document compliance mapping in the Scope Document for each release
6. Maintain Codebase Guide with security-relevant architecture information and product documentation
7. Ensure verification records are retained for compliance evidence

### Required Developer Practices

1. Apply "Think before you code" evaluation to every feature and component
2. Follow the Engine Workflow (Scope → Setup → Build → Governance Check → Ship → Repeat)
3. Treat documentation as a first-class deliverable alongside code
4. Maintain a product-first mindset in all development activities
5. Update the Codebase Guide after security-relevant changes
6. Document security controls in Scope Documents
7. Use AI assistants only within the Context Wrapper boundaries
8. Submit all code to Assurance Core verification before release
9. Report any AI-generated security concerns through standard incident procedures
10. Regularly evaluate existing code for continued relevance and value

## 4. Governance & Assurance

| Component | Security Relevance | Compliance Evidence |
|-----------|-------------------|----------------------|
| Codebase Guide | Documents security controls and architecture | Design documentation (ISO27001 A.14.2.5) |
| Scope Document | Captures security requirements for each release | Change management evidence (ISO27001 A.14.2.2) |
| Context Wrapper | Defines security standards during development | Secure coding evidence (Cyber Essentials) |
| Assurance Checks | Verifies compliance with security requirements | Testing evidence (ISO27001 A.14.2.8) |

## 5. Review and Maintenance

This policy must be:

* Reviewed annually or after significant changes to AI capabilities
* Updated when ISO27001 or Cyber Essentials standards are revised
* Tested through internal audit of the AIPDE implementation

## 6. Approval

| Role | Name | Date |
|------|------|------|
| CISO | [Name] | [Date] |
| CTO | [Name] | [Date] |
| DPO | [Name] | [Date] |

---

This template demonstrates how the AI Product Delivery Engine provides the technical foundation for regulated AI-assisted development. Organisations should customise this policy to match their specific security requirements, product goals, and governance structure. 