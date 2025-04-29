# When you can change your scope mid-workflow (and when you can't)

## Purpose
This document explains when it is safe to adjust the project scope during an active build cycle and when such changes should be avoided. It helps maintain stability and traceability in the AI Delivery Engine workflow.

## When you can change your scope
• During the Modular Build phase, if missing requirements or critical clarity gaps block implementation.  
• When stakeholder-approved changes affect acceptance criteria or in-scope user stories.  
• After running an explicit scope review: update the Scope Document (`docs/scopes/vX.Y.Z.md`) and communicate the change to all contributors.  

## When you can't change your scope
• In the middle of development without stakeholder review or documented approval.  
• During or after the Governance Check phase, unless a critical compliance or security issue forces a re-scope.  
• Without updating the Scope Document or re-running Assurance Core checks.  

## How to change scope safely
1. Stop development and open a scope-change PR that clearly describes the proposed adjustment.  
2. Obtain stakeholder approval and update the Scope Document (`docs/scopes/vX.Y.Z.md`).  
3. Refresh the Codebase Guide with the Update Template prompt (`prompts/update_codebase_guide.md`).  
4. Run Assurance Core checks (human review, LLM diff, automated tests) to confirm binary compliance.  
5. Communicate the updated plan and acceptance criteria to the team.  

## Related resources
- **Scope Document Template**: `core/scope_doc_template.md`  
- **Codebase Guide Update Template**: `prompts/update_codebase_guide.md`  
- **Upcoming**: Scope management guidelines (coming soon) 