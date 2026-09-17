from flask import Blueprint, Response, request
from twilio.twiml.messaging_response import MessagingResponse

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

    # Mensagem vazia
    if not message:

        response.message(
            "Por enquanto consigo "
            "processar apenas mensagens de texto."
        )

        return Response(
            str(response),
            mimetype="text/xml"
        )

    # Proteção básica
    if len(message) > 4000:

        response.message(
            "Sua mensagem é muito longa."
        )

        return Response(
            str(response),
            mimetype="text/xml"
        )

    try:

        print(
            f"Mensagem recebida "
            f"de {sender}"
        )

        chat_service = ChatService()

        answer = chat_service.send_message(
            message
        )

        response.message(answer)

    except Exception as error:

        print(
            f"Erro WhatsApp: "
            f"{type(error).__name__}: {error}"
        )

        response.message(
            "Não consegui processar sua "
            "mensagem neste momento. "
            "Tente novamente em alguns instantes."
        )

    return Response(
        str(response),
        mimetype="text/xml"
    )