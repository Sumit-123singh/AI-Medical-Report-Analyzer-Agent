import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi import FastAPI

app = FastAPI(title="AI Medical Report Analyzer")


@app.on_event("startup")
def on_startup():
    from app.db.base import Base
    from app.db.session import engine
    

    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/health/db")
def db_health():
    return {"db": "models loaded successfully"}

@app.on_event("startup")
def on_startup():
    from app.db.init_db import init_db
    init_db()


