from __future__ import annotations


def call_llm(prompt: str) -> str:
    """
    Local mock LLM for development and security testing.
    This avoids external dependencies and quota issues.
    """
    return (
        "For more information email rescribano@correjemplo.comp "
        "or call +34 600 123 456."
    )
