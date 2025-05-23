# Tier 5: Enterprise Context Wrapper

> **Who should use this:** Use this wrapper for enterprise-grade applications, regulated industry systems, and projects requiring the highest levels of security, compliance, and reliability.

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

2. **No virtualenvs — 100% of tooling and tests run inside the Docker image**  
   * Invoke all lint, test, and build commands via `docker compose run …`.  
   * Use the same pinned image for local development; maintain zero drift between dev, CI, and prod.

---

### 2 Supply-Chain Integrity  
1. **SLSA 3+**: Emit provenance JSON from build workflow, stored with the image.  
2. **cosign / gitsign**: Sign all images and commits; block unsigned artifacts in CD.  
3. **SBOM**: Generate CycloneDX (`syft`) on every build; fail if *any* high/critical CVE remains unpatched.

---

### 3 CI/CD Pipeline (GitHub Actions unless told otherwise)  
```
lint → test → build → sbom+scan → sign → provenance → deploy(canary) → promote
```
* Implement progressive delivery (blue/green or Flagger) with auto-rollback on error-budget burn.  
* Enforce OPA/Kyverno policy gate: only signed artifacts with passing SLSA, SBOM, CVE scan, and secret-scan will deploy.  
* Use OIDC keyless pushes; prohibit long-lived registry credentials.

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
* Use Async FastAPI; exclude all logic from `routes/`.  
* Keep DTOs and ORM models separate.  
* Store settings only in `pydantic_settings` + env vars; never hard-code.

---

### 5 Database Discipline  
* Create one Alembic migration per schema change; prohibit autogenerate without manual edit + review.  
* Run `upgrade head && downgrade -1` on disposable DB in CI.  
* For destructive migrations, require reversible script or back-fill.

---

### 6 Testing & Quality Gates  
* Achieve 90% line + 70% mutation coverage (`mutmut`) with **pytest**.  
* Configure `pre-commit` with ruff, black, isort, mypy, bandit, gitleaks, detect-secrets.  
* Create OpenAPI snapshot; break build on diff.  
* Write property-based tests (Hypothesis) for core data paths; implement contract tests for external APIs.

---

### 7 Security Runtime & Scanning  
* Run IaC scan (`tfsec`/`checkov`) for all Terraform/Pulumi.  
* Schedule fuzzing (oss-fuzz) and DAST (OWASP ZAP) nightly.  
* Enforce Falco/eBPF rules in production.  

---

### 8 Observability & Reliability  
* Implement OpenTelemetry traces, metrics, logs (OTLP exporter).  
* Create `/healthz`, `/readyz` endpoints and handle graceful shutdown via `lifespan`.  
* Enable continuous profiling (Pyroscope).  
* Define SLOs + error budgets; block deployment if burn rate > 2 × budget.

---

### 9 Documentation & Onboarding  
* Create `docs/` via MkDocs; fail CI on broken links.  
* Store ADRs in `docs/adr/`.  
* Update `codebase_guide.md` (repo root) only on explicit "Update the codebase guide" prompt; trace every sentence to code.  
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
* When asked "check codebase vs vX.Y.Z", compare code to that file line-by-line and report discrepancies with file-path evidence.  
* Treat scope files as **read-only**.

---

### 11 Branch, Commit & Release Hygiene  
* Use trunk-based development; limit feature branches to short lifespan, squash-merge via PR.  
* Follow Conventional Commits, sign with gitsign; generate changelog on tag.  
* Tag Docker images as `v<semver>-<gitsha>`; never use `latest`.

---

### 12 LLM-Specific Guard-Rails  
1. Never emit secrets, personal data, or license-incompatible code.  
2. Include file paths or commit SHAs when claiming "implemented."  
3. Run static analysis after generation; block any commit if scans fail.

---

### 13 Provenance & Watermarking Requirement
All AI-generated code or content must include embedded attribution indicating:
- The tool used (e.g. Cursor, Copilot, etc.)
- Generation timestamp (ISO 8601 format)
- Responsible entity: {{ CompanyNameOrDeveloper }}

This watermark must be:
- Included in file headers or docstrings (for code)
- Persistently trackable across commits
- Verifiable during audits via structured diff or metadata analysis

**Compliance is binary**: any generated artifact without a valid watermark fails verification.  
The Assurance Core's LLM structural diff will automatically verify watermark presence.

---

## Implementation Notes

* This context wrapper defines the most rigorous enterprise-grade configuration.
* Apply the entire context when building mission-critical applications.
* All security, compliance, and operational requirements are non-negotiable.
* Verify each directive is enforced by CI/CD pipelines.