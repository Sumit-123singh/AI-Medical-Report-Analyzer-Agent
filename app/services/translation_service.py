from deep_translator import GoogleTranslator
from googletrans import Translator


translator = Translator()

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "bho": "Bhojpuri",
}


def translate_text(text: str, target_language: str) -> str:
    """
    Translate text using Google Translator via deep-translator
    Supported languages: 'en', 'hi', 'mr', etc.
    """
    return GoogleTranslator(source="auto", target=target_language).translate(text)
