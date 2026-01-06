from app.db.base import Base
from app.db.session import engine

# 👇 VERY IMPORTANT: import all models
from app.models.user import User
from app.models.report import MedicalReport
from app.models.analysis import AnalysisResult


def init_db():
    Base.metadata.create_all(bind=engine)
