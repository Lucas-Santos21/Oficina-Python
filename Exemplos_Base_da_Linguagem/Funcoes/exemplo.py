# Exemplo
def validar_Nome(nome):
    if any(char.isdigit() for char in nome):

        raise ValueError("A resposta não pode conter números")
    else:
        return True

def melhor_jogador(a):
    if(a == "b)Pelé"):
        print("")
        print("Certa Resposta!")
        return True
    else:
        print("")
        print("Tente novamente!")
        print("")
        return False

resposta = False

while True:
    try:
        print("")
        print("Qual o melhor jogador do mundo?")
        print("a)Messi")
        print("b)Pelé")
        print("c)Cristiano Ronaldo")
        print("d)Neymar")
        print("")
        resp = input("Resposta:")
        print("")
        
        validar_Nome(resp)
        
        if melhor_jogador(resp):
            break

    except ValueError as e:
        print("Erro: " + str(e))