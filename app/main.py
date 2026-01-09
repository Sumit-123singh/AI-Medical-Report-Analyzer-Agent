import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.db.init_db import init_db

# Routers
from app.auth.routes import router as auth_router
from app.api.report_routes import router as report_router
from app.api.history_routes import router as history_router
from app.user.routes import router as user_router


# -----------------------------
# Create required directories
# -----------------------------
os.makedirs("uploads", exist_ok=True)
os.makedirs("audio", exist_ok=True)


# -----------------------------
# Create FastAPI app (ONLY ONCE)
# -----------------------------
app = FastAPI(
    title="AI Medical Report Analyzer",
    version="1.0.0"
)


# -----------------------------
# Include Routers
# -----------------------------
app.include_router(auth_router)
app.include_router(report_router)
app.include_router(history_router)
app.include_router(user_router)


# -----------------------------
# Static Files (IMPORTANT)
# -----------------------------
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/audio", StaticFiles(directory="audio"), name="audio")


# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
def startup_event():
    init_db()


# -----------------------------
# Root & Health APIs
# -----------------------------
@app.get("/")
def root():
    return {"status": "API running successfully"}


@app.get("/health/db")
def db_health():
    return {"db": "connected"}
