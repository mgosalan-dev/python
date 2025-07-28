"""
Exercício 040 - Média e situação escolar
"""

def main():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    if media >= 7:
        print(f"Aprovado com média {media:.1f}")
    elif media >= 5:
        print(f"Recuperação com média {media:.1f}")
    else:
        print(f"Reprovado com média {media:.1f}")

if __name__ == "__main__":
    main()
