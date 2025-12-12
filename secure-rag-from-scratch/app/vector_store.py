from __future__ import annotations

import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple


_TOKEN_PATTERN = re.compile(r"\b\w+\b")


def _tokenize(text: str) -> Counter:
    tokens = _TOKEN_PATTERN.findall(text.lower())
    return Counter(tokens)


def _cosine_similarity(a: Counter, b: Counter) -> float:
    """Compute cosine similarity between two sparse vectors."""

    dot_product = sum(a[token] * b[token] for token in a.keys() & b.keys())
    if dot_product == 0:
        return 0.0

    a_norm = math.sqrt(sum(v * v for v in a.values()))
    b_norm = math.sqrt(sum(v * v for v in b.values()))
    if a_norm == 0 or b_norm == 0:
        return 0.0
    return dot_product / (a_norm * b_norm)


@dataclass
class StoredDocument:
    path: str
    content: str
    vector: Counter

    def to_json(self) -> dict:
        return {"path": self.path, "content": self.content, "vector": dict(self.vector)}

    @classmethod
    def from_json(cls, payload: dict) -> "StoredDocument":
        return cls(path=payload["path"], content=payload["content"], vector=Counter(payload["vector"]))


class VectorStore:
    """Minimal vector store backed by a JSON file."""

    def __init__(self, index_path: Path) -> None:
        self.index_path = index_path
        self.documents: List[StoredDocument] = []
        if index_path.exists():
            self._load()

    def _load(self) -> None:
        with self.index_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        self.documents = [StoredDocument.from_json(doc) for doc in payload.get("documents", [])]

    def _persist(self) -> None:
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        with self.index_path.open("w", encoding="utf-8") as handle:
            json.dump({"documents": [doc.to_json() for doc in self.documents]}, handle, ensure_ascii=False, indent=2)

    def add_document(self, path: str, content: str) -> None:
        vector = _tokenize(content)
        self.documents.append(StoredDocument(path=path, content=content, vector=vector))
        self._persist()

    def add_many(self, items: Iterable[Tuple[str, str]]) -> None:
        for path, content in items:
            self.add_document(path, content)

    def search(self, query: str, top_k: int = 3) -> List[StoredDocument]:
        query_vector = _tokenize(query)
        scored: List[Tuple[float, StoredDocument]] = []
        for doc in self.documents:
            score = _cosine_similarity(doc.vector, query_vector)
            if score > 0:
                scored.append((score, doc))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [doc for _, doc in scored[:top_k]]


__all__ = ["VectorStore", "StoredDocument"]
