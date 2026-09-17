import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    APP_NAME = os.getenv(
        "APP_NAME",
        "WhatsApp Bot IA"
    )
    APP_ENV = os.getenv(
        "APP_ENV",
        "development"
    )
    HOST = os.getenv(
        "HOST",
        "127.0.0.1"
    )
    PORT = int(
        os.getenv("PORT", "5000")
    )
    DEBUG = os.getenv(
        "DEBUG",
        "false"
    ).lower() == "true"
settings = Settings()