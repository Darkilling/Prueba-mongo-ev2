from conectar import conexion

def insertar_cliente():
    db = conexion()
    coleccion = db.clientes

    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")

    nuevo_documento = {
        "nombre": nombre,
        "email": email
    }

    resultado = coleccion.insert_one(nuevo_documento)

    print("El id del nuevo cliente es:", resultado.inserted_id)