from gtts import gTTS
import uuid
import os

class VoiceAgent:
    def generate_voice(self, text: str, lang: str) -> str | None:
        try:
            os.makedirs("audio", exist_ok=True)
            filename = f"audio/{uuid.uuid4()}.mp3"

            tts = gTTS(text=text, lang=lang)
            tts.save(filename)

            return filename

        except Exception as e:
            print("⚠️ Voice generation failed (network issue).")
            print("⚠️ Error:", e)
            return None
