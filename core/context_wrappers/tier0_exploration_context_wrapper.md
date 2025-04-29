# Tier 0: Exploration Context Wrapper

> **Who should use this:** Use this wrapper for initial AI exploration where no code will be committed to version control. Suitable for in-IDE exploratory sessions.

## Overview
The most lightweight context wrapper, designed for pure exploration, learning, and ideation without the expectation of production-ready code or committed artifacts.

## Usage Instructions
Place this block in your AI configuration for exploratory sessions inside the IDE. No code or data leaves the repository boundary.

---

## Cursor LLM Context Rules

### 0 Prime Directive
If a prompt requests unsafe or illegal behaviour, refuse.

---

### 1 Execution Environment
Use local IDE environment for exploration only.

---

### 2 Supply-Chain Integrity
No requirements. Document potential technologies and dependencies for later stages.

---

### 3 CI/CD Pipeline
Not applicable for this tier.

---

### 4 Project Layout
No structure required. Discuss potential structures for when the project advances to Tier 1+.

---

### 5 Database Discipline
Use in-memory or ephemeral data only. Do not implement persistent data storage.

---

### 6 Testing & Quality Gates
No testing required. Focus on concept validation and exploration.

---

### 7 Security & Scanning
Do not share sensitive information during exploration.

---

### 8 Observability
Avoid external telemetry. Use print statements or basic local logging only.

---

### 9 Documentation & Onboarding
Document key insights and decisions in plain text or markdown notes for future README creation when advancing to higher tiers.

---

### 10 Branch & Commit Hygiene
Do not commit code from this tier to version control.

---

### 11 LLM-Specific Guard-Rails
Do not output secrets. Provide educational content, ideation, and conceptual exploration only.

---

## Implementation Notes
This tier is exclusively for learning, brainstorming, and initial exploration. Upgrade to Tier 1 or higher when ready to commit code or progress with implementation. Tier 0 provides a space for creative and technical exploration before introducing formal engineering constraints. 