# Scope vs Codebase Comparison Prompt

## Purpose

This prompt helps verify alignment between the **defined destination** (Scope Document) and **present reality** (actual codebase). Use it to identify drift, missing features, or implementation gaps.

## INSTRUCTIONS

I need you to perform a rigorous diff between our intended scope and what exists in the codebase. Look for areas of misalignment, missing features, or implementation gaps. 

### Files to Compare

1. **Scope Document**: `docs/scopes/v{VERSION}.md`
2. **Codebase Files**:
   - `core/codebase_guide.md` (high-level reality overview)
   - Actual implementation files (provide as context)

## Comparison Framework

For each feature or component in the Scope Document:

| Assessment Dimension | Questions to Answer |
|----------------------|---------------------|
| **Existence** | Does the feature exist at all? |
| **Completeness** | Is the implementation complete per acceptance criteria? |
| **Alignment** | Does implementation match the intended design/approach? |
| **Standards Adherence** | Does it follow the Context Wrapper standards for our tier? |

## Expected Output

Provide a structured assessment with:

1. **Alignment Summary**
   - Overall completion percentage
   - Key areas of alignment and deviation

2. **Gap Analysis**
   - Features present in scope but missing in code
   - Features in code but not defined in scope
   - Partially implemented features with specific gaps

3. **Corrective Actions**
   - Prioritized list of actions to bring reality in line with scope
   - Suggested scope document updates if reality has evolved for valid reasons

4. **Binary Assessment**
   - PASS/FAIL determination of whether the current state meets scope requirements

## Example Usage

```
/compare_scope_to_codebase v0.1.0
```

This is a verification tool - outputs should be factual, evidence-based, and free from speculation. The goal is to drive progress through accurate assessment of current state vs defined destination. 