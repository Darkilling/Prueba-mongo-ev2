from conectar import conexion

def insertar_libro():
    db = conexion()
    coleccion = db.libros

    id = int(input("Ingrese el id del libro: "))
    titulo = input("Ingrese el título del libro: ")
    autor_id = int(input("Ingrese el ID del autor: "))
    precio = float(input("Ingrese el precio del libro: "))
    stock = int(input("Ingrese el stock del libro: "))

    nuevo_documento = {
        "id": id,
        "titulo": titulo,
        "autor_id": autor_id,
        "precio": precio,
        "stock": stock
    }

    resultado = coleccion.insert_one(nuevo_documento)

    print("El id del nuevo libro es:", resultado.inserted_id)