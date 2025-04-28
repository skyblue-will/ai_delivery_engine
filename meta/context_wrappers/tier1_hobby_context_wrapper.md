# Tier 1: Hobby Context Wrapper

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
Docker optional. A simple `Dockerfile` or `requirements.txt` is recommended to let others reproduce your environment. Document any known limitations.

---

### 2 Supply-Chain Integrity
No formal requirements, but avoid known-vulnerable dependencies. Pin versions in `requirements.txt`/`pyproject.toml` and run `pip-audit` or Dependabot if possible.

---

### 3 CI/CD Pipeline
Manual testing acceptable. A single-file GitHub Actions workflow that runs `ruff --select=E,F` and your tests on push is strongly encouraged.

---

### 4 Project Layout
Flexible. Recommended structure:
```
app/
  main.py
```

---

### 5 Database Discipline
SQLite allowed. No migration tooling required.

---

### 6 Testing & Quality Gates
Aim for a handful of **pytest** tests covering core logic (~20 % coverage). Always run a formatter (`black`) and linter (`ruff`) before committing. Type-checking with **mypy** is a nice-to-have.

---

### 7 Security & Scanning
No mandatory scans. Avoid committing secrets.

---

### 8 Observability
Print statements or basic logging.

---

### 9 Documentation & Onboarding
README with setup instructions and a short **Getting Started** section. Maintain a simple `CHANGELOG.md` for major milestones.

---

### 10 Branch & Commit Hygiene
Commit often with descriptive messages (e.g., "feat: add booking form"), and open small pull requests for easier review.

---

### 11 LLM-Specific Guard-Rails
Do not output secrets. Provide file path references when helpful.

---

## Implementation Notes
Ideal for learning, prototypes, and weekend hacks. Strive for incremental improvements—today's hobby project can become tomorrow's startup. Upgrade to higher tiers as project maturity increases.
