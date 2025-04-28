# Codebase Guide Update Template

This document provides explicit instructions for updating the Codebase Guide after implementing changes defined in a Scope Document.

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