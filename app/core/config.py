from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    #OPENAI_API_KEY: str
    DATABASE_URL: str | None = None
    SECRET_KEY: str | None = None
    algorithm:str="HS256"

    class Config:
        env_file = BASE_DIR.parent / ".env"


settings = Settings()
