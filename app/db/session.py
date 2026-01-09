from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
print("🔥 FASTAPI CONNECTED TO DB:", engine.url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ THIS FUNCTION WAS MISSING OR WRONG
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
