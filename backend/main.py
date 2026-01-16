from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.core.database import get_db

app = FastAPI(title="Cybersecurity Training Platform")

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "database": settings.DATABASE_URL,
    }

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    return {"message": "Database connection successful"}

