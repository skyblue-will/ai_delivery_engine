## Key Differences: Cursor vs. GitHub Copilot

This document highlights verified differences between AI coding assistants that impact their compatibility with the AI Delivery Engine's Governance ↔ Assurance workflow.

### Core Verified Differences

1. **Persistent Rules Mechanism**
   - **Cursor**: Provides `cursorrules` feature that allows injecting persistent context/directives with every interaction
   - **Copilot**: No equivalent feature; requires creating files in the repository that must be explicitly referenced

2. **Model Configuration**
   - **Copilot**: Advanced models must be enabled for more complex reasoning capabilities
   - **Cursor**: Advanced reasoning capabilities are available by default

### Impact on Delivery Engine Implementation

The lack of a persistent rules mechanism in Copilot makes implementing the Governance Core more challenging, as standards must be manually referenced or included in each prompt rather than automatically enforced across all interactions.

For organizations implementing the AI Delivery Engine framework, these differences significantly affect how the Governance Core can be implemented and maintained across development workflows. 