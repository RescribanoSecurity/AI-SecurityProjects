# AI Security Learning Lab  
*(LLMs · Secure RAG · Cloud · MLOps)*

Este README está disponible en:
- 🇬🇧 EN English → [README.md](README.md)
- 🇪🇸 ES Español (este documento)

---

## Visión General

Este repositorio es mi **laboratorio personal de aprendizaje en Seguridad de IA** y **repositorio índice**, que documenta mi evolución desde **Cloud Security** hacia **AI / LLM Security**, con el objetivo a largo plazo de un perfil de **AI Cloud Security Architect**.

El enfoque es **construir sistemas de IA reales desde cero**, hacer explícitas las **decisiones arquitectónicas y de seguridad**, validarlas mediante pruebas prácticas y documentar tanto **los resultados como los errores**.

Este **no es un repositorio de tutoriales**.  
Es una exploración **ingenieril y security-first** de sistemas modernos basados en LLMs.

---

## Objetivos de Aprendizaje

- Comprender cómo funcionan internamente los **LLMs** (contexto, prompts, generación).
- Diseñar y construir **pipelines RAG (Retrieval-Augmented Generation) seguros**.
- Aplicar **controles prácticos de seguridad en IA**, inspirados en **OWASP LLM Top 10**:
  - Prompt injection y jailbreaks
  - Fugas de datos y exposición de PII
  - Riesgos en la ingesta y data poisoning
  - Prevención de abuso y auditabilidad
- Preparar sistemas para **entornos tipo enterprise**:
  - Configuración multi-entorno
  - Observabilidad y logging estructurado
  - Arquitectura preparada para cloud
  - Fundamentos de MLOps

---

## Proyectos

### 🔬 Secure RAG from Scratch — Versión 1 (Laboratorio Legacy)
📁 `secure-rag-from-scratch/`

Este proyecto representa la **primera iteración exploratoria** de Secure RAG.

Su objetivo fue:
- Entender los mecanismos básicos de los sistemas RAG
- Experimentar con **controles iniciales de seguridad de entrada**
- Validar supuestos antes de introducir mayor complejidad de infraestructura

**Características principales de V1:**
- Ejecución local
- Vector store en memoria
- LLM simulado (independiente del proveedor)
- Detección básica de prompt injection
- Pruebas manuales y documentación

⚠️ **Esta versión se considera actualmente un laboratorio legacy.**

👉 La versión activa y evolucionada es **Secure RAG v2**, mantenida en un repositorio independiente.

---

### 🚀 Secure RAG from Scratch — Versión 2 (Proyecto Principal)

🔗 Repositorio:  
https://github.com/RescribanoSecurity/secure-rag-from-scratch-v2

Secure RAG v2 es el **proyecto principal y más maduro**, evolucionado directamente a partir de las lecciones aprendidas en V1.

**Áreas clave:**
- Arquitectura modular de pipeline RAG
- Controles de seguridad de entrada **y salida**
- Detección, redacción y bloqueo de PII
- Mapeo con OWASP LLM Top 10
- Infraestructura dockerizada
- Base de datos vectorial real (Qdrant)
- Trazabilidad y auditoría de peticiones
- Validación visual mediante interfaz Streamlit

Este proyecto es:
- Ejecutable
- Testeable
- Basado en evidencia
- Transparente sobre lo que está implementado y lo que no

📄 La documentación técnica completa, capturas y presentaciones se mantienen **dentro del repositorio de la V2**.

---

## Filosofía de Diseño

- **Evolución por fases**: cada fase es estable, revisable y extensible.
- **La seguridad como pilar central**, no como añadido.
- **Arquitectura desacoplada**: los controles de seguridad no dependen del proveedor de LLM ni del vector store.
- **Local-first, cloud-ready**: reducir complejidad inicial sin cerrar puertas al escalado.
- **Los fallos se documentan**, no se ocultan.

---

## Roadmap (Alto Nivel)

- [x] Baseline Secure RAG local (V1)
- [x] Controles de seguridad de entrada
- [x] Seguridad de salida (detección, redacción y bloqueo de PII)
- [x] Validación manual con evidencia documentada
- [ ] Vector stores cloud-native (OpenSearch / Azure AI Search)
- [ ] Autenticación y logging con identidad
- [ ] Logs de auditoría persistentes
- [ ] CI/CD y testing automático de seguridad
- [ ] Threat modeling y enforcement completo de OWASP LLM Top 10

---

## Por qué existe este repositorio

Los sistemas de IA modernos **van a ser atacados**.

Saber:
- diseñarlos de forma segura,
- validar controles de seguridad,
- detectar abusos,
- auditar comportamientos,
- y evolucionar arquitecturas con criterio,

se está convirtiendo en una **competencia clave en seguridad**.

Este repositorio documenta ese camino.
