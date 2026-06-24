from flask import Flask
from flask_cors import CORS
from .controllers.holamundo import holamundo_endpoints
from .controllers.estudiantes import estudiantes_endpoints

def create_app():
    app = Flask(__name__)
    app.register_blueprint(holamundo_endpoints, url_prefix="/holamundo-ejemplo/api/v1")
    app.register_blueprint(estudiantes_endpoints, url_prefix="/estudiantes/api/v1")
    CORS(app, origins="*")
    return app