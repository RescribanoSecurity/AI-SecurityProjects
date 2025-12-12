from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

from .config import Settings
from .llm_client import LLMClient
from .vector_store import StoredDocument, VectorStore


class RAGPipeline:
    """Simple retrieval augmented generation pipeline."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.vector_store = VectorStore(settings.index_path)
        self.client = LLMClient(settings.model_name, api_key=settings.openai_api_key)

    def ingest_directory(self, directory: Path) -> int:
        """Ingest all text files under ``directory``.

        Returns the number of documents added.
        """

        documents = []
        for path in directory.rglob("*.txt"):
            content = path.read_text(encoding="utf-8")
            documents.append((str(path), content))
        self.vector_store.add_many(documents)
        return len(documents)

    def search(self, query: str) -> List[StoredDocument]:
        return self.vector_store.search(query, top_k=self.settings.top_k)

    def answer(self, question: str) -> str:
        """Return an answer based on retrieved context."""

        results = self.search(question)
        context = [doc.content for doc in results]
        return self.client.generate(question, context)


__all__ = ["RAGPipeline"]
