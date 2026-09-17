from datetime import datetime

from flask import Blueprint, jsonify, request

from app.config import settings
from app.services.chat_service import ChatService


api_bp = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


@api_bp.route("/health", methods=["GET"])
def health():

    return jsonify({
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    })


@api_bp.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json(silent=True) or {}

        message = str(
            data.get("message", "")
        ).strip()

        if not message:

            return jsonify({
                "error": "Mensagem não informada."
            }), 400

        # Proteção básica
        if len(message) > 4000:

            return jsonify({
                "error": "Mensagem muito longa."
            }), 400

        chat_service = ChatService()

        answer = chat_service.send_message(
            message
        )

        return jsonify({
            "answer": answer
        })

    except Exception as error:

        print(
            f"Erro ao processar chat: "
            f"{type(error).__name__}: {error}"
        )

        return jsonify({
            "error": "Não foi possível processar a mensagem."
        }), 500