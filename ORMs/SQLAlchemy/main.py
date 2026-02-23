# SQLAlchemy

# É um ORM(Object Relational Mapper)
# É uma biblioteca que permite criar e editar bancos de dados SQL,
# por meio de codigos em Python
# Para instalar -> terminal: pip install sqlalchemy

# É necessário importar o SQLAlchemy para utilizá=lo

from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey # Importando os tipos das colunas e o criador do db
from sqlalchemy.orm import sessionmaker, declarative_base # Importando a base e a sessao

# Criando o Banco de dados:

# db -> Variavel que armazena a instacia do banco, sera usada para realizar operações no banco
# create_engine -> Cria o banco de dados. Se ele já existir, funciona como uma ponte de conexão com o banco 
# sqlite -> Define o tipo do banco
# :/// -> Separa o driver do caminho. A quantidade de barras define o tipo de endereço:
#        1. CAMINHO RELATIVO (3 barras): Procura a partir da pasta atual do script.
#           Ex: 'sqlite:///meubanco.db' (na mesma pasta)
#           Ex: 'sqlite:///models/meubanco.db' (dentro da subpasta 'models')
#        2. CAMINHO ABSOLUTO (Endereço completo):
#           Linux/Mac (4 barras): 'sqlite:////home/usuario/meubanco.db'
#           Windows (3 barras + letra da unidade): 'sqlite:///C:\dados\meubanco.db'

# OBS: Para outros bancos de dados o caminho/chave de acesso será especifico para cada um deles
#      Recomendavel consultar documentação do banco que será utilizado.

db = create_engine("sqlite:///meubanco.db")

# Criando uma sessão no banco de dados:

# Uma sessão permite realizar modificações no banco e guarda alterações feitas para manipular o banco

# Session = sessionmaker(bind-nome-do-banco) -> cria o obj da sessão, para realizar as alterações no banco

Session = sessionmaker(bind=db) # bind indica qual o banco e o nome dele
session = Session() # Cria uma instancia de Session() que pode ser reutilizado

# Criando a Base

# A Base serve para permitir criar tabelas no bdd a partir de classes python,
# onde a classe que herda a Base (ex: class Usuario(base):) é uma tabela, e seus atributos os campos.

Base = declarative_base() 

# Criando tabelas(ex: Biblioteca)

# usuario
class Usuario(Base):
    __tablename__ = "usuarios" # passando um nome especifico para a tabela (sem declarar, nome será o nome da classe em minusculo com um 's' adicionado no final)
    
    id = Column("id", Integer, primary_key=True, autoincrement=True) 
    nome = Column("nome", String) #Criando as colunas -> 1º parametro: nome da colna, 2º parametro: Tipo aceito na coluna
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

# Livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qnt_paginas = Column("qnt_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qnt_paginas, dono):
        self.titulo = titulo
        self.qnt_paginas = qnt_paginas
        self.dono = dono


#Para criar as tabelas no Banco:

Base.metadata.create_all(bind=db)

# OBS: Caso queira criar o banco sem tabelas, execute o comando acima sem declarar as tabelas(classes)
# OBS2: O comando de criação do banco e das tabelas DEVE SER O ULTIMO DO CODIGO
#       caso não seja, ele n irá reconhecer as tabelas e não vai criá-las


# Base -> É a classe base declarada anteriormente, que as outras classes herdam
# metadata -> É o registro de todos os objetos 'Table' que foram definidos atravéz da base
# create_all() -> É o comando que instrui o SQLAlchemy a verificar as tabelas que ainda não existem no banco e criá-las

#Manipulando dados no banco

# Inserindo um Usuario
usuario = Usuario(nome="Lucas", email="teste@email.com", senha="123456") # Criando um usuário com dados apssados
session.add(usuario) #registra na sessão que um usuario foi criado
session.commit() # Envia as alterações feitas na sessão para o Banco de Dados

usuario = Usuario(nome="Lucas2", email="teste2@email.com", senha="123456") # Criando um usuário com dados apssados
session.add(usuario) #registra na sessão que um usuario foi criado
session.commit() # Envia as alterações feitas na sessão para o Banco de Dados

# Buscando o Usuário no Banco
# lista_usuarios = session.query(Usuario).all() # Realizando uma Query na tabela Usuário(.all() busca todos os dados da tabela)
usuario_lucas = session.query(Usuario).filter_by(email = "teste@email.com").first() #filtra o dado e pega o primeiro resultado
print(usuario_lucas)
print(usuario_lucas.nome)
print(usuario_lucas.email)

# Inserindo um Livro
livro = Livro(titulo="Historia da Terra", qnt_paginas=200, dono=usuario_lucas.id)
session.add(livro)
session.commit()

# Atualizando um dado
usuario_lucas.nome = "Lucas teste"
session.add(usuario_lucas)
session.commit()

print(usuario_lucas.nome)

# Deletando um dado
usuario_lucas2 = session.query(Usuario).filter_by(email = "teste2@email.com").first()
session.delete(usuario_lucas2)
session.commit()