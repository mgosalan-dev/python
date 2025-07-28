"""
Exercício 041 - Classificação de atletas por idade
"""

from datetime import date

def main():
    ano = int(input("Ano de nascimento do atleta: "))
    idade = date.today().year - ano
    if idade <= 9:
        categoria = "Mirim"
    elif idade <= 14:
        categoria = "Infantil"
    elif idade <= 19:
        categoria = "Junior"
    elif idade <= 25:
        categoria = "Sênior"
    else:
        categoria = "Master"
    print(f"Categoria: {categoria}")

if __name__ == "__main__":
    main()
