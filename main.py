
from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    with open('proyectos.json', 'r', encoding='utf-8') as f:
        lista_proyectos = json.load(f)
    return render_template('proyectos.html', proyectos=lista_proyectos)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
