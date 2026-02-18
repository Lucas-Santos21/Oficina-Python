class Vendedor():
    
    def __init__(self, nome):
        self.nome = nome.strip().title()
        self.vendas = 0.0

    def total_vendas(self):
        return self.vendas

    def vender(self, valor):
        if valor <= 0:
            raise ValueError("O valor da venda deve ser maior que zero.")
        
        self.vendas += valor

    def bateu_meta(self, meta):
        return self.vendas >= meta
    
    def __str__(self):
        return "Vendedor: " + self.nome + " | Total em vendas: R$ " + str(self.vendas)