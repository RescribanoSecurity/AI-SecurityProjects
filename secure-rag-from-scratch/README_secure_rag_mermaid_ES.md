# Secure RAG from Scratch – Documentación Técnica

## Arquitectura de Alto Nivel

Cliente → FastAPI → Seguridad de Entrada → Pipeline RAG → Seguridad de Salida → Auditoría → Respuesta

```mermaid
flowchart LR
    Usuario["Usuario / Cliente"]
    API["FastAPI API"]
    SecEntrada["Seguridad de Entrada (Detección de Prompt Injection)"]
    RAG["Pipeline RAG"]
    VS["Vector Store (En Memoria)"]
    LLM["Cliente LLM (Mock o Proveedor)"]
    SecSalida["Seguridad de Salida (Detección y Redacción de PII)"]
    Auditoria["Auditoría"]
    Respuesta["Respuesta HTTP"]

    Usuario --> API
    API --> SecEntrada
    SecEntrada --> RAG
    RAG --> VS
    RAG --> LLM
    LLM --> SecSalida
    SecSalida --> Auditoria
    Auditoria --> Respuesta
    Respuesta --> Usuario
```

---

## Modos de Ejecución (APP_MODE)

El sistema permite un **endurecimiento progresivo de la seguridad** mediante modos de ejecución.

```mermaid
flowchart TB
    subgraph LocalBasico["APP_MODE = local_basic"]
        LB1["Seguridad de Entrada"]
        LB2["Pipeline RAG"]
        LB3["Respuesta del LLM"]
    end

    subgraph LocalSeguro["APP_MODE = local_secure"]
        LS1["Seguridad de Entrada"]
        LS2["Pipeline RAG"]
        LS3["Seguridad de Salida (Redacción de PII)"]
        LS4["Auditoría"]
    end

    LB1 --> LB2 --> LB3
    LS1 --> LS2 --> LS3 --> LS4
```

---

## Flujo de Seguridad (Detallado)

```mermaid
sequenceDiagram
    participant Usuario
    participant API as FastAPI
    participant SecEntrada as Seguridad de Entrada
    participant RAG
    participant LLM
    participant SecSalida as Seguridad de Salida
    participant Auditoria

    Usuario->>API: POST /query
    API->>SecEntrada: Validar consulta

    alt Entrada maliciosa detectada
        SecEntrada-->>API: Bloquear petición
        API->>Auditoria: Log blocked_input
        API-->>Usuario: HTTP 400
    else Entrada válida
        SecEntrada->>RAG: Enviar consulta
        RAG->>LLM: Generar respuesta
        LLM-->>RAG: Respuesta sin procesar
        RAG->>SecSalida: Comprobar PII (local_secure)
        alt PII detectada
            SecSalida->>Auditoria: Log pii_detected
            SecSalida-->>API: Respuesta redactada
        else Sin PII
            SecSalida-->>API: Respuesta limpia
        end
        API-->>Usuario: HTTP 200
    end
```

---

## Notas

- Los controles de seguridad están **fuera del LLM**.
- La auditoría forma parte del diseño, no es opcional.
- Este README puede subirse directamente a GitHub sin modificaciones.
