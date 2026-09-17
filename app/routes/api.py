from datetime import datetime
from flask import Blueprint, jsonify
from app.config import settings

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