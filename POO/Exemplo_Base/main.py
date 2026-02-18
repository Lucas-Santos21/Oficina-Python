# Exemplo sem a classe
vendedor = "Lucas"

vendas = 1000

meta = 500

if vendas >= meta:
    print("Bateu a meta")
else:
    print("Não bateu a meta")


# Exemplo com a classe
class Vendedor():
    #inicializa a classe
    # O self deve existir como primeiro argumento nos métodos para indicar 
    # que o metodo pertence a instancia de uma classe
    
    def __init__(self, nome):
        #inicializando as propriedades
        # self simboliza que o atributo foi criado e pertence a classe
        
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas += vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print("O vendedor", self.nome, "Bateu a meta!")
        else:
            print("O vendedor", self.nome, "Não bateu a meta!")

# Testando a classe
vendedor1 = Vendedor(nome = "Lucas")

print("Vendedor:", vendedor1.nome)
print("Valor das vendas totais:", vendedor1.vendas)
print()

vendedor1.bateu_meta(600)

vendedor2 = Vendedor(nome = "Ronaldo")
vendedor2.vendeu(700)

print()
print("Vendedor:", vendedor2.nome)
print("Valor das vendas totais:", vendedor2.vendas)
print()

vendedor2.bateu_meta(600)