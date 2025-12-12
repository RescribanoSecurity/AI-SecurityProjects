# Secure RAG from Scratch (Documentación Técnica)

📄 Esta documentación está disponible en:
- 🇬🇧 English → README.md
- 🇪🇸 Español (este documento)

---

## Propósito del proyecto

Este proyecto implementa un **sistema RAG (Retrieval-Augmented Generation) seguro** desde cero, con el objetivo de:

- Entender cómo funciona un RAG extremo a extremo
- Aplicar controles de seguridad reales a sistemas con LLM
- Separar seguridad, infraestructura y proveedor
- Evolucionar de local a cloud de forma ordenada

---

## Arquitectura general

Cliente → FastAPI → Seguridad de entrada → Pipeline RAG → Seguridad de salida → Auditoría → Respuesta

---

## Modos de ejecución (APP_MODE)

local_basic  – RAG básico con seguridad de entrada  
local_secure – Añade seguridad de salida (PII) y auditoría

---

## Estructura del proyecto

- app/main.py – Punto de entrada FastAPI
- app/security.py – Detección de prompt injection
- app/rag.py – Pipeline RAG
- app/vector_store.py – Vector store en memoria
- app/llm_client.py – LLM simulado
- app/security_output.py – Detección y redacción de PII
- app/audit.py – Auditoría estructurada

---

## Controles de seguridad

- Detección de prompt injection
- Redacción de PII
- Logs de auditoría

---

## Pruebas

Pruebas manuales:
- Bloqueo de prompt injection
- Redacción de datos sensibles
- Registro de eventos de seguridad

---

## Lecciones aprendidas

- Dependencias externas rompen el desarrollo
- El diseño local-first acelera pruebas
- La seguridad no debe depender del proveedor LLM

---

## Evolución futura

- Vector store cloud
- Contenedores
- CI/CD y controles de seguridad
