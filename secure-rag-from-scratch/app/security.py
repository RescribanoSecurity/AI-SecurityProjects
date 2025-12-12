from __future__ import annotations

import re
from typing import Tuple


# Patrones comunes de prompt injection
SUSPICIOUS_PATTERNS = [
    r"ignore (all|previous) instructions",
    r"disregard the above",
    r"act as .*",
    r"reveal .*prompt",
    r"show .*system prompt",
    r"you are now .*",
    r"bypass .*security",
    r"print .*password",
    r"print .*token",
]


def normalize_query(query: str) -> str:
    """Normaliza la query para evitar trucos básicos."""
    return query.strip().lower()


def detect_prompt_injection(query: str) -> Tuple[bool, str]:
    """
    Detecta intentos básicos de prompt injection.
    Devuelve (is_malicious, reason)
    """
    normalized = normalize_query(query)

    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, normalized):
            return True, f"Matched suspicious pattern: {pattern}"

    return False, "OK"

