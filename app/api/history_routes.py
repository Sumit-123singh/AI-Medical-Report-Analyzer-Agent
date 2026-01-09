from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.report import MedicalReport
from app.models.analysis import AnalysisResult
from app.models.user import User

router = APIRouter(prefix="/history", tags=["History"])


@router.get("/")
def get_user_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    reports = (
        db.query(MedicalReport)
        .filter(MedicalReport.user_id == current_user.id)
        .order_by(MedicalReport.uploaded_at.desc())
        .all()
    )

    history = []

    for report in reports:
        analysis = (
            db.query(AnalysisResult)
            .filter(AnalysisResult.report_id == report.id)
            .first()
        )

        history.append({
            "report_id": report.id,
            "filename": report.file_name,
            "analysis": analysis.medical_analysis if analysis else None,
            "uploaded_at": report.uploaded_at
        })

    return history
