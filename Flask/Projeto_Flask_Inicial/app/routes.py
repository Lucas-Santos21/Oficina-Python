from app import app
from flask import render_template, request, redirect, session, url_for, flash #render permite chamar arquivos html do projeto

#Rota inicial do projeto
@app.route('/')
def index():
    return render_template('index.html.j2')


@app.route('/contato')
def contato():
    return render_template('contato.html.j2')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se alguém já estiver logado e tentar postar de novo, apenas manda pro dash
    
    if 'usuario_logado' in session:
        return redirect(url_for('dashbord'))
    
    if request.method == 'GET':
        return render_template('login.html.j2')

    if request.method == 'POST':
        usuario = request.form.get('username')
        senha = request.form.get('password')

        if not usuario or not senha:
            flash('Preencha todos os campos!', 'erro')
            return redirect(url_for('login'))
        
         # Salva na sessão
        session['usuario_logado'] = usuario

        return redirect(url_for('dashbord'))

@app.route('/dashbord')
def dashbord():
    # Busca o dado que foi salvo no login
    usuario = session.get('usuario_logado')

    if not usuario:
        return redirect(url_for('login')) # Volta se tentar entrar sem post
    
    return render_template('dashbord.html.j2', usuario=usuario)

@app.route('/logout', methods=['POST'])
def logout():

    session.pop('usuario_logado', None)
    flash('Usuario deslogado', 'sucesso')
    return redirect(url_for('login'))