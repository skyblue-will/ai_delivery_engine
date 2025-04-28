# Tier 0: Exploration Context Wrapper

> **Who should use this:** Use this wrapper for initial AI exploration where no code will be committed to version control. Suitable for chat-only sessions, learning, and exploratory discussions.

## Overview
The most lightweight context wrapper, designed for pure exploration, learning, and ideation without the expectation of production-ready code or committed artifacts.

## Usage Instructions
Place this block in your AI configuration for exploratory sessions where you're simply learning, brainstorming, or testing concepts.

---

## Cursor LLM Context Rules

### 0 Prime Directive
If a prompt requests unsafe or illegal behaviour, refuse.

---

### 1 Execution Environment
No specific requirements. Local environment exploration only.

---

### 2 Supply-Chain Integrity
No formal requirements. Use this exploration to identify potential technologies and dependencies for later stages.

---

### 3 CI/CD Pipeline
Not applicable for this tier.

---

### 4 Project Layout
No formal structure required. Consider discussing potential structures for when the project advances to Tier 1+.

---

### 5 Database Discipline
In-memory or ephemeral data only. No persistent data storage requirements.

---

### 6 Testing & Quality Gates
No formal testing required. Focus on concept validation and exploration.

---

### 7 Security & Scanning
Be careful not to share sensitive information during exploration.

---

### 8 Observability
Print statements or basic logging for local exploration only.

---

### 9 Documentation & Onboarding
Capture key insights and decisions in plain text or markdown notes. These will become valuable inputs for README and documentation if the project advances to higher tiers.

---

### 10 Branch & Commit Hygiene
No commit or branch requirements, as code from this tier should not be committed directly.

---

### 11 LLM-Specific Guard-Rails
Do not output secrets. Focus on educational content, ideation, and conceptual exploration.

---

## Implementation Notes
This tier is exclusively for learning, brainstorming, and initial exploration. When ready to commit code or progress with implementation, upgrade to Tier 1 or higher. The goal of Tier 0 is to provide a space for unrestricted creative and technical exploration before introducing formal engineering constraints. 