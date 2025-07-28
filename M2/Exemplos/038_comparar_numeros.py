"""
Exercício 038 - Maior e menor de três números
"""

def main():
    a = float(input("1º número: "))
    b = float(input("2º número: "))
    c = float(input("3º número: "))
    print(f"Maior: {max(a, b, c)}")
    print(f"Menor: {min(a, b, c)}")

if __name__ == "__main__":
    main()
