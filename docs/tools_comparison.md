## Key Differences: Cursor vs. GitHub Copilot

This document highlights verified differences between AI coding assistants that impact their compatibility with the AI Delivery Engine's Governance ↔ Assurance workflow.

### Core Verified Differences

1. **Persistent Rules Mechanism**
   - **Cursor**: Provides `cursorrules` feature that allows injecting persistent context/directives with every interaction
   - **Copilot**: Offers "Use Instruction Files" setting that enables stronger compliance with rules, allowing for persistent guidance across interactions

2. **Model Configuration**
   - **Copilot**: Advanced models must be enabled for more complex reasoning capabilities
   - **Cursor**: Advanced reasoning capabilities are available by default

### Impact on Delivery Engine Implementation

With Copilot's "Use Instruction Files" setting enabled, the Governance Core can be more effectively implemented, as standards can be persistently applied across interactions, similar to Cursor's approach.

For organisations implementing the AI Delivery Engine framework, understanding these features helps determine how the Governance Core can be implemented and maintained across development workflows. 