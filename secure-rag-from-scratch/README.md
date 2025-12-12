# Secure RAG from Scratch (Technical Documentation)

📄 This documentation is available in:
- 🇬🇧 English (this document)
- 🇪🇸 Español → README_ES.md

---

## Purpose of this project

This project implements a **secure Retrieval-Augmented Generation (RAG) system** from scratch, designed to:

- Understand how RAG pipelines work end to end
- Apply real security controls to LLM-based systems
- Separate security logic from infrastructure and providers
- Evolve cleanly from local development to cloud environments

The focus is on architecture, security decisions, and explainability.

---
```mermaid
flowchart LR
    A --> B
---

## Execution modes (APP_MODE)

local_basic  – Baseline RAG with input security  
local_secure – Adds output security (PII) and audit logging

---

## Project Structure

- app/main.py – FastAPI entry point and orchestration
- app/security.py – Prompt injection detection
- app/rag.py – Core RAG pipeline
- app/vector_store.py – In-memory vector store
- app/llm_client.py – Mock LLM client
- app/security_output.py – PII detection and redaction
- app/audit.py – Structured audit logging

---

## Security Controls

- Prompt injection detection
- PII detection and redaction
- Structured audit logging

---

## Testing

Manual tests cover:
- Prompt injection blocking
- PII redaction
- Audit log generation

---

## Lessons Learned

- External dependencies can block development
- Local-first design accelerates security testing
- Security must be independent of LLM providers

---

## Future Work

- Cloud vector stores
- Dockerized deployment
- CI/CD and security testing
