from __future__ import annotations

from app.config import TOP_K
from app.vector_store import search_docs
from app.llm_client import call_llm


def build_prompt(query: str, contexts: list[str]) -> str:
    context_block = "\n\n---\n\n".join(contexts) if contexts else ""

    return f"""
Eres un asistente que responde SOLO usando el contexto proporcionado.
Si la respuesta no está en el contexto, responde exactamente:
"No dispongo de datos suficientes para responder."

[CONTEXTO]
{context_block}

[PREGUNTA]
{query}
""".strip()


def rag_pipeline(query: str) -> str:
    contexts = search_docs(query, k=TOP_K)
    prompt = build_prompt(query, contexts)
    return call_llm(prompt)

