from app.services.translation_service import translate_text


class TranslateAgent:
    """
    Handles language translation for medical reports.
    """

    # Supported language mapping
    LANGUAGE_MAP = {
        "english": "en",
        "en": "en",

        "hindi": "hi",
        "hi": "hi",

        "marathi": "mr",
        "mr": "mr",

        "tamil": "ta",
        "ta": "ta",

        # Bhojpuri is NOT officially supported → fallback to Hindi
        "bhojpuri": "hi"
    }

    def translate(self, text: str, target_language: str) -> str:
        """
        Translate text into selected language.
        Supported: English, Hindi, Marathi, Tamil, Bhojpuri
        """

        if not text.strip():
            return text  # nothing to translate

        # Normalize language
        lang_key = target_language.lower().strip()
        lang_code = self.LANGUAGE_MAP.get(lang_key, "en")

        try:
            translated_text = translate_text(
                text=text,
                target_language=lang_code
            )
            return translated_text
        except Exception as e:
            # Fail-safe: return original text
            print(f"[Translation Error] {e}")
            return text
