"""FastAPI application exposing portfolio endpoints."""

from fastapi import FastAPI

app = FastAPI(title="Dividend Portfolio Tracker")


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Simple health check endpoint."""
    return {"status": "ok"}
