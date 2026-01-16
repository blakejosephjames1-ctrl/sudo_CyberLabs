from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import get_db, engine
from app.db.base import Base
from app.db import models # noqa: F401

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Cybersecurity Training Platform", lifespan=lifespan)

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "database": settings.DATABASE_URL,
    }

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    return {"message": "Database connection successful"}

