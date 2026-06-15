from app import mongo

class ReportesVentas:

    @staticmethod
    def top_3_libros_mas_vendidos():
        pipeline = [
            {"$group": {
                "_id": "$libro.titulo",
                "total_vendido": {"$sum": "$cantidad"}
            }},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 3}
        ]
        return list(mongo.db.ventas.aggregate(pipeline))

    @staticmethod
    def libros_con_ventas():
        # Devuelve solo los títulos
        return mongo.db.ventas.distinct("libro.titulo")

    @staticmethod
    def libros_vendidos_con_stock():
        # Agrupa ventas por título
        pipeline = [
            {"$group": {
                "_id": "$libro.titulo",
                "cantidad_vendida": {"$sum": "$cantidad"}
            }}
        ]
        vendidos = list(mongo.db.ventas.aggregate(pipeline))

        resultado = []
        for venta in vendidos:
            libro = mongo.db.libros.find_one({"titulo": venta["_id"]})
            if libro:
                resultado.append({
                    "titulo": venta["_id"],
                    "cantidad_vendida": venta["cantidad_vendida"],
                    "stock_restante": libro.get("cantidad_stock", 0)
                })
        return resultado

    @staticmethod
    def top_5_libros_mas_vendidos():
        pipeline = [
            {"$group": {
                "_id": "$libro.titulo",
                "cantidad_vendida": {"$sum": "$cantidad"}
            }},
            {"$sort": {"cantidad_vendida": -1}},
            {"$limit": 5}
        ]
        return list(mongo.db.ventas.aggregate(pipeline))
