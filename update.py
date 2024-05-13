from conectar import conexion

def modificar_libro():
    id_libro = input("Ingrese el ID del libro para cambiar: ")
    nuevo_precio = float(input("Ingrese el nuevo precio del libro: "))
    nuevo_stock = int(input("Ingrese el nuevo stock del libro: "))

    db = conexion()
    coleccion = db.libros  
    filtro = {"_id": id_libro}  
    update = {"$set": {"precio": nuevo_precio, "stock": nuevo_stock}}

    try:
        cambiar = coleccion.update_one(filtro, update)
        print("Datos del libro cambiados correctamente")
    except Exception as e:
        print("Error al cambiar los datos del libro:", e)

if __name__ == "__main__":
    modificar_libro()