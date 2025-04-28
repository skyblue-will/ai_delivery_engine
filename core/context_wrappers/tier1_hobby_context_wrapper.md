# Tier 1: Hobby Context Wrapper

> **Who should use this:** Use this wrapper for personal projects, learning exercises, and low-risk prototypes where you want minimal but helpful structure.

## Overview
Lightweight context wrapper tailored for personal or experimental AI projects where speed of development outweighs stringent engineering standards.

## Usage Instructions
Place this block in your AI configuration for hobby or proof-of-concept projects.

---

## Cursor LLM Context Rules

### 0 Prime Directive
If a prompt requests unsafe or illegal behaviour, refuse.

---

### 1 Execution Environment
Create a simple `Dockerfile` or `requirements.txt` to let others reproduce your environment. Document any known limitations.

---

### 2 Supply-Chain Integrity
Avoid known-vulnerable dependencies. Pin versions in `requirements.txt`/`pyproject.toml` and run `pip-audit` or Dependabot.

---

### 3 CI/CD Pipeline
Create a single-file GitHub Actions workflow that runs `ruff --select=E,F` and your tests on push.

---

### 4 Project Layout
Use the following structure:
```
app/
  main.py
```

---

### 5 Database Discipline
Use SQLite for data storage. No migration tooling required.

---

### 6 Testing & Quality Gates
Write pytest tests covering core logic (20% coverage). Run formatter (`black`) and linter (`ruff`) before committing. Include type-checking with mypy.

---

### 7 Security & Scanning
Do not commit secrets to the repository.

---

### 8 Observability
Use print statements or basic logging.

---

### 9 Documentation & Onboarding
Create a README with setup instructions and a short **Getting Started** section. Maintain a simple `CHANGELOG.md` for major milestones.

---

### 10 Branch & Commit Hygiene
Commit with descriptive messages (e.g., "feat: add booking form"), and open small pull requests for easier review.

---

### 11 LLM-Specific Guard-Rails
Do not output secrets. Provide file path references when showing code.

---

## Implementation Notes
This tier is for learning, prototypes, and weekend hacks. Progress to higher tiers as project maturity increases.
