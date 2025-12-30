# AI Security Learning Lab  
*(LLMs · Secure RAG · Cloud · MLOps)*

This README is available in:
- 🇬🇧 EN English (this document)
- 🇪🇸 ES Español → [README_ES.md](README_ES.md)

---

## Overview

This repository is my personal **AI Security learning lab and project index**, documenting my transition from **Cloud Security** into **AI / LLM Security**, with the long-term goal of an **AI Cloud Security Architect** profile.

The focus is on **building real AI systems from scratch**, making **security and architectural decisions explicit**, validating them through hands-on testing, and documenting both **results and failures**.

This is **not a tutorial repository**.  
It is an **engineering-first, security-first exploration** of modern LLM-based systems.

---

## Learning Objectives

- Understand how **LLMs** work internally (context windows, prompts, generation behavior).
- Design and build **secure Retrieval-Augmented Generation (RAG)** pipelines.
- Apply **practical AI security controls**, inspired by the **OWASP LLM Top 10**:
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

### 🔬 Secure RAG from Scratch — Version 1 (Legacy Lab)
📁 `secure-rag-from-scratch/`

This project represents the **first exploratory iteration** of Secure RAG.

Its goal was to:
- Understand the core mechanics of RAG systems
- Experiment with early **input security controls**
- Validate basic assumptions before introducing infrastructure complexity

**Key characteristics of V1:**
- Local-only execution
- In-memory vector store
- Mock LLM (provider-independent)
- Initial prompt injection detection
- Manual testing and documentation

⚠️ **This version is now considered a legacy learning lab.**

👉 The actively developed and extended version is **Secure RAG v2**, available as a standalone repository.

---

### 🚀 Secure RAG from Scratch — Version 2 (Main Project)

🔗 Repository:  
https://github.com/RescribanoSecurity/secure-rag-from-scratch-v2

Secure RAG v2 is the **main, production-grade learning project**, evolving directly from the lessons learned in V1.

**Focus areas include:**
- Modular RAG pipeline architecture
- Input **and output security controls**
- PII detection, redaction, and output blocking
- OWASP LLM Top 10 mapping
- Dockerized infrastructure
- Real vector database (Qdrant)
- Auditability and request tracing
- Visual validation via Streamlit UI

This project is:
- Runnable
- Testable
- Evidence-driven
- Explicit about what is implemented and what is not

📄 Full documentation, screenshots, and technical presentations are maintained **inside the V2 repository**.

---

## Design Philosophy

- **Incremental by phases**: each phase is stable, reviewable, and extensible.
- **Security as a first-class concern**, not an afterthought.
- **Decoupled architecture**: security controls are independent of LLM providers or vector stores.
- **Local-first, cloud-ready**: reduce early complexity while designing for future scale.
- **Failures are documented**, not hidden.

---

## Roadmap (High-Level)

- [x] Secure RAG local baseline (V1)
- [x] Input security controls
- [x] Output security (PII detection, redaction, blocking)
- [x] Manual validation with documented evidence
- [ ] Cloud-native vector stores (OpenSearch / Azure AI Search)
- [ ] Authentication and identity-aware logging
- [ ] Persistent audit logs
- [ ] CI/CD and automated security testing
- [ ] Threat modeling and full OWASP LLM Top 10 enforcement

---

## Why this repository exists

Modern AI systems **will be attacked**.

Understanding how to:
- design them securely,
- validate security controls,
- detect abuse,
- audit behavior,
- and evolve architectures safely,

is becoming a **core security skill**.

This repository documents that journey.
