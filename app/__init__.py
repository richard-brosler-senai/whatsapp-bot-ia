from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.web import web_bp
    from app.routes.api import api_bp
    from app.routes.whatsapp import whatsapp_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(whatsapp_bp)

    return app