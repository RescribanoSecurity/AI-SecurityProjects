from __future__ import annotations

from typing import Iterable


class LLMClient:
    """Lightweight text generator placeholder.

    The class is written to keep the dependency surface minimal while still
    allowing callers to swap in a real LLM implementation later on.
    """

    def __init__(self, model_name: str, api_key: str | None = None) -> None:
        self.model_name = model_name
        self.api_key = api_key

    def generate(self, question: str, context: Iterable[str]) -> str:
        """Generate a deterministic response using provided context.

        A production implementation could call an external LLM API. For this
        reference project we keep the response local and reproducible by
        composing the question and retrieved passages.
        """

        context_snippets = "\n- " + "\n- ".join([c.strip() for c in context if c.strip()])
        return (
            f"Model: {self.model_name}\n"
            f"Question: {question.strip()}\n"
            "Context used:" + (context_snippets if context_snippets.strip() else "\n- (none)")
        )
