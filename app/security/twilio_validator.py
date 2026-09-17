from functools import wraps

from flask import abort, request
from twilio.request_validator import RequestValidator

from app.config import settings


def validate_twilio_request(func):

    @wraps(func)
    def decorated_function(*args, **kwargs):

        if not settings.TWILIO_AUTH_TOKEN:
            print("ERRO: TWILIO_AUTH_TOKEN não configurado.")
            abort(500)

        signature = request.headers.get(
            "X-Twilio-Signature",
            ""
        )

        if not signature:
            print("Webhook rejeitado: assinatura ausente.")
            abort(403)

        validator = RequestValidator(
            settings.TWILIO_AUTH_TOKEN
        )

        url = request.url

        # Render trabalha atrás de proxy reverso.
        forwarded_proto = request.headers.get(
            "X-Forwarded-Proto"
        )

        if forwarded_proto == "https" and url.startswith("http://"):
            url = "https://" + url[len("http://"):]

        valid = validator.validate(
            url,
            request.form,
            signature
        )

        if not valid:
            print("Webhook rejeitado: assinatura inválida.")
            abort(403)

        return func(*args, **kwargs)

    return decorated_function