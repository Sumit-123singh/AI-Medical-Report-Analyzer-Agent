from services.translation_service import translate_text


class TranslateAgent:
    def translate(self, text: str, target_language: str) -> str:
        """
        Translate text into selected language (hi, mr, en, etc.)
        """
        translated_text = translate_text(
            text=text,
            target_language=target_language
        )
        return translated_text
