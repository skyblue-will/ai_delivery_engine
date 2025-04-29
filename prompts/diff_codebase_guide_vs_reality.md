# Codebase Guide vs Reality Diff

## Purpose

This prompt helps identify discrepancies between the **Codebase Guide** (documented reality) and the **actual codebase** (present reality). It enforces the principle that documentation must always reflect the true system state.

## INSTRUCTIONS

Analyze both the Codebase Guide (`core/codebase_guide.md`) and the actual codebase to identify any misalignments, missing information, or outdated documentation.

### Assessment Areas

1. **Structure Comparison**
   - Compare directory structure documented vs. actual
   - Validate file organization descriptions

2. **Component Validation**
   - Verify all documented components actually exist
   - Check for components in code not listed in guide

3. **Data Flow Accuracy**
   - Validate documented data flows match implementation
   - Look for undocumented interactions

4. **Entry Point Verification**
   - Confirm all documented entry points exist and work as described
   - Identify undocumented entry points

5. **Technical Debt Honesty**
   - Verify known issues are accurately documented
   - Identify undocumented quirks/debt

## Expected Output

Provide a structured diff with:

1. **Inventory Analysis**
   - Components documented but not present in code
   - Components present in code but not documented
   - Components with inaccurate documentation

2. **Documentation Quality**
   - Areas where documentation is outdated
   - Areas where documentation is too vague
   - Areas of complete alignment (documented accurately)

3. **Codebase Guide Update Plan**
   - Specific sections needing revision
   - New sections needed
   - Sections to remove

4. **Reality Assessment**
   - Binary determination: Does documentation reflect reality? (YES/NO)
   - Percentage of codebase accurately documented

## Example Usage

```
/diff_codebase_guide_vs_reality
```

The goal is to maintain the Codebase Guide as a **precise mirror** of the system's true state. Documentation that diverges from reality is actively harmful and violates the framework's core principle that governance documents must reflect the actual system. 