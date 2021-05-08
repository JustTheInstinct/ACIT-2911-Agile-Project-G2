from flask import Flask
from .pvz import pvz_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pvz_bp)
    return app