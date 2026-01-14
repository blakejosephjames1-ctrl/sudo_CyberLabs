from fastapi import FastAPI
from .app.core.config import settings

app = FastAPI(title="Cybersecurity Training Platform")

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "database": settings.DATABASE_URL,
    }
