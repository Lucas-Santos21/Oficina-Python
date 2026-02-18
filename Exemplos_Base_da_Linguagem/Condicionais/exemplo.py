# Exemplo:
while True:
    try:
        idade = int(input("Informe a sua idade:"))
        break
    
    except ValueError:
        print('Digite um número')


if (idade >= 18):
    print('Adulto!')
else:
    print('Não é adulto!')
