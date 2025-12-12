from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .config import get_settings
from .rag import RAGPipeline

app = FastAPI(title="Secure RAG from Scratch")
settings = get_settings()
pipeline = RAGPipeline(settings)


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest) -> QueryResponse:
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question must not be empty")

    answer = pipeline.answer(question)
    return QueryResponse(answer=answer)
