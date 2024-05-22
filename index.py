from flask import *
from conectar import *



db = conexion()
app = Flask(__name__)


@app.route('/')
def mostrar_datos():
    libros = list(db.libros.find())
    autores = list(db.autores.find())
    clientes = list(db.clientes.find())
    pedidos = list(db.pedidos.find())
    return render_template('index.html', libros=libros, autores=autores, clientes=clientes, pedidos=pedidos)


@app.route('/libros')
def libros():

    libreria = db.libros
    find = libreria.find()

    return render_template('libros.html', libreria = find)

@app.route('/autores')
def autores():

    autor = db.autores
    find = autor.find()

    return render_template('autores.html', autor = find)

@app.route('/clientes')
def clientes():

    cliente = db.clientes
    find = cliente.find()

    return render_template('clientes.html', cliente = find)

@app.route('/pedidos')
def pedidos():

    pedido = db.pedidos
    find = pedido.find()

    return render_template('pedidos.html', pedido = find)

@app.route('/insertar_libro', methods=['GET', 'POST'])
def insertar_libro():
    if request.method == 'POST':
        id = request.form.get('id')
        titulo = request.form.get('titulo')
        autor = request.form.get('autor_id')
        precio = float(request.form.get('precio'))
        stock = int(request.form.get('stock'))

        nuevo_libro = {
            "_id": id,
            "titulo": titulo,
            "autor_id": autor,
            "precio": precio,
            "stock": stock
        }

        db.libros.insert_one(nuevo_libro)
 
        return redirect(url_for('libros'))


    return render_template('libros.html')

@app.route('/delete_libro', methods=['POST'])
def delete_libro():
    if request.method == 'POST':
        id = request.form.get('id')

        if id:
            db.libros.delete_one({"_id": id})
            return redirect(url_for('libros'))

    return render_template('libros.html')

@app.route('/update_libro', methods=['POST'])
def update_libro():
    if request.method == 'POST':
        id = request.form.get('id')
        titulo = request.form.get('titulo')
        autor = request.form.get('autor_id')
        precio = float(request.form.get('precio'))
        stock = int(request.form.get('stock'))

        if id:
            db.libros.update_one({"_id": id}, {'$set': {'titulo': titulo, 'autor_id': autor, 'precio': precio, 'stock': stock}})
            return redirect(url_for('libros'))

    return render_template('libros.html')

@app.route('/insertar_autor', methods=['GET', 'POST'])
def insertar_autor():
    
   if request.method == 'POST':
        id = request.form.get('id')
        nombre = request.form.get('nombre')
        nacionalidad = request.form.get('nacionalidad')

        nuevo_autor = {

          "autor_id": id,
          "nombre": nombre,
          "nacionalidad": nacionalidad
        }

        db.autores.insert_one(nuevo_autor)
        return redirect(url_for('autores'))
   return render_template('autores.html')

@app.route('/delete_autor', methods=['POST'])
def delete_autor():
    if request.method == 'POST':
        id = request.form.get('id')

        if id:
            db.autores.delete_one({"autor_id": id})
            return redirect(url_for('autores'))

    return render_template('autores.html')

@app.route('/update_autor', methods=['POST'])
def update_autor():
    if request.method == 'POST':
        id = request.form.get('id')
        nombre = request.form.get('nombre')
        nacionalidad = request.form.get('nacionalidad')

        if id:
            db.autores.update_one({"autor_id": id}, {'$set': {'nombre': nombre, 'nacionalidad': nacionalidad}})
            return redirect(url_for('autores'))

    return render_template('autores.html')

@app.route('/insertar_cliente', methods=['GET', 'POST'])
def insertar_cliente():

    if request.method == 'POST':
        id = request.form.get('id')
        nombre = request.form.get('nombre')
        email = request.form.get('email')

        nuevo_cliente = {

            "_id": id,
            "nombre": nombre,
            "email": email
        }

        db.clientes.insert_one(nuevo_cliente)
        return redirect(url_for('clientes'))
    return render_template('clientes.html')

@app.route('/delete_cliente', methods=['POST'])
def delete_cliente():
    if request.method == 'POST':
        id = request.form.get('id')

        if id:
            db.clientes.delete_one({"_id": id})
            return redirect(url_for('clientes'))

    return render_template('clientes.html')

@app.route('/update_cliente', methods=['POST'])
def update_cliente():
    if request.method == 'POST':
        id = request.form.get('id')
        nombre = request.form.get('nombre')
        email = request.form.get('email')

        if id:
            db.clientes.update_one({"_id": id}, {'$set': {'nombre': nombre, 'email': email}})
            return redirect(url_for('clientes'))

    return render_template('clientes.html')

@app.route('/insertar_pedido', methods=['POST'])
def insertar_pedido():
    if request.method == 'POST':
        id = request.form.get('id')
        cliente_id = request.form.get('cliente_id')
        libro_id = request.form.get('libro_id')
        cantidad = request.form.get('cantidad')
        total = request.form.get('total')

        if id and cliente_id and libro_id and cantidad and total:
            nuevo_pedido = {
                "_id": int(id),
                "cliente_id": int(cliente_id),
                "libro_id": int(libro_id),
                "cantidad": int(cantidad),
                "total": float(total)
            }

            db.pedidos.insert_one(nuevo_pedido)
            return redirect(url_for('pedidos'))

    return render_template('pedidos.html')


@app.route('/buscar', methods=['GET','POST'])
def buscar():
    resultado = db.libros
    find = list(resultado.find())

    if request.method == 'POST':
        id = request.form.get('id') 
        if id:
            libro = resultado.find_one({"_id": int(id)})
            if libro is None:
                libro = []
            return render_template('index.html', libros=[libro])
        else:
            if not find:
                find = []
            return render_template('index.html', libros=find)
        

       
'''@app.route ('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        id = request.form.get('id')
        if not id:
            print("Falta el ID del libro")
            return redirect(url_for('home'))

        coleccion = db.libros.find_one({"id": id})
        return render_template('resultado_busqueda.html', coleccion=coleccion)



@app.route('/insertar_libro', methods=['GET','POST'])
def insertar_libro():
    
    libreria = db.libros
    find = libreria.find()

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

    resultado = libreria.insert_one(nuevo_documento)

    print("El id del nuevo libro es:", resultado.inserted_id)
    return render_template('libros.html', datos = libreria.find)


@app.route('/buscar', methods=['GET','POST'])
def buscar():
    libros = []
    if request.method == 'POST':
        id = request.form.get('_id')
        if id:
            buscar = Buscar(id)
            libros = buscar.buscar()

            return render_template('index.html', datos = libros)
        else:
            return render_template('index.html', datos = [])
    else:
        return render_template('index.html')
'''


if __name__ == '__main__':
    app.run(debug=True)