## Key Differences: Cursor vs. GitHub Copilot

This document highlights critical differences between AI coding assistants that impact their compatibility with the AI Delivery Engine's Governance ↔ Assurance workflow.

### Core Differences

1. **Persistent Rules Mechanism**
   - **Cursor**: Provides `cursorrules` feature that allows injecting persistent context/directives with every interaction
   - **Copilot**: No equivalent feature; requires creating files in the repository that must be explicitly referenced

2. **Context Awareness**
   - **Cursor**: Can automatically access multiple files across the repository to understand context
   - **Copilot**: More limited context window; generally focused on the current file

3. **Execution Environment**
   - **Cursor**: Offers terminal access directly in the chat interface
   - **Copilot**: Limited execution capabilities within the conversation

4. **Customization**
   - **Cursor**: Can self-host models and customize behavior extensively
   - **Copilot**: Cloud-only service with more fixed behavior patterns

### Impact on Delivery Engine Implementation

The lack of a persistent rules mechanism in Copilot makes implementing the Governance Core more challenging, as standards must be manually referenced or included in each prompt rather than automatically enforced across all interactions.

For organizations implementing the AI Delivery Engine framework, Cursor currently provides more direct support for the tightly-coupled Governance ↔ Assurance workflow due to its ability to enforce persistent rules and standards. 