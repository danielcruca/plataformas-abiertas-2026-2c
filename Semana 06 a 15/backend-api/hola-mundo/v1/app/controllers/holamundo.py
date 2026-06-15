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
    # obtenemos los parametros
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    apellido2 = request.args.get('apellido2')
    # Valida los parametros
    if not nombre or not apellido:
        return jsonify({'error': 'Faltan parámetros nombre o apellido'}), 400

    # Crea un saludo.
    saludo = f"Hola {nombre} {apellido} {apellido2} !"
    # Convierte el saludo a JSON
    return jsonify({'saludo': saludo}), 200 # la se convierte a JSON