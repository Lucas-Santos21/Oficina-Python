# Exemplo

# informações do jogador
player = {
    "nome": "Lucas",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5
}

# lista de inimigos
npcs = [
    {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    {"nome": "Monstro", "dano": 5, "hp": 100, "exp": 10},
    {"nome": "Monstrão", "dano": 10, "hp": 150, "exp": 15},
    {"nome": "Chefão", "dano": 25, "hp": 200, "exp": 20}
]

#Informações do jogador:
print("Informações que o player possui:")
print("")

for info in player.keys():
    print(info)

print("")
print("Dados do player:")
print("")

for valor in player.values():
    print(valor)

print("")

#Informações dos inimigos
print("Informações dos inimigos:")
print("")

for npc in npcs:
    for info, valor in npc.items():
        print(str(info), ":", str(valor))
    print("")