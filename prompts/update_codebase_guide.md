# Codebase Guide Update Template

## Purpose and Importance

This template helps you update the AI Delivery Engine's `core/codebase_guide.md`, which serves as the authoritative reference for the current state of the codebase.

**Why This Matters:**
- **Single Source of Truth**: The codebase guide provides an accurate snapshot of the system that all team members and AI tools can rely on.
- **Onboarding Efficiency**: New developers can quickly understand the system without extensive exploration.
- **AI Context Reliability**: Ensures AI tools have accurate, up-to-date information when generating code or providing recommendations.
- **Governance Anchor**: Acts as a central reference point for compliance and architectural decisions.
- **Drift Prevention**: Regular updates prevent documentation from becoming outdated and misleading.

---

## 🔧 Task  
Rewrite codebase_guide.md so it mirrors the code **exactly as it exists right now**, and refresh the C4 diagrams.

## 🧭 Rules  
1. No speculation, TODOs, or future-feature notes.  
2. Every statement must map to code you can point at today.  
3. Match repo naming/casing verbatim.  
4. Keep it short, factual, and in plain English.

## 🗂️ Deliverable – include these sections in this order  
1. **Project Structure** – top-level dirs & purpose.  
2. **Key Modules & Components** – one-liner per module/class.  
3. **Data Flow** – request ➜ processing ➜ persistence ➜ response.  
4. **Entry Points & Core Logic** – CLIs, services, jobs.  
5. **Known Quirks / Tech Debt** – only what's visible in code.  
6. **C4 Diagrams** – Context, Container, Component images (see below).

## 🖼️ Diagram Step  
• Use the `diagrams` Python library to (re)generate Context, Container, and Component diagrams.  
• Save PNGs to `docs/architecture/` with filenames `c4_<level>.png`.  
• Add markdown image links in section 6 of the guide.

## 🧠 Voice  
Write for a new engineer who must ship a bug-fix today.

## 🔎 Self-Check  
‣ "grep" the repo for evidence of every bullet.  
‣ No future plans or README fiction.  
‣ Delete fluff.

## ✏️ Output  
1. Overwrite `core/codebase_guide.md` with the updated content.  
2. Commit the new/updated diagram PNGs in `docs/architecture/`.

## Example Usage

```
/update_codebase_guide
```

This update must be performed after each significant change to the codebase. The Codebase Guide is a critical governance document that provides an accurate, current snapshot of the system - maintaining the **present reality** pillar of the Governance Core. 