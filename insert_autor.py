from conectar import conexion

def insertar_autor():
    db = conexion()
    coleccion = db.autores

    nombre = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad del autor: ")

    nuevo_documento = {
        "nombre": nombre,
        "nacionalidad": nacionalidad
    }

    resultado = coleccion.insert_one(nuevo_documento)

    print("El id del nuevo autor es:", resultado.inserted_id)
