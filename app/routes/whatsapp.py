from flask import Blueprint, Response, request
from twilio.twiml.messaging_response import MessagingResponse

from app.security.twilio_validator import validate_twilio_request
from app.services.chat_service import ChatService


whatsapp_bp = Blueprint(
    "whatsapp",
    __name__,
    url_prefix="/webhook"
)


@whatsapp_bp.route(
    "/whatsapp",
    methods=["POST"]
)
@validate_twilio_request
def whatsapp():

    message = request.form.get(
        "Body",
        ""
    ).strip()

    sender = request.form.get(
        "From",
        ""
    )

    response = MessagingResponse()

    if not message:

        response.message(
            "Por enquanto consigo processar "
            "apenas mensagens de texto."
        )

        return Response(
            str(response),
            mimetype="text/xml"
        )

    if len(message) > 4000:

        response.message(
            "Sua mensagem é muito longa."
        )

        return Response(
            str(response),
            mimetype="text/xml"
        )

    try:

        # Não registrar o número completo
        print("Mensagem WhatsApp recebida.")

        chat_service = ChatService()

        answer = chat_service.send_message(
            message
        )

        response.message(answer)

    except Exception as error:

        print(
            "Erro WhatsApp: "
            f"{type(error).__name__}"
        )

        response.message(
            "Não consegui processar sua mensagem "
            "neste momento. Tente novamente."
        )

    return Response(
        str(response),
        mimetype="text/xml"
    )