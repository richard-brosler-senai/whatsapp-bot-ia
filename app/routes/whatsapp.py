from flask import Blueprint, request, jsonify


whatsapp_bp = Blueprint(
    "whatsapp",
    __name__,
    url_prefix="/webhook"
)


@whatsapp_bp.route("/whatsapp", methods=["POST"])
def whatsapp():
    mensagem = request.form.get("Body", "")
    remetente = request.form.get("From", "")

    print(f"Mensagem recebida de {remetente}: {mensagem}")

    return jsonify({
        "status": "received"
    })