# Exemplo
list_alunos = []

def validar_Nome(nome):
    if any(char.isdigit() for char in nome):
        raise ValueError("Um nome não pode conter números")
    else:
        return True
        

while True:
    try:        
        qnt = int(input("Digite a quantidade de alunos a adicionar: "))
        break
    except ValueError:
        print("digite um numero inteiro")

print("")

for i in range(qnt):    
    while True:
        try:
            nome = input("Digite o nome do aluno " + str(i + 1) + " :")
            validar_Nome(nome)
            list_alunos.append(nome)
            print("Nome salvo!")
            break
        except ValueError as e:
            print("Erro: " + str(e))

print("")
print("Alunos Cadastrados:")
print("")


for aluno in list_alunos:
    print("Aluno:", aluno[0])