# **AI Model Guide — AI Delivery Framework**

---

## 🎯 Purpose

This guide helps teams make practical decisions about **selecting and using AI models** in projects that follow the AI Delivery Framework. It connects everyday technical choices to the framework's core governance components (Codebase Guide, Scope Documents, and Context Wrappers).

*Who should read this?* Project leads, developers, and architects who need clear guidelines for using AI effectively in their projects.

---

## 1. Model Selection Guidelines

| Question | What to Consider | How It Connects to Framework |
|-----------|-----------------|-------------------|
| **What are you trying to accomplish?** | • What specific output do you need?<br>• How fast must it work? | Document these requirements in your *Scope Document* under **Functional Requirements**. |
| **What data are you working with?** | • Does your task involve sensitive data? | Determines which *Delivery Tier* applies and what compliance rules to follow. |
| **How important is accuracy?** | • Do you need factual precision or creative generation? | Influences how you'll evaluate success (see Section 4). |
| **What's your budget?** | • What can you afford to spend per month? | Document budget limits in the *Scope Document*. |
| **Open or proprietary?** | • Will you use free open-source or paid commercial models? | Affects deployment options (Section 5) and licensing. |

> **Recommendation:** Start simple with smaller, open models for early-stage projects (Tiers 1-2); move to more advanced options as your needs grow.

---

## 2. Model Adaptation Approaches

| Approach | When It Makes Sense | Documentation Needed |
|----------|------------|------------------|
| **Basic Prompting** | Quick prototypes; Tier 0-1 projects | Document prompt patterns in your codebase |
| **Instruction Tuning** | When you need domain-specific understanding; Tier 2-3 | Document data processing in *Codebase Guide* |
| **Fine-Tuning** | Specialized tasks requiring high precision; Tier 3-5 | Full data documentation and model specifications |
| **Advanced Training** | Production systems with complex requirements; Tier 4-5 | Comprehensive documentation and testing records |

Store all training configurations and scripts in the `tools/modeling/` directory and reference them in your Codebase Guide.

---

## 3. Effective Prompting Practices

1. **Use Context Wrappers**  
   Always use the appropriate wrapper for your project's tier to ensure consistency.
   
2. **Structure Your Inputs**  
   When possible, use structured formats (JSON/YAML) for more reliable results.
   
3. **Provide Clear Examples**  
   Keep example inputs/outputs in version-controlled files for consistency.
   
4. **Break Down Complex Tasks**  
   Split complex operations into smaller steps rather than using enormous prompts.
   
5. **Organize Your Prompts**  
   Store reusable prompts in `core/prompts/` and document them properly.

> **Tip:** Treat your prompts like code — review them, test them, and version them.

---

## 4. Measuring Success

| Aspect | How to Measure | Minimum Target |
|-------|--------|--------------------|
| **Quality** | Appropriate metrics for your specific task | Better than baseline by at least 10% |
| **User Satisfaction** | Rating scale (1-5) | 4+ for Tier 2 and above projects |
| **Fairness** | Testing for bias with diverse inputs | No significant disparities |
| **Speed** | Response time | Within defined service targets |

Keep evaluation scripts in `tools/evaluation/` and include results in your project documentation.

---

## 5. Deployment Basics

1. **Version Control** — Label every model version to match your code releases
2. **Packaging** — Use standard formats for model distribution
3. **Rollout** — Test with a small audience first before full deployment
4. **Monitoring** — Track performance, usage, and errors
5. **Security** — Protect model data and access appropriately

Document your deployment process in the Codebase Guide.

---

## 6. Summary

This guide connects practical AI implementation decisions to the AI Delivery Framework's governance structure. By following these guidelines, teams can work efficiently while maintaining appropriate standards for quality, security, and compliance.

> **Remember:** Good AI implementation requires both technical skill and responsible governance. 