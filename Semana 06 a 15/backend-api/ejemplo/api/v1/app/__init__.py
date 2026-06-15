from flask import Flask
from flask_cors import CORS
# Importante: Aca se importa el controller.
from .holamundocontrollers.holamundo import holamundo_endpoints

from controllers.holamundocontrollers.holamundo import holamundo_endpoints


def create_app():
    # Importante: Usamos flask y flask_cors para crear la app. 
    app = Flask(__name__)
    app.register_blueprint(holamundo_endpoints, url_prefix="/holamundo-ejemplo/api/v1")
    # IMPORTANTE: Esto es solo para probar, estamos permitiendo el acceso desde cualquier origen.
    # Esto es importante para cuando hagamos el frontend.
    CORS(app, origins="*")
    return app
