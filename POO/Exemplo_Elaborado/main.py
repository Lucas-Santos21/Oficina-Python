from gerenciador import GerenciadorVendedores
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione Enter para continuar...")

def menu():
    limpar_tela()
    print("\n===== SISTEMA DE VENDAS =====")
    print("1 - Cadastrar vendedor")
    print("2 - Registrar venda")
    print("3 - Listar vendedores")
    print("4 - Verificar meta")
    print("5 - Sair")


def main():
    gerenciador = GerenciadorVendedores()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:

            if opcao == "1":
                nome = input("Nome do vendedor: ")
                gerenciador.cadastrar_vendedor(nome)
                print("Vendedor cadastrado com sucesso!")
                pausar()


            elif opcao == "2":
                nome = input("Nome do vendedor: ")
                valor = float(input("Valor da venda: "))
                gerenciador.registrar_venda(nome, valor)
                print("Venda registrada com sucesso!")
                
                pausar()


            elif opcao == "3":
                vendedores = gerenciador.listar_vendedores()

                if not vendedores:
                    print("Nenhum venddor cadastrado.")
                else:
                    for vendedor in vendedores:
                        print(vendedor)

                pausar()


            elif opcao == "4":
                nome = input("Nome do vendedor: ")
                meta = float(input("Valor da meta: "))
                vendedor = gerenciador.buscar_vendedor(nome)

                if not vendedor:
                    print("Vendedor não encontrado.")
                else:
                    if vendedor.bateu_meta(meta):
                        print("Meta atingida!")
                    else:
                        print("Meta ainda não atingida.")

                pausar()


            elif opcao == "5":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida.")
                pausar()

        except ValueError as e:
            print("Erro", e)
            pausar()


if __name__ == "__main__":
    main()