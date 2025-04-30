# Example AI Coding Policy

**Status:** Template

This document provides an example policy framework for organisations implementing AI-assisted software development while maintaining compliance with ISO27001 and Cyber Essentials security standards. It demonstrates how the AI Delivery Engine can be used as the technical enforcement layer for organisational security and compliance requirements.

## Policy Overview

| Component | Description |
|-----------|-------------|
| **Purpose** | Define secure, compliant practices for AI-assisted development |
| **Scope** | All AI-assisted software engineering activities |
| **Compliance** | ISO27001 (Information Security) and Cyber Essentials |
| **Implementation** | AI Delivery Engine (AIDE) with appropriate Delivery Tier |

## 1. Information Security Requirements (ISO27001)

| Requirement | Policy Statement | Implementation via AIDE |
|-------------|------------------|-------------------------|
| **A.14.2.1 Secure Development** | All AI-assisted development must occur within controlled environments with appropriate access controls and monitoring. | AIDE enforces Docker-first development with controlled contexts and workspace boundaries. |
| **A.14.2.5 Secure System Engineering** | AI coding assistants must operate within defined guardrails that enforce security principles. | AIDE Governance Core defines standards based on Delivery Tier; Assurance Core verifies compliance. |
| **A.14.2.6 Secure Development Environment** | Development environments must include segregation of duties and access controls. | AIDE workflow includes separation between Scope, Build, and Governance Check phases. |
| **A.14.2.8 System Security Testing** | All code, regardless of origin (human or AI-generated), must undergo security testing. | AIDE Assurance Core implements binary verification of all security requirements. |
| **A.12.4.1 Logging & Monitoring** | AI interactions that produce code must be logged and attributable. | AIDE implements watermarking and provenance tracking for all AI-generated artefacts. |
| **A.18.1.3 Protection of Records** | Evidence of compliance must be maintained. | AIDE maintains immutable scope documents, governance artefacts, and verification records. |

## 2. Cyber Essentials Requirements

| Requirement | Policy Statement | Implementation via AIDE |
|-------------|------------------|-------------------------|
| **Secure Configuration** | AI tools must use secure configurations prohibiting vulnerable patterns. | AIDE Governance Core defines secure coding standards, while Context Wrappers provide implementation guidance. |
| **Boundary Firewalls** | AI assistants must not exfiltrate sensitive data. | AIDE enforces privacy-first approach with telemetry-off by default and boundaries around data access. |
| **Access Control** | AI tool access must be limited to authorised personnel. | AIDE workflow integrates with existing authentication and authorisation systems. |
| **Malware Protection** | AI-generated code must be scanned for security vulnerabilities. | AIDE Assurance Core includes automated scanning in the verification process. |
| **Patch Management** | Dependencies used must be current and vulnerability-free. | AIDE enforces SBOM creation and dependency validation in higher Delivery Tiers. |

## 3. Implementation Using AI Delivery Engine

### Required Delivery Tier Selection

| Risk Level | Example System | Required AIDE Tier |
|------------|----------------|-------------------|
| Low | Internal tools, non-sensitive data | Tier 2-3 |
| Medium | Customer-facing, non-regulated | Tier 3-4 |
| High | Regulated, sensitive data | Tier 5 |

### Implementation Steps

1. Deploy the AI Delivery Engine as your development framework
2. Select appropriate Delivery Tier based on system risk level
3. Customise Context Wrappers to include specific organisational security requirements
4. Enable appropriate Assurance Core checks (both automated and manual)
5. Document compliance mapping in the Scope Document for each release
6. Maintain Codebase Guide with security-relevant architecture information
7. Ensure verification records are retained for compliance evidence

### Required Developer Practices

1. Follow the Engine Workflow (Scope → Setup → Build → Governance Check → Ship → Repeat)
2. Update the Codebase Guide after security-relevant changes
3. Document security controls in Scope Documents
4. Use AI assistants only within the Context Wrapper boundaries
5. Submit all code to Assurance Core verification before release
6. Report any AI-generated security concerns through standard incident procedures

## 4. Governance & Assurance

| Component | Security Relevance | Compliance Evidence |
|-----------|-------------------|---------------------|
| **Codebase Guide** | Documents security controls and architecture | Design documentation (ISO27001 A.14.2.5) |
| **Scope Document** | Captures security requirements for each release | Change management evidence (ISO27001 A.14.2.2) |
| **Context Wrapper** | Defines security standards during development | Secure coding evidence (Cyber Essentials) |
| **Assurance Checks** | Verifies compliance with security requirements | Testing evidence (ISO27001 A.14.2.8) |

## 5. Review and Maintenance

This policy must be:
- Reviewed annually or after significant changes to AI capabilities
- Updated when ISO27001 or Cyber Essentials standards are revised
- Tested through internal audit of the AIDE implementation

## 6. Approval

| Role | Name | Date |
|------|------|------|
| CISO | [Name] | [Date] |
| CTO | [Name] | [Date] |
| DPO | [Name] | [Date] |

---

*This template demonstrates how the AI Delivery Engine provides the technical foundation for regulated AI-assisted development. Organisations should customise this policy to match their specific security requirements and governance structure.* 