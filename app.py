from flask import Flask, render_template, request, redirect
from connection_handler import connectionHandler

app = Flask(__name__)

# Configurações do banco de dados
connection_handler = connectionHandler(
    host='autorack.proxy.rlwy.net',
    username='root',
    password='CGwuHntYlbgdGDnqjXcqQmTbAulRrWUv',
    database='railway',
    port=38176
)

@app.route('/')
def index():
    cursos = connection_handler.listar_todos()
    return render_template('index.html', cursos=cursos)

@app.route('/programacao')
def programacao():
    cursos = connection_handler.buscar_por_categoria('Programação')
    return render_template('index.html', cursos=cursos)

@app.route('/design')
def design():
    cursos = connection_handler.buscar_por_categoria('Design')
    return render_template('index.html', cursos=cursos)

@app.route('/marketing')
def marketing():
    cursos = connection_handler.buscar_por_categoria('Marketing')
    return render_template('index.html', cursos=cursos)

@app.route('/buscar', methods=['GET'])
def buscar():
    nome = request.args.get('nome')
    categoria = request.args.get('categoria')
    
    cursos = []
    
    if nome:
        cursos = connection_handler.buscar_por_nome(nome)
    elif categoria:
        cursos = connection_handler.buscar_por_categoria(categoria)
    else:
        cursos = connection_handler.listar_todos()
    
    return render_template('index.html', cursos=cursos)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
