'''from conectar import conexion
from flask import *

def insertar_cliente():
    db = conexion()
    coleccion = db.clientes

    id = request.form.get('id')
    nombre = request.form.get('nombre')
    email = request.form.get('email')

    nuevo_documento = {
        "_id": id,
        "nombre": nombre,
        "email": email
    }

    resultado = coleccion.insert_one(nuevo_documento)

    print("El id del nuevo cliente es:", resultado.inserted_id)
    return render_template('clientes.html')'''