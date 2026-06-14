import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "AI Dance SaaS"
    ENV = os.getenv("ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    AI_PROVIDER = os.getenv("AI_PROVIDER", "mock")

settings = Settings()
