# df34 calcular aumento de salario

def calcular_aumento(salario: float) -> float:
    if salario <= 1250:
        return salario * 0.15
    return salario * 0.10

def main():
    salario = float(input('Digite o salário do funcionário: € '))
    aumento = calcular_aumento(salario)
    novo_salario = salario + aumento

    print(f'Aumento: € {aumento:.2f}')
    print(f'Novo salário com aumento: € {novo_salario:.2f}')

if __name__ == '__main__':
    main()
