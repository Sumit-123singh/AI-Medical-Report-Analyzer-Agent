from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import os
import traceback

from app.db.session import get_db
from app.core.deps import get_current_user
from app.models.report import MedicalReport
from app.models.analysis import AnalysisResult   # ✅ STEP 1: IMPORT
from app.models.user import User

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.post("/upload")
def upload_report(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        print("🔥 /reports/upload HIT")
        print("🔥 Current user ID:", current_user.id)
        print("🔥 Filename:", file.filename)

        # Ensure uploads directory exists
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"

        # 1️⃣ Save file to disk
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        print("✅ File saved at:", file_path)

        # 2️⃣ Save medical report
        report = MedicalReport(
            user_id=current_user.id,
            file_name=file.filename,
            file_path=file_path,
            status="uploaded"
        )

        db.add(report)
        db.commit()
        db.refresh(report)  # report.id available

        print("✅ Report saved in DB with ID:", report.id)

        # 3️⃣ SAVE ANALYSIS RESULT (THIS WAS MISSING)
        analysis = AnalysisResult(
            report_id=report.id,
            summary="Sample medical summary",
            explanation="This is a demo explanation until AI is connected.",
            risk_level="Low",
            language="en"
        )

        db.add(analysis)
        db.commit()

        print("✅ Analysis saved for report ID:", report.id)

        return {
            "message": "Report uploaded and analyzed successfully",
            "report_id": report.id,
            "analysis_saved": True
        }

    except Exception as e:
        print("❌ ERROR during upload")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


# ✅ DB FORCE TEST (KEEP THIS FOR DEBUGGING)
@router.post("/absolute-db-test")
def absolute_db_test(db: Session = Depends(get_db)):
    report = MedicalReport(
        user_id=1,
        file_name="absolute.pdf",
        file_path="uploads/absolute.pdf",
        status="uploaded"
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    analysis = AnalysisResult(
        report_id=report.id,
        summary="Absolute test summary",
        explanation="Absolute test explanation",
        risk_level="Low",
        language="en"
    )

    db.add(analysis)
    db.commit()

    print("🔥 ABSOLUTE TEST INSERT ID:", report.id)

    return {"id": report.id}
