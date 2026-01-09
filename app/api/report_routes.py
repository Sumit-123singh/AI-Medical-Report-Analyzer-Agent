from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pathlib import Path
import shutil

from app.ocr.pdf_reader import read_pdf
from app.agents.explain_agent import ExplainAgent
from app.agents.translate_agent import TranslateAgent
from app.agents.voice_agent import text_to_voice
from app.utils.response_utils import add_medical_disclaimer


router = APIRouter(prefix="/reports", tags=["Reports"])


# -----------------------------
# Supported demo languages
# -----------------------------
SUPPORTED_LANGUAGES = {"english", "hindi", "marathi", "tamil"}
SUPPORTED_MODES = {"patient", "doctor"}


# -----------------------------
# Agent instances
# -----------------------------
explain_agent = ExplainAgent()
translate_agent = TranslateAgent()


# =========================================================
# ANALYZE REPORT (PDF / IMAGE → TEXT → EXPLAIN → AUDIO)
# =========================================================
@router.post("/analyze")
def analyze_report(
    file: UploadFile = File(...),
    mode: str = Form(...),        # doctor / patient
    language: str = Form(...)     # english / hindi / marathi / tamil
):
    # -----------------------------
    # Validate language
    # -----------------------------
     # Normalize inputs
    mode = mode.lower().strip()
    language = language.lower().strip()

    # Validate mode
    if mode not in SUPPORTED_MODES:
        raise HTTPException(
            status_code=400,
            detail="Mode not supported. Please select one of: patient, doctor."
        )
    language = language.lower().strip()

    if language not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail=(
                "Language not supported. "
                "Please select one of: English, Hindi, Marathi, Tamil."
            )
        )

    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    file_path = upload_dir / file.filename

    # -----------------------------
    # Save uploaded file
    # -----------------------------
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to save uploaded file")

    # -----------------------------
    # OCR (RAW TEXT)
    # -----------------------------
    try:
        raw_text = read_pdf(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not raw_text.strip():
        raise HTTPException(
            status_code=400,
            detail="No readable text found in the uploaded document"
        )

    # -----------------------------
    # Decide LLM language strategy
    # -----------------------------
    # For Marathi & Tamil → generate English, then translate
    llm_language = "english" if language in {"marathi", "tamil"} else language

    # -----------------------------
    # EXPLAIN (LLM)
    # -----------------------------
    explained_text = explain_agent.explain(
        text=raw_text,
        mode=mode,
        language=llm_language
    )

    # -----------------------------
    # TRANSLATE (if needed)
    # -----------------------------
    final_text = translate_agent.translate(
        text=explained_text,
        target_language=language
    )

    # -----------------------------
    # ADD DISCLAIMER
    # -----------------------------
    final_text = add_medical_disclaimer(
        final_text,
        language=language
    )

    # -----------------------------
    # CREATE AUDIO
    # -----------------------------
    audio_path = text_to_voice(
        text=final_text,
        language=language
    )

    audio_url = None
    if audio_path:
        audio_url = f"/audio/{Path(audio_path).name}"

    return {
        "mode": mode,
        "language": language,
        "result": final_text,
        "audio_url": audio_url
    }


# =========================================================
# AUDIO SECTION (LIST ALL AUDIO FILES)
# =========================================================
@router.get("/audio/list")
def list_audio_files():
    audio_dir = Path("audio")

    if not audio_dir.exists():
        return {
            "count": 0,
            "audio_files": []
        }

    audio_files = [
        f"/audio/{file.name}"
        for file in audio_dir.iterdir()
        if file.suffix == ".mp3"
    ]

    return {
        "count": len(audio_files),
        "audio_files": audio_files
    }
