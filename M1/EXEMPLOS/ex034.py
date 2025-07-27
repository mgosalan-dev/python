# Exercício 34 - Aumento de salário


salario = float(input('Digite o salário do funcionário: € '))

if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

novo_salario = salario + aumento

print(f'Novo salário com aumento: R$ {novo_salario:.2f}')
