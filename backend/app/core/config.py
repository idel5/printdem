from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    PROJECT_NAME: str = "PrintDem API"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/printdem"
    
    SECRET_KEY: str = "your-secret-key-placeholder"

settings = Settings()
