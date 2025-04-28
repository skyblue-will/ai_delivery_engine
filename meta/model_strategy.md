# **AI Model Strategy Guide — AI Delivery Framework**

---

## 🎯 Purpose

Provide a concise, governance-aligned reference for **selecting, adapting, and operating AI models** inside projects that adopt the AI Delivery Framework. This guide connects everyday model decisions to the framework's governance core — *Codebase Guide*, *Scope Documents*, and *Context Wrappers* — ensuring technical choices stay transparent, auditable, and upgrade-ready.

*
Who should read this?* Machine-learning engineers, architects, and delivery leads who need clear guard-rails for model operations without slowing down iteration speed.

---

## 1. Model Selection Criteria

| Dimension | Questions to Ask | Governance Tie-In |
|-----------|-----------------|-------------------|
| **Use Case Fit** | • What artefact must the model produce?  <br>• What latency/throughput is acceptable? | Must be stated in the active *Scope Document* under **Functional Requirements**. |
| **Data Sensitivity** | • Does the task involve personal or regulated data? | Determines minimum *Delivery Tier* and activates GDPR-Lite or full compliance modules. |
| **Accuracy vs. Creativity** | • Is factual correctness paramount or is exploratory generation acceptable? | Drives evaluation metrics in §5 and prompts structure in §3. |
| **Cost Envelope** | • What is the target run-rate per call / month? | Must be budgeted in the *Scope Document*; audited in CI cost guardrails. |
| **Model Openness** | • Open-source, proprietary API, or bespoke? | Affects **Deployment Considerations** in §6 and licensing checks. |

> **Recommendation:** Default to a **small, open model** for Tier 1–2 projects; graduate to larger proprietary or fine-tuned variants as accuracy and scale demands rise.

---

## 2. Fine-Tuning & Adaptation Approaches

| Approach | When to Use | Tooling | Compliance Gates |
|----------|------------|---------|------------------|
| **Prompt-only** (zero / few-shot) | Rapid prototyping; Tier 0-1 | Context Wrapper | None |
| **Instruction Tuning** | Stable tasks with domain-specific phrasing; Tier 2-3 | PEFT / LoRA on open models | Data processing documentation required in *Codebase Guide*. |
| **Full Fine-Tuning** | High-precision, domain-sensitive workloads; Tier 3-5 | Off-line training pipeline (e.g., HuggingFace Trainer) | Full data governance (GDPR, model cards). |
| **RLHF / RLAIF** | Complex preference alignment, production chatbots; Tier 4-5 | Dedicated RL stack | Mandatory internal audit + red-teaming. |

Implementation artefacts (configs, scripts, datasets) **must live in `tools/modeling/`** and be referenced by the Codebase Guide.

---

## 3. Prompt Engineering Best Practices

1. **System Layer = Context Wrapper**  
   Always inject the tier-appropriate wrapper before any user or developer messages.
2. **Structured Inputs**  
   Where possible, favour JSON/YAML payloads for deterministic parsing downstream.
3. **Few-Shot Canonical Examples**  
   Maintain examples in version-controlled fixture files; update alongside feature changes.
4. **Streaming & Tool Calls**  
   Decompose complex tasks into tool-enabled sub-calls rather than massive prompts.
5. **Prompt Registry**  
   Store reusable prompt files in `core/prompts/` and document them in the Codebase Guide.

> **Tip:** Treat prompts as **first-class code** — reviewed, tested, and versioned.

---

## 4. Evaluation Methodology

| Layer | Metric | Minimum Acceptance |
|-------|--------|--------------------|
| **Offline** | BLEU / ROUGE / accuracy depending on task | ≥ baseline open-model score +10% |
| **Human Review** | Likert 1-5 usefulness | ≥ 4 for Tier 2+, documented in PR description |
| **Fairness & Bias** | Bias amplification on synthetic sets | No *critical* disparities (Δ < 5 pp) |
| **Performance** | p95 latency | < 2× target SLO |

Evaluation scripts live under `tools/evaluation/` and must be **CI-executable**. Results are attached to PR artefacts and summarised in the Scope Document's *Acceptance* section.

---

## 5. Deployment Considerations

1. **Model Versioning** — Tag every model artefact with *semantic version* matching the repository release (e.g., `v0.2.0-model`).
2. **Packaging** — Use [OpenAI Model Packaging Standard 2025] or Docker images pushed to an internal registry.
3. **Rollout Strategy** — Canary first, guarded by feature flags for Tier 3+.
4. **Observability** — Emit structured logs (`prompt`, `response`, `latency_ms`, `token_count`).
5. **Security** — Encrypt model weights at rest; enforce least-privilege IAM for inference APIs.

Deployment templates and scripts must be referenced in the Codebase Guide *Deployment Process* section.

---

## 6. Summary

The AI Model Strategy Guide links day-to-day modelling choices to the AI Delivery Framework's governance spine. By following the selection matrix, fine-tuning gates, prompt best practices, and evaluation criteria herein, teams can iterate quickly **without losing compliance, transparency, or control**.

> **Remember:** *Every model decision is also a governance decision.* 