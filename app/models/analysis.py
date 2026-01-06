from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime,String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)

    report_id = Column(Integer, ForeignKey("medical_reports.id"), nullable=False)

    summary = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    risk_level = Column(String(50), nullable=True)
    language = Column(String(50), default="en")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    report = relationship("MedicalReport", back_populates="analysis")
