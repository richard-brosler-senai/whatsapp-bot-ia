from app.services.groq_service import GroqService


SYSTEM_PROMPT = """
Você é um assistente virtual prestativo.

Responda sempre em português brasileiro, exceto quando
o usuário solicitar explicitamente outro idioma.

Seja educado, objetivo e claro.

Quando não souber uma informação, informe que não sabe
em vez de inventar uma resposta.
""".strip()


class ChatService:

    def __init__(self):
        self.groq = GroqService()

    def send_message(self, message: str) -> str:

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ]

        return self.groq.chat(messages)