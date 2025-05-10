
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
app.secret_key = os.getenv('CLAVE_SECRETA')

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

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        clave = request.form.get('clave')
        if clave == os.getenv('CLAVE_SECRETA'):
            return render_template('nuevo.html')
        else:
            return "Clave incorrecta", 403
    return render_template('clave.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nuevo_proyecto = {
        "nombre": request.form['nombre'],
        "descripcion": request.form['descripcion'],
        "link": request.form['link'],
        "imagen": request.form['imagen']
    }

    with open('proyectos.json', 'r', encoding='utf-8') as f:
        proyectos = json.load(f)

    proyectos.append(nuevo_proyecto)

    with open('proyectos.json', 'w', encoding='utf-8') as f:
        json.dump(proyectos, f, ensure_ascii=False, indent=2)

    return redirect('/proyectos')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
