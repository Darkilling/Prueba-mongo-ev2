from flask import *
from conectar import *

db = conexion()
app = Flask(__name__)
@app.route('/')

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

if __name__ == '__main__':
    app.run(debug=True)