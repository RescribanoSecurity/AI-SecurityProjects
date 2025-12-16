# AI Security Learning Lab (LLMs · Secure RAG · Cloud · MLOps)

 Este README está disponible en:
- EN English → [README.md](README.md)
- 🇪🇸 Español (este documento)

---

## Visión General

Este repositorio es mi **laboratorio personal de aprendizaje en seguridad de IA**, enfocado en evolucionar desde **Cloud Security** hacia **Seguridad en IA / LLM**, con el objetivo a largo plazo de un perfil de **AI Cloud Security Architect**.

El objetivo es **construir sistemas reales de IA desde cero**, hacer explícitas las decisiones arquitectónicas y de seguridad, validarlas mediante pruebas prácticas y documentar tanto los resultados como las lecciones aprendidas.

Este **no es un repositorio de tutoriales**.  
Es una exploración **orientada a la ingeniería y a la seguridad** de sistemas modernos basados en LLM.

---

## Objetivos de Aprendizaje

- Comprender cómo funcionan internamente los **LLM** (gestión de contexto, prompts, límites de generación).
- Diseñar y construir pipelines **RAG (Retrieval-Augmented Generation) seguros**.
- Aplicar **controles de seguridad prácticos**, inspirados en el OWASP LLM Top 10:
  - Prompt injection y jailbreaks
  - Fugas de datos y exposición de PII
  - Riesgos en la ingesta y data poisoning
  - Prevención de abuso y auditoría
- Preparar sistemas para **entornos similares a los empresariales**:
  - Configuración multi-entorno
  - Observabilidad y logging estructurado
  - Arquitectura preparada para cloud
  - Fundamentos de MLOps

---

## Proyectos

###  Secure RAG from Scratch
 `secure-rag-from-scratch/`

Un sistema RAG **diseñado con la seguridad como eje central**, construido de forma incremental y validado mediante ejecución y pruebas reales.

**Alcance actual:**

- **Baseline local**
  - Vector store en memoria
  - LLM simulado (independiente del proveedor)
  - Seguridad de entrada (detección de prompt injection)

- **Modo local seguro**
  - Seguridad de salida (detección y redacción de PII)
  - Auditoría estructurada
  - Modos de ejecución basados en entorno (`APP_MODE`)
  - Validación manual con evidencias documentadas

Cada fase es **ejecutable, comprobable y documentada**, incluyendo decisiones de diseño y lecciones aprendidas.

 Documentación técnica completa:
- 🇬🇧 [secure-rag-from-scratch/README.md](secure-rag-from-scratch/README.md)
- EN [secure-rag-from-scratch/README_ES.md](secure-rag-from-scratch/README_ES.md)

---

## Filosofía de Diseño

- **Incremental por fases**: cada fase es estable, revisable y extensible.
- **La seguridad como elemento de primer nivel**, no como añadido posterior.
- **Arquitectura desacoplada**: los controles de seguridad no dependen del proveedor de LLM ni del vector store.
- **Local-first, cloud-ready**: reducir complejidad inicial sin perder visión de escalado futuro.

---

## Roadmap

- [x] Baseline local de Secure RAG
- [x] Seguridad de salida y auditoría
- [x] Validación manual y evidencias documentadas
- [ ] Abstracción del vector store (local vs cloud)
- [ ] Docker y despliegue en contenedores
- [ ] Vector stores cloud-native (OpenSearch / Azure AI Search)
- [ ] CI/CD y pruebas de seguridad automatizadas
- [ ] Threat modeling y mapeo OWASP LLM Top 10

---

## Por qué existe este repositorio

Los sistemas modernos de IA **van a ser atacados**.

Comprender cómo:
- diseñarlos de forma segura,
- validar controles de seguridad,
- detectar abusos,
- auditar comportamientos,
- y evolucionar arquitecturas de forma segura,

se está convirtiendo en una **competencia clave** para perfiles de seguridad y cloud.

Este repositorio documenta ese camino.

---

## Licencia

MIT
