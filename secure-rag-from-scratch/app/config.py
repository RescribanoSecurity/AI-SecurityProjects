from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    """Application configuration derived from environment variables."""

    data_dir: Path = Path(os.getenv("DATA_DIR", "data"))
    index_path: Path = Path(os.getenv("INDEX_PATH", "data/index.json"))
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    top_k: int = int(os.getenv("TOP_K", "3"))
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")


def get_settings() -> Settings:
    """Return populated :class:`Settings` for the application."""

    return Settings()
