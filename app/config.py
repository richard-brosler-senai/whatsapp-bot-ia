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

    # Groq
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GROQ_MODEL = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-120b"
    )

    GROQ_TEMPERATURE = float(
        os.getenv("GROQ_TEMPERATURE", "0.7")
    )

    GROQ_MAX_TOKENS = int(
        os.getenv("GROQ_MAX_TOKENS", "1000")
    )


settings = Settings()