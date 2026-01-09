from gtts import gTTS
import uuid
import os

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)


def text_to_speech(text: str, language: str = "en") -> str:
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text=text, lang=language)
    tts.save(file_path)

    return file_path
