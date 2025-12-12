from __future__ import annotations


def call_llm(prompt: str) -> str:
    """
    Local mock LLM for development and security testing.
    This avoids external dependencies and quota issues.
    """
    return (
        "Para más información escribe a rescribano@correjemplo.comp"
	"o llama al teléfono +34 600 123 456"
    )

