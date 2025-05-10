
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    lista_proyectos = [
        {
            'nombre': 'Chatbot con GPT',
            'descripcion': 'Un chatbot basado en inteligencia artificial usando OpenAI.',
            'link': 'https://github.com/tuusuario/chatbot-gpt',
            'imagen': 'https://placehold.co/300x200?text=Chatbot'
        },
        {
            'nombre': 'Análisis de Sentimientos',
            'descripcion': 'Web app que analiza el sentimiento de un texto.',
            'link': 'https://github.com/tuusuario/analisis-sentimientos',
            'imagen': 'https://placehold.co/300x200?text=Sentimientos'
        }
    ]
    return render_template('proyectos.html', proyectos=lista_proyectos)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
