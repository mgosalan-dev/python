"""
Exercício 036 - Empréstimo aprovado se prestação ≤ 30% do salário
"""
def main():
    valor_casa = float(input("Valor da casa: € "))
    salario = float(input("Salário: € "))
    anos = int(input("Anos para pagar: "))
    prestacao = valor_casa / (anos * 12)
    if prestacao <= salario * 0.3:
        print("Empréstimo aprovado!")
    else:
        print("Empréstimo negado!")

if __name__ == "__main__":
    main()
