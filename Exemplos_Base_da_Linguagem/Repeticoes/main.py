# Laços de repeticao

#for
notas = []

for x in range(3):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print(notas)

for aluno in notas:
    print("Aluno:", aluno[0], "nota:", aluno[1])


#while
resp = ""

while resp != "Pelé":
    print("Você prefere Messi ou Pelé?")
    resp = input("Resposta:")
    print("")

    if resp != "Pelé":
        print("Tem certeza? pense melhor!")
        print("")

print("Concordo! Pelé melhor jogador da história.")