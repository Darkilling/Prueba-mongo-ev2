from flask import *
from conectar import *

db = conexion()
app = Flask(__name__)
@app.route('/')

def home():
    evaluacion = db.evaluacion2
    find = libros.find()

    return render_template('index.html', evaluacion = find)

