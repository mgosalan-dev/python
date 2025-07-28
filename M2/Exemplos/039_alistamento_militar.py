"""
Exercício 039 - Alistamento militar baseado no ano de nascimento
"""

from datetime import date

def main():
    ano = int(input("Ano de nascimento: "))
    idade = date.today().year - ano
    if idade < 18:
        print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    elif idade == 18:
        print("Você deve se alistar este ano!")
    else:
        print(f"Você já deveria ter se alistado há {idade - 18} anos.")

if __name__ == "__main__":
    main()
