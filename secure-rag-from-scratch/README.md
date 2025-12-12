# Secure RAG from Scratch – Technical Documentation

## High-level Architecture

Client → FastAPI → Input Security → RAG Pipeline → Output Security → Audit → Response

```mermaid
flowchart LR
    User["User / Client"]
    API["FastAPI API"]
    InputSec["Input Security (Prompt Injection Detection)"]
    RAG["RAG Pipeline"]
    VS["Vector Store (In-Memory)"]
    LLM["LLM Client (Mock or Provider)"]
    OutputSec["Output Security (PII Detection and Redaction)"]
    Audit["Audit Logging"]
    Response["HTTP Response"]

    User --> API
    API --> InputSec
    InputSec --> RAG
    RAG --> VS
    RAG --> LLM
    LLM --> OutputSec
    OutputSec --> Audit
    Audit --> Response
    Response --> User
```

---

## Execution Modes (APP_MODE)

The system supports progressive security hardening using execution modes.

```mermaid
flowchart TB
    subgraph LocalBasic["APP_MODE = local_basic"]
        LB1["Input Security"]
        LB2["RAG Pipeline"]
        LB3["LLM Response"]
    end

    subgraph LocalSecure["APP_MODE = local_secure"]
        LS1["Input Security"]
        LS2["RAG Pipeline"]
        LS3["Output Security (PII Redaction)"]
        LS4["Audit Logging"]
    end

    LB1 --> LB2 --> LB3
    LS1 --> LS2 --> LS3 --> LS4
```

---

## Security Flow (Detailed)

```mermaid
sequenceDiagram
    participant User
    participant API as FastAPI
    participant InputSec as Input Security
    participant RAG
    participant LLM
    participant OutputSec as Output Security
    participant Audit

    User->>API: POST /query
    API->>InputSec: Validate query

    alt Malicious input detected
        InputSec-->>API: Block request
        API->>Audit: Log blocked_input
        API-->>User: HTTP 400
    else Valid input
        InputSec->>RAG: Forward query
        RAG->>LLM: Generate response
        LLM-->>RAG: Raw answer
        RAG->>OutputSec: Check PII (local_secure)
        alt PII detected
            OutputSec->>Audit: Log pii_detected
            OutputSec-->>API: Redacted answer
        else No PII detected
            OutputSec-->>API: Clean answer
        end
        API-->>User: HTTP 200
    end
```

---

## Notes

- Security controls are external to the LLM.
- Mermaid blocks are isolated and closed correctly.
- This README can be uploaded directly to GitHub without editing.
