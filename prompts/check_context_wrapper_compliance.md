# Context Wrapper Compliance Checker

## Purpose

This prompt helps verify whether code adheres to the standards defined in the Context Wrapper for the project's Delivery Tier. It enforces the principle that **compliance is binary** - code either meets all required standards or fails compliance.

## INSTRUCTIONS

I need you to conduct a thorough compliance check of the codebase against our active Context Wrapper standards. Look for violations, omissions, or areas where implementation deviates from requirements.

### Files to Compare

1. **Context Wrapper**: `core/context_wrappers/tier{TIER_NUMBER}_*.md`
2. **Codebase Files**:
   - Implementation files relevant to the assessment (provide as context)

## Compliance Engine

For each standard category in the Context Wrapper:

| Standard Category | Assessment Approach |
|-------------------|---------------------|
| **Execution Environment** | Check for Docker/venv configuration per tier requirements |
| **Supply Chain Integrity** | Verify dependency versioning and vulnerability scanning |
| **CI/CD Pipeline** | Confirm workflows exist and include required checks |
| **Project Layout** | Validate directory structure meets tier standards |
| **Database Discipline** | Check DB usage, migrations, security per tier |
| **Testing & Quality** | Verify test coverage and quality gates |
| **Security & Scanning** | Confirm security practices are implemented |
| **Observability** | Check logging/monitoring implementation |
| **Documentation** | Verify docs match tier requirements |
| **Branch/Commit Hygiene** | Assess commit messages and branching |
| **LLM Guard-Rails** | Confirm AI safety measures |

## Expected Output

Provide a structured assessment with:

1. **Standards Summary**
   - List all standards from the Context Wrapper
   - Mapping of where each is implemented (or not)

2. **Compliance Details**
   - For each standard: PASS, FAIL, or PARTIAL
   - Evidence and file references for each assessment
   - Specific violations where standards aren't met

3. **Remediation Plan**
   - Prioritized actions to resolve compliance issues
   - Estimated effort per item (Low/Medium/High)

4. **Binary Assessment**
   - Overall PASS/FAIL determination
   - "FAIL" if ANY standard is not fully implemented

## Example Usage

```
/check_context_wrapper_compliance 3
```

This verification enforces the principle that compliance is binary - either ALL standards are met (PASS) or the project is non-compliant (FAIL). There is no "mostly compliant" state accepted in the AI Delivery Engine. 