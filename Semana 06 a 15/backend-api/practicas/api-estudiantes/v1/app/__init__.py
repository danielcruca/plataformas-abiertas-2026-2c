from flask import Flask
from flask_cors import CORS
from .controllers.estudiantes import estudiante_endpoint 

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(estudiante_endpoint , url_prefix='/estudiante/api/v1')
    CORS(app, origin='*')
    return app