from sqlalchemy.orm import Session
from app.models.report import MedicalReport
from app.models.analysis import AnalysisResult
from app.ocr.pdf_reader import read_pdf
from app.ocr.image_reader import read_image
from app.ocr.clean_text import clean_medical_text
from app.agents.medical_agent import analyze_report
from app.agents.explain_agent import explain_report
from app.agents.translate_agent import translate_text
from app.agents.voice_agent import text_to_voice

def process_report(
    report_id: int,
    file_path: str,
    language: str,
    mode: str,
    db: Session
):
    report = db.query(MedicalReport).get(report_id)

    try:
        report.status = "processing"
        db.commit()

        if file_path.endswith(".pdf"):
            raw_text = read_pdf(file_path)
        else:
            raw_text = read_image(file_path)

        cleaned_text = clean_medical_text(raw_text)

        analysis_data = analyze_report(cleaned_text)
        explanation = explain_report(
            analysis_data["analysis"],
            mode
        )
        translated = translate_text(explanation, language)
        audio_path = text_to_voice(translated)

        analysis = AnalysisResult(
            report_id=report.id,
            medical_analysis=analysis_data["analysis"],
            confidence_score=analysis_data["confidence"],
            disclaimer=analysis_data["disclaimer"],
            simplified_explanation=explanation,
            translated_text=translated,
            audio_file=audio_path
        )

        report.status = "completed"
        db.add(analysis)
        db.commit()

    except Exception:
        report.status = "failed"
        db.commit()




for attempt in range(3):
    try:
        # OCR + AI logic
        break
    except Exception:
        if attempt == 2:
            raise
