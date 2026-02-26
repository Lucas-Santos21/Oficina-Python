#FLASK - Backend

# Importando do flask:
# Flask -> para utilizá-lo no projeto
# url_for -> para montar links para outras rotas

from flask import Flask, url_for 

# Inicialização

app = Flask(__name__) # inicializa o Flask

# Rotas
# Criando a rota

@app.route('/') # OBS: se não declarar o methods, o padrão é GET

# Função que recebe a requisição -> SEMPRE deve retornar algo!

def ola_mundo():
    return f"<a href='{ url_for('pagina_sobre') }'>Página sobre"    # url_for chama a função associada a rota que queremos acessar

@app.route('/sobre')
def pagina_sobre():
    return """
        <b>Dica: </b>Assista as melhores jogadas do Cristiano Ronaldo!"
        <a href="https://www.youtube.com/">Pesquise no Youtube!
    """


# Execução

app.run(debug=True) #executa o servidor web -> debug=True ativa o modo dev 