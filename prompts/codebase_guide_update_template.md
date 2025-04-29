# Codebase Guide Update Template

## Purpose and Importance

This template is designed to be copied and pasted as a prompt for AI tools like Cursor or Winsurf. When provided to these AI assistants, it will guide them to properly update the AI Delivery Engine's `codebase_guide.md`, which serves as the authoritative reference for the current state of the codebase.

**Why This Matters:**
- **Single Source of Truth**: The codebase guide provides an accurate snapshot of the system that all team members and AI tools can rely on.
- **Onboarding Efficiency**: New developers can quickly understand the system without extensive exploration.
- **AI Context Reliability**: Ensures AI tools have accurate, up-to-date information when generating code or providing recommendations.
- **Governance Anchor**: Acts as a central reference point for compliance and architectural decisions.
- **Drift Prevention**: Regular updates prevent documentation from becoming outdated and misleading.

To use this template, simply copy the entire contents of this file and paste it as a prompt to your AI assistant (Cursor, Winsurf, etc.) after implementing changes defined in a Scope Document. The AI will then analyze your codebase and generate an updated codebase guide that reflects the actual state of the code.

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
1. Overwrite `codebase_guide.md` with the updated content.  
2. Commit the new/updated diagram PNGs in `docs/architecture/`.

---

**Note:** This update must be performed after each significant change to the codebase. The Codebase Guide is a critical governance document that provides an accurate, current snapshot of the system. It is the canonical reference for all team members and AI tools working with the codebase. 