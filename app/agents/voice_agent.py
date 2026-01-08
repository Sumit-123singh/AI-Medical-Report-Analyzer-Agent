from gtts import gTTS
from gtts.tts import gTTSError
import os
import uuid
import re

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

LANGUAGE_MAP = {
    "english": "en",
    "hindi": "hi",
    "hinglish": "hi",
    "marathi": "mr",
    "tamil": "ta",
    "bhojpuri": "hi"
}

MAX_TTS_CHARS = 1200  # 🔥 SAFE LIMIT


def _clean_for_tts(text: str) -> str:
    text = re.sub(r"\*\*|\*|_|`|#", "", text)
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"[^\w\s\u0900-\u097F\u0B80-\u0BFF]", "", text)
    return text.strip()


def text_to_voice(text: str, language: str = "english") -> str:
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(AUDIO_DIR, filename)

    tts_lang = LANGUAGE_MAP.get(language.lower(), "en")

    clean_text = _clean_for_tts(text)

    # 🔥 CRITICAL: limit length
    clean_text = clean_text[:MAX_TTS_CHARS]

    if not clean_text:
        print("⚠️ TTS skipped: empty text")
        return ""

    try:
        tts = gTTS(text=clean_text, lang=tts_lang)
        tts.save(file_path)
        print(f"✅ Audio created at: {file_path}")
        return file_path

    except gTTSError as e:
        print("❌ gTTS failed:", e)
        return ""
