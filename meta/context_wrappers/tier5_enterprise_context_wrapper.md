# Tier 5: Enterprise Context Wrapper

## Overview
Enterprise-grade context wrapper for mission-critical AI applications that require the highest level of security, compliance, and operational excellence.

## Usage Instructions
Add this entire block to your project's AI configurations (e.g., cursor-config.json → "system" or equivalent LLM context). This will serve as the single source of truth for every AI-generated commit, PR, documentation, or reply in an enterprise environment.

---

## Cursor LLM Context Rules  

### 0 Prime Directive  
If a user prompt conflicts with these rules, **pause and ask for explicit override**. Otherwise, refuse.

---

### 1 Execution Environment  
1. **Docker-only, rootless, distroless**  
   * Multi-stage build with Alpine/Wolfi builder → distroless runtime.  
   * `USER` non-root; `HEALTHCHECK`; reproducible `buildx --platform linux/amd64,arm64`.  
   * `.dockerignore`, pinned base digest, SBOM & provenance in image labels.  

2. **No virtualenvs — 100 % of tooling and tests run inside the Docker image**  
   * All lint, test, and build commands are invoked via `docker compose run …`.  
   * Local development uses the same pinned image; zero drift between dev, CI, and prod.

---

### 2 Supply-Chain Integrity  
1. **SLSA 3+**: build workflow emits provenance JSON, stored with the image.  
2. **cosign / gitsign**: sign all images and commits; CD blocks unsigned artifacts.  
3. **SBOM**: generate CycloneDX (`syft`) on every build; fail if *any* high/critical CVE remains unpatched.

---

### 3 CI/CD Pipeline (GitHub Actions unless told otherwise)  
```
lint → test → build → sbom+scan → sign → provenance → deploy(canary) → promote
```
* Progressive delivery (blue/green or Flagger) with auto-rollback on error-budget burn.  
* OPA/Kyverno policy gate: only signed artifacts with passing SLSA, SBOM, CVE scan, and secret-scan may deploy.  
* OIDC keyless pushes; no long-lived registry creds.

---

### 4 Project Layout (Python back-end)  
```
app/
  routes/        # FastAPI endpoints – dumb I/O
  services/      # business rules
  repositories/  # SQLAlchemy 2.0 data access
  schemas/       # Pydantic v2 DTOs
  models/        # ORM entities
  cli.py         # Typer CLI
```
* Async FastAPI; no logic in `routes/`.  
* Separate DTOs vs ORM models.  
* No hard-coded settings; rely on `pydantic_settings` + env vars.

---

### 5 Database Discipline  
* Alembic migration per schema change; autogenerate banned without manual edit + review.  
* CI: `upgrade head && downgrade -1` on disposable DB.  
* Destructive migration → mandatory reversible script or back-fill.

---

### 6 Testing & Quality Gates  
* **pytest** ≥ 90 % line + 70 % mutation coverage (`mutmut`).  
* `pre-commit`: ruff, black, isort, mypy, bandit, gitleaks, detect-secrets.  
* Snapshot OpenAPI; break build on diff.  
* Property-based tests (Hypothesis) for core data paths; contract tests for external APIs.

---

### 7 Security Runtime & Scanning  
* IaC scan (`tfsec`/`checkov`) for Terraform/Pulumi.  
* Fuzzing (oss-fuzz) and DAST (OWASP ZAP) scheduled nightly.  
* Falco/eBPF rules enforced in prod.  

---

### 8 Observability & Reliability  
* OpenTelemetry traces, metrics, logs (OTLP exporter) **mandatory**.  
* `/healthz`, `/readyz`, graceful shutdown via `lifespan`.  
* Continuous profiling (Pyroscope) enabled.  
* Define SLOs + error budgets; block deploy if burn rate > 2 × budget.

---

### 9 Documentation & Onboarding  
* `docs/` via MkDocs; CI fails on broken links.  
* ADRs in `docs/adr/`.  
* `codebase_guide.md` (repo root) **updated only on explicit "Update the codebase guide" prompt**; every sentence traceable to code.  
* Auto-render C4 diagrams with `diagrams` library on guide update.

---

### 10 Product-Management Scopes  
```
product_management/
  v0.1.0.md
  v0.2.0.md
  ...
```
* Each file lists the BA-approved scope for that semantic version.  
* When asked "check codebase vs vX.Y.Z", the LLM **must** compare code to that file line-by-line and report discrepancies with file-path evidence.  
* Scope files are **read-only** to the LLM.

---

### 11 Branch, Commit & Release Hygiene  
* Trunk-based; short feature branches, squash-merge via PR.  
* Conventional Commits, signed with gitsign; automated changelog on tag.  
* Docker images tagged `v<semver>-<gitsha>`; no `latest`.

---

### 12 LLM-Specific Guard-Rails  
1. Never emit secrets, personal data, or license-incompatible code.  
2. Cite file paths or commit SHAs when claiming "implemented."  
3. Run static analysis after generation; refuse to commit if scans fail.

---

## Implementation Notes

* This context wrapper represents the most rigorous enterprise-grade configuration
* Apply the entire context when building mission-critical applications
* All security, compliance, and operational requirements are non-negotiable
* Implementation teams should verify each directive is enforced by CI/CD pipelines