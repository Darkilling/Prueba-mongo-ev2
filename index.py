from flask import *
from conectar import *

db = conexion()
app = Flask(__name__)
@app.route('/')


def home():
    libreria = db.libros
    find = libreria.find()

    return render_template('index.html', libreria = find)

if __name__ == '__main__':
    app.run(debug=True)