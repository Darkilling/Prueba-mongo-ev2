'''from conectar import conexion
from flask import Flask ,request, render_template

app = Flask(__name__)

def insertar_libro():
    db = conexion()
    coleccion = db.libros

    id= request.form.get('id')
    titulo = request.form.get('titulo')
    autor = request.form.get('autor_id')
    precio = float(request.form.get('precio'))
    stock = int(request.form.get('stock'))

    nuevo_documento = {
        "_id": id, 
        "titulo": titulo,
        "autor_id": autor,
        "precio": precio,
        "stock": stock
    }

    resultado = coleccion.insert_one(nuevo_documento)

    print("El id del nuevo libro es:", resultado.inserted_id)
    return render_template('insert_libro.html')'''