from flask import Blueprint, request, jsonify
# De momento no se usa el modelo.

holamundo_endpoints = Blueprint('holamundo_endpoints', __name__)

# GET todas las ventas
# http://127.0.0.1:5000/holamundo-ejemplo/api/v1/holamundo
@holamundo_endpoints.route('/holamundo', methods=['GET'])
def obtener_ventas():
    holaMundo = "hola mundo"
    return jsonify(holaMundo), 200 # la se convierte a JSON

# http://127.0.0.1:5000/holamundo-ejemplo/api/v1/saludo?nombre=Jose&apellido=Mujica
@holamundo_endpoints.route('/saludo', methods=['GET'])
def saludar():
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    if not nombre or not apellido:
        return jsonify({'error': 'Faltan parámetros nombre o apellido'}), 400

    saludo = f"Hola {nombre} {apellido}"
    return jsonify({'saludo': saludo}), 200