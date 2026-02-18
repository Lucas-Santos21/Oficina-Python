import os

mensagens = []

while True:

    # Limpando terminal
    os.system('clear')

    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print('_________________________')

    # obtendo texto
    nome = input("Nome: ")
    texto = input("Mensagem: ")

    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })