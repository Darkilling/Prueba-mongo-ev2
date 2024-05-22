'''from conectar import conexion

def insertar_pedido():
    db = conexion()
    coleccion = db.pedidos

    cliente_id = int(input("Ingrese el ID del cliente: "))
    libro_id = int(input("Ingrese el ID del libro: "))
    cantidad = int(input("Ingrese la cantidad: "))
    total = float(input("Ingrese el total: "))

    nuevo_documento = {
        "cliente_id": cliente_id,
        "libro_id": libro_id,
        "cantidad": cantidad,
        "total": total
    }

    resultado = coleccion.insert_one(nuevo_documento)

    print("El ID del nuevo pedido es:", resultado.inserted_id)'''