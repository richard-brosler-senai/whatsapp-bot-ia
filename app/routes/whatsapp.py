from flask import Blueprint, Response, request
from twilio.twiml.messaging_response import MessagingResponse


whatsapp_bp = Blueprint(
    "whatsapp",
    __name__,
    url_prefix="/webhook"
)


@whatsapp_bp.route(
    "/whatsapp",
    methods=["POST"]
)
def whatsapp():

    message = request.form.get(
        "Body",
        ""
    ).strip()

    sender = request.form.get(
        "From",
        ""
    )

    print(
        f"WhatsApp recebido "
        f"de {sender}: {message}"
    )

    response = MessagingResponse()

    response.message(
        f"Recebi sua mensagem: {message}"
    )

    return Response(
        str(response),
        mimetype="text/xml"
    )