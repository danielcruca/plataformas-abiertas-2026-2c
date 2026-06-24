from flask import Blueprint, request, jsonify

estudiantes_endpoints = Blueprint('estudiantes_endpoints', __name__)


@estudiantes_endpoints.route('/saludo', methods=['GET'])
def saludar():
    data = request.get_json()

    nombre = data.get('nombre')
    apellido = data.get('apellido')

    if not nombre or not apellido:
        return jsonify({'error': 'Faltan parámetros nombre o apellido'}), 400

    saludo = f"Hola {nombre} {apellido}"
    return jsonify({'saludo': saludo}), 200


@estudiantes_endpoints.route('/hola', methods=['GET'])
def hola():
    return jsonify("hola mundo"), 200