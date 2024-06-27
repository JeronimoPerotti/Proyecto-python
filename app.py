from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/') #app es la instancia, route el metodo y '/ disparador

def index():
    return render_template(
        'index.html',
    )
@app.route('/info')

def informacion():
    return render_template(
        'informacion.html',
    )
@app.route('/bienvenido/<nombre>')
def bienvenida(nombre):
    return render_template(
        'bienvenida.html',
    )