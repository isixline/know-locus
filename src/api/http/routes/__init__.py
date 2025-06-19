from flask import Flask
from flask_cors import CORS
from .nodes import nodes_bp
from .matcher import matcher_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(nodes_bp)
    app.register_blueprint(matcher_bp)
    return app
