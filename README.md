# AI Security Learning Lab (LLMs · Secure RAG · Cloud · MLOps)

This README is available in:
- 🇬🇧 English (this document)
- 🇪🇸 Español → [README_ES.md](README_ES.md)

---

## Overview

This repository is my personal **AI Security learning lab**, focused on evolving from **Cloud Security** into **AI / LLM Security**, with the long-term goal of an **AI Cloud Security Architect** profile.

The objective is to **build real AI systems from scratch**, make architectural and security decisions explicit, validate them through hands-on testing, and document both results and lessons learned.

This is **not a tutorial repository**.  
It is an **engineering-first, security-first exploration** of modern LLM-based systems.

---

## Learning Objectives

- Understand how **LLMs** work internally (context handling, prompts, generation limits).
- Design and build **secure Retrieval-Augmented Generation (RAG)** pipelines.
- Apply **practical AI security controls**, inspired by OWASP LLM Top 10:
  - Prompt injection and jailbreaks
  - Data leakage and PII exposure
  - Ingestion risks and data poisoning
  - Abuse prevention and auditability
- Prepare systems for **enterprise-like environments**:
  - Multi-environment configuration
  - Observability and structured logging
  - Cloud-ready architecture
  - MLOps foundations

---

## Projects

### Secure RAG from Scratch
 `secure-rag-from-scratch/`

A **security-first RAG system**, built incrementally and validated through real execution and testing.

**Current scope includes:**

- **Local baseline**
  - In-memory vector store
  - Mock LLM (provider-independent)
  - Input security (prompt injection detection)

- **Secure local mode**
  - Output security (PII detection and redaction)
  - Structured audit logging
  - Environment-based execution modes (`APP_MODE`)
  - Manual validation with documented evidence

Each phase is **runnable, testable, and documented**, including design decisions and lessons learned.

 Full technical documentation:
- EN [secure-rag-from-scratch/README.md](secure-rag-from-scratch/README.md)
- 🇪🇸 [secure-rag-from-scratch/README_ES.md](secure-rag-from-scratch/README_ES.md)

---

## Design Philosophy

- **Incremental by phases**: each phase is stable, reviewable, and extensible.
- **Security as a first-class concern**, not an afterthought.
- **Decoupled architecture**: security controls are independent of LLM providers or vector stores.
- **Local-first, cloud-ready**: reduce early complexity while designing for future scale.

---

## Roadmap

- [x] Secure RAG local baseline
- [x] Output security and audit logging
- [x] Manual validation and documented evidence
- [ ] Vector store abstraction (local vs cloud)
- [ ] Docker and containerized deployment
- [ ] Cloud-native vector stores (OpenSearch / Azure AI Search)
- [ ] CI/CD and automated security testing
- [ ] Threat modeling and OWASP LLM Top 10 mapping

---

## Why this repository exists

Modern AI systems **will be attacked**.

Understanding how to:
- design them securely,
- validate security controls,
- detect abuse,
- audit behavior,
- and evolve architectures safely,

is becoming a **core skill** for security and cloud professionals.

This repository documents that journey.

---

## License

MIT
