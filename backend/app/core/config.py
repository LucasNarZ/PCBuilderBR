from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    database_url: str

    model_config = {"env_file": Path(__file__).resolve().parent.parent.parent.parent / ".env", "extra": "ignore"}

settings = Settings()

