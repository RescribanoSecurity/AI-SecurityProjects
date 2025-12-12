# Laboratorio de Seguridad en IA (LLMs · RAG Seguro · Cloud · MLOps)

📄 Este README está disponible en:
- 🇬🇧 English → [README.md](README.md)
- 🇪🇸 Español (este documento)

---

## Visión general

Este repositorio es mi **laboratorio personal de aprendizaje en seguridad de Inteligencia Artificial**, con el objetivo de evolucionar desde **Cloud Security** hacia perfiles de **AI / LLM Security** o **AI Cloud Security Architect**.

El enfoque es **construir sistemas reales desde cero**, documentando decisiones técnicas, errores reales y controles de seguridad aplicables a entornos empresariales.

No es un repositorio de tutoriales.  
Es un **ejercicio de ingeniería y seguridad aplicada**.

---

## Objetivos de aprendizaje

- Comprender cómo funcionan los **LLMs** (contexto, prompts, generación, limitaciones).
- Diseñar y construir **RAGs seguros (Retrieval-Augmented Generation)**.
- Aplicar controles reales de seguridad inspirados en **OWASP LLM Top 10**:
  - Prompt Injection y Jailbreaks
  - Fugas de información y PII
  - Riesgos en ingestión de datos
  - Auditoría y trazabilidad
- Preparar arquitecturas **listas para entornos cloud empresariales**.

---

## Proyectos

### 🔐 Secure RAG from Scratch
📂 `secure-rag-from-scratch/`

Sistema RAG seguro construido de forma incremental:

- **Fase 1 – Baseline local**
  - Vector store en memoria
  - LLM simulado (mock)
  - Seguridad de entrada (prompt injection)

- **Fase 2 – Modo local seguro**
  - Seguridad de salida (detección y redacción de PII)
  - Auditoría estructurada
  - Activación por entorno (`APP_MODE`)

📘 Documentación técnica:
- 🇬🇧 [secure-rag-from-scratch/README.md](secure-rag-from-scratch/README.md)
- 🇪🇸 [secure-rag-from-scratch/README_ES.md](secure-rag-from-scratch/README_ES.md)

---

## Filosofía de diseño

- Evolución por fases claras
- Seguridad como capa transversal
- Separación entre lógica, infraestructura y proveedor
- Diseño local-first pero cloud-ready

---

## Roadmap

- [x] RAG local funcional
- [x] Seguridad de salida y auditoría
- [ ] Abstracción de infraestructura
- [ ] Contenedores y despliegue cloud
- [ ] Integración con servicios vectoriales empresariales
- [ ] Automatización y MLOps

---

## Por qué existe este repositorio

Los sistemas de IA:
- van a fallar,
- van a ser atacados,
- y van a manejar datos sensibles.

Este repositorio documenta cómo **diseñarlos y protegerlos de forma responsable**.

---

## Licencia
MIT
