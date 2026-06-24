from flask import Blueprint, Flask, jsonify, request 
from flask import Blueprint, jsonify

estudiante_endpoint = Blueprint('estudiante_endpoints', __name__)

#http://127.0.0.1:5000/estudiante/api/v1/hola
@estudiante_endpoint.route('/hola', methods=['GET'])
def holamundo():    
    return jsonify({"message": "Hola estudiante", "status": "success"})

#http://127.0.0.1:5000/estudiante/api/v1/saludo
@estudiante_endpoint.route('/saludo', methods=['GET'])
def saludo():
    
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    if not nombre or not apellido:
        return jsonify({'error': 'Faltan parámetros nombre o apellido'}), 400

    saludo = f"Hola estudiante {nombre} {apellido}"
    return jsonify({'saludo': saludo}), 200

# http://127.0.0.1:5000/estudiante/api/v1/saludo-parametros?nombre=Luis&apellido=Coto
@estudiante_endpoint.route('/saludo-parametros', methods=['GET'])
def saludo_con_parametros():
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    if not nombre or not apellido:
        return jsonify({'error': 'Faltan parámetros nombre o apellido'}), 400

    saludo = f"Hola estudiante {nombre} {apellido}"
    return jsonify({'saludo': saludo}), 200
