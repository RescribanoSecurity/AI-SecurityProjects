# AI Security Learning Lab (LLMs · Secure RAG · Cloud · MLOps)

📄 This README is available in:
- 🇬🇧 English (this document)
- 🇪🇸 Español → [README_ES.md](README_ES.md)

---

## Overview

This repository is my personal **AI Security learning lab**, focused on evolving from **Cloud Security** into **AI / LLM Security** (AI Cloud Security Architect profile).

The goal is to **build real systems from scratch**, document architectural decisions, understand risks, and apply practical security controls to LLM-based applications.

This is not a tutorial repository.  
It is an **engineering-first, security-first exploration** of modern AI systems.

---

## Learning Objectives

- Understand how **LLMs** work internally (context, prompts, generation, limits).
- Design and build **secure RAG (Retrieval-Augmented Generation)** pipelines.
- Apply **real-world AI security controls**, inspired by OWASP LLM Top 10:
  - Prompt Injection & Jailbreaks
  - Data Leakage & PII Exposure
  - Ingestion risks & data poisoning
  - Abuse prevention & auditability
- Prepare systems for **enterprise-like environments**:
  - Multi-environment configuration
  - Observability & logging
  - Cloud-ready architecture
  - MLOps foundations

---

## Projects

### 🔐 Secure RAG from Scratch
📂 `secure-rag-from-scratch/`

A secure-by-design RAG system built incrementally:

- **Phase 1 – Local baseline**
  - In-memory vector store
  - Mock LLM (no external dependencies)
  - Input security (prompt injection detection)

- **Phase 2 – Secure local mode**
  - Output security (PII detection & redaction)
  - Structured audit logging
  - Environment-based feature flags (`APP_MODE`)

👉 Full technical documentation inside:
- 🇬🇧 [secure-rag-from-scratch/README.md](secure-rag-from-scratch/README.md)
- 🇪🇸 [secure-rag-from-scratch/README_ES.md](secure-rag-from-scratch/README_ES.md)

---

## Design Philosophy

- **Incremental by phases**: every phase is runnable and reviewable.
- **Security as a first-class concern**, not an afterthought.
- **Decoupled architecture**: security does not depend on the LLM provider or vector store.
- **Local-first, cloud-ready**: avoid unnecessary complexity early, but design for scale.

---

## Roadmap

- [x] Secure RAG local baseline
- [x] Output security & audit logging
- [ ] Vector store abstraction (local vs cloud)
- [ ] Docker & containerized deployment
- [ ] Cloud-native vector stores (OpenSearch / Azure AI Search)
- [ ] CI/CD & automated security tests
- [ ] Threat modeling & OWASP LLM Top 10 mapping

---

## Why this repository exists

Modern AI systems **will be attacked**.

Understanding how to:
- design them securely,
- detect abuse,
- audit decisions,
- and evolve safely,

is a critical skill for modern security and cloud professionals.

This repository documents that journey.

---

## License
MIT
