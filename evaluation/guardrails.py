"""
Guardrails utilities for SOC LLM governance demo.

- redact(): removes common PII/secrets patterns from text before sending to LLMs
- (Optional extensions can add injection/unsafe classification, but Streamlit app uses Llama Guard 3 for that decision.)
"""

import re

PII_PATTERNS = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone": re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
}

SECRET_PATTERNS = {
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "generic_api_key": re.compile(r"\b(sk_(live|test)_[A-Za-z0-9]{10,})\b"),
    "token_like": re.compile(r"(?i)\b(token|apikey|api_key|secret|password)\s*=\s*([^\s'\";]{6,})"),
}

def redact(text: str) -> str:
    out = text or ""
    for name, rx in PII_PATTERNS.items():
        out = rx.sub(f"[REDACTED_{name.upper()}]", out)
    for name, rx in SECRET_PATTERNS.items():
        out = rx.sub(f"[REDACTED_{name.upper()}]", out)
    return out
