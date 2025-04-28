# Tier 2: MVP Context Wrapper

> **Who should use this:** Use this wrapper for early-stage startup MVPs, proof-of-concept projects for stakeholders, and projects that may handle basic user data.

## Overview
Context wrapper for Minimum Viable Product (MVP) AI projects that prioritise rapid iteration and user feedback while maintaining baseline engineering hygiene.

## Usage Instructions
Include this block in your AI configuration to guide AI-generated content during MVP development cycles.

---

## Cursor LLM Context Rules

### 0 Prime Directive
If a user prompt conflicts with these rules, **seek clarification**. Otherwise, comply.

---

### 1 Execution Environment
1. **Docker optional but encouraged**  
   * Simple Dockerfile with single-stage build acceptable.  
   * `USER` may run as root; document security implications.
2. Local runs permitted outside Docker for speed, but CI must run in a container.

---

### 2 Supply-Chain Integrity
1. Generate SBOM if tooling available; no hard requirement.  
2. No signing requirement, but note unsigned builds.

---

### 3 CI/CD Pipeline
```
lint → test → build → staging
```
* Automatic deployment to staging; production manual.  
* Secret scanning mandatory.

---

### 4 Project Layout (Python)
Minimal recommended structure:
```
app/
  routes/
  services/
```

---

### 5 Database Discipline
* Migrations optional; lightweight ORM like SQLModel acceptable.  
* Manual DB changes allowed in early iterations.

---

### 6 Testing & Quality Gates
* **pytest** ≥ 50 % line coverage.  
* `pre-commit`: black, ruff basic linting.  
* No mutation coverage requirement.

---

### 7 Security & Scanning
* Secret scanning must pass.  
* High CVEs flagged but not blocker.

---

### 8 Observability
Basic logging to stdout; optional metrics.

---

### 9 Documentation & Onboarding
Keep README up to date; other docs optional.

---

### 10 Branch, Commit & Release Hygiene
* Feature branches; merge when tests pass.  
* Conventional Commits recommended but not enforced.

---

### 11 LLM-Specific Guard-Rails
1. Avoid secrets; redact if necessary.  
2. Provide file path references when showing code.

---

## Implementation Notes
Tier 2 focuses on shipping value quickly to validate market fit. Engineering safeguards are lighter but still provide baseline quality.
