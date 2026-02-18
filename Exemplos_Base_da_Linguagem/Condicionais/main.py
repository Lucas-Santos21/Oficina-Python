# Condições
valor1 = 10
valor2 = 20

if valor1 > valor2:
    print(valor1, "é maior que", valor2)
else:
    print(valor2, "é maior que", valor1)

# Outro exemplo

salario = float(input('Informe o salário: '))

if salario <= 3000:
    print('programador junior')
elif salario > 3000 and salario <= 6000:
    print('programador pleno')
elif salario > 6000 and salario <= 15000:
    print('programador senior')
else:
    print('gerente de projetos')