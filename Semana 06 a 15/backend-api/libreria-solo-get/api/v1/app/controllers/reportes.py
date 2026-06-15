from app.models.reportes_ventas import ReportesVentas
from flask import Blueprint, request, jsonify

reportes_endpoint = Blueprint('reportes_endpoint', __name__)
#End point: http://127.0.0.1:5000/libreria/api/v1//reportes/top3
@reportes_endpoint.route("/reportes/top3", methods=["GET"])
def top_3():
    return jsonify(ReportesVentas.top_3_libros_mas_vendidos())

# End point: http://127.0.0.1:5000/libreria/api/v1//reportes/con-ventas
@reportes_endpoint.route("/reportes/con-ventas", methods=["GET"])
def con_ventas():
    return jsonify(ReportesVentas.libros_con_ventas())

#end point: http://127.0.0.1:5000/libreria/api/v1//reportes/vendidos-con-stock
@reportes_endpoint.route("/reportes/vendidos-con-stock", methods=["GET"])
def vendidos_stock():
    return jsonify(ReportesVentas.libros_vendidos_con_stock())
#end point: http://127.0.0.1:5000/libreria/api/v1//reportes/top5
@reportes_endpoint.route("/reportes/top5", methods=["GET"])
def top_5():
    return jsonify(ReportesVentas.top_5_libros_mas_vendidos())
