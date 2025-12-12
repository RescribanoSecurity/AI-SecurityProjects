# Secure RAG from Scratch

A minimal retrieval augmented generation (RAG) starter that keeps dependencies light and encourages secure defaults.

## Project layout
- `app/`: FastAPI app plus RAG primitives.
- `scripts/ingest.py`: CLI helper to ingest `.txt` files from `data/raw` into the JSON-backed index.
- `data/raw/`: Place text files here before running ingestion.
- `infra/requirements.txt`: Python dependencies for the app.
- `.env.example`: Environment variable template for local runs.

## Getting started
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r infra/requirements.txt
   ```
2. Copy `.env.example` to `.env` and set values as needed.
3. Ingest documents:
   ```bash
   python scripts/ingest.py
   ```
4. Run the API locally:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
5. Query the service:
   ```bash
   curl -X POST http://localhost:8000/query -H "Content-Type: application/json" \\
     -d '{"question": "What does this project demonstrate?"}'
   ```
