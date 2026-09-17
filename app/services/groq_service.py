from groq import Groq

from app.config import settings


class GroqService:

    def __init__(self):

        if not settings.GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY não foi configurada."
            )

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def chat(self, messages: list[dict]) -> str:

        response = self.client.chat.completions.create(

            model=settings.GROQ_MODEL,

            messages=messages,

            temperature=settings.GROQ_TEMPERATURE,

            max_completion_tokens=settings.GROQ_MAX_TOKENS
        )

        return response.choices[0].message.content