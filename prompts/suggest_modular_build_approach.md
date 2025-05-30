# Modular Build Approach Suggestion

## Purpose

This prompt helps you leverage an LLM to suggest an optimal modular build approach for your project based on finalized governance artifacts. It's designed to be used at the end of the Planning Phase, after your Scope Document, Codebase Guide, and Context Wrapper are established.

## When to Use

Use this prompt after:
1. Your Delivery Tier has been selected
2. The Scope Document (`v0.x.0.md`) has been approved
3. The Codebase Guide accurately reflects current state
4. The Context Wrapper for your tier has been loaded

## Benefits

- Prevents LLM cognitive overload during implementation
- Ensures architectural decisions align with governance standards
- Creates a coherent build plan that respects scope boundaries
- Reduces development rework through upfront module planning

## Instructions

1. Copy the content between the lines below
2. Replace the `{placeholders}` with your project specifics
3. Submit to your LLM in your preferred AI coding environment
4. Ensure your governance documents are accessible as context to the LLM

---

**System Instructions: You are an architectural planning assistant tasked with suggesting the optimal modular approach for implementing a software project. You will analyze governance documents and propose a clear, organized build strategy.**

I need you to suggest an optimal modular build approach for my project. The following governance artifacts are available in the context:

- Scope Document: {path_to_scope_document} (version {version})
- Codebase Guide: {path_to_codebase_guide}
- Context Wrapper: {path_to_context_wrapper} (Tier {tier_number})

Please use these documents as context rather than requiring me to copy their full content.

Based on these governance artifacts, please provide:

1. A **Modular Architecture Map** breaking down the implementation into logical modules with clear boundaries and interfaces
2. A suggested **Build Sequence** showing dependencies and recommended implementation order
3. **Module Responsibility Matrix** defining what each module is responsible for, highlighting potential reusable components
4. **Key Integration Points** where modules will need to interact
5. **Technical Debt Considerations** to avoid during the build phase, based on our selected delivery tier

Please optimize your suggestions for:
- Alignment with the scope boundaries
- Adherence to the context wrapper standards
- Realistic implementation given the current codebase state
- Maintainability and future extensibility
- {any_additional_optimization_criteria}

Your response should be concrete, practical, and directly actionable by developers who will implement the system.

---

## Notes

- This prompt works best with AI systems that can access multiple documents as context
- The LLM may suggest additional clarification questions if the governance artifacts contain ambiguities
- This prompt is most effective when the Scope Document contains clear functional requirements
- For complex systems, consider segmenting this prompt into domain-specific modular planning sessions 
- After each section of the suggested Build Sequence is generated, use the Codebase Guide Update Template prompt (`prompts/update_codebase_guide.md`) to refresh the Codebase Guide accordingly. 