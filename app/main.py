from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.db.init_db import init_db

app = FastAPI(
    title="AI Medical Report Analyzer",
    version="1.0.0"
)

# ✅ Include routers
app.include_router(auth_router)
from app.user.routes import router as user_router

app.include_router(user_router)


# ✅ Startup event (ONLY ONE)
@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/health/db")
def db_health():
    return {"db": "connected"}
