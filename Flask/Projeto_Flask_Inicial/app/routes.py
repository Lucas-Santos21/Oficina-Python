from app import app
from flask import render_template #permite chamar arquivos html do projeto

#Rota inicial do projeto
@app.route('/')
@app.route('/index')

def index():
    nome = "Lucas"
    dados = {"profissão": "Programador", "idade": "90"}

    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')

def contato():
    return render_template('contato.html')