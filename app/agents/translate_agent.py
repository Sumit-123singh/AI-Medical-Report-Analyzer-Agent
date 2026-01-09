from app.services.translation_service import translate_text


class TranslateAgent:
    """
    Handles language translation for medical reports.

    Demo-supported languages:
    - English
    - Hindi
    - Marathi
    - Tamil

    NOTE:
    - Hinglish is handled via LLM (not translated here)
    - Bhojpuri is intentionally removed from demo support
    """

    # Supported language mapping (REAL TRANSLATION ONLY)
    LANGUAGE_MAP = {
        "english": "en",
        "en": "en",

        "hindi": "hi",
        "hi": "hi",

        "marathi": "mr",
        "mr": "mr",

        "tamil": "ta",
        "ta": "ta",
    }

    # Languages handled directly by LLM (no translation)
    LLM_LANGUAGES = {"hinglish"}

    def translate(self, text: str, target_language: str) -> str:
        """
        Translate text into selected language.
        Hinglish is returned as-is.
        """

        if not text or not text.strip():
            return text

        lang_key = target_language.lower().strip()

        # 🚀 LLM-handled languages → DO NOT TRANSLATE
        if lang_key in self.LLM_LANGUAGES:
            return text

        lang_code = self.LANGUAGE_MAP.get(lang_key, "en")

        try:
            return translate_text(
                text=text,
                target_language=lang_code
            )
        except Exception as e:
            print(f"[Translation Error] {e}")
            return text
