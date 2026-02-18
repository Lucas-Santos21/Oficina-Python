from vendedor import Vendedor

class GerenciadorVendedores:
    def __init__(self):
        self.vendedores = []
    
    def buscar_vendedor(self, nome):
        nome = nome.strip().title()
        for vendedor in self.vendedores:
            if vendedor.nome == nome:
                return vendedor
            
        return None
    
    def listar_vendedores(self):
        return self.vendedores
    
    def cadastrar_vendedor(self, nome):
        if self.buscar_vendedor(nome):
            raise ValueError("Este vendedor ja existe!")
        
        vendedor = Vendedor(nome)
        self.vendedores.append(vendedor)
        return vendedor
    
    def registrar_venda(self, nome, valor):
        vendedor = self.buscar_vendedor(nome)

        if not vendedor:
            raise ValueError("Vendedor não encontrado.")
        
        vendedor.vender(valor)