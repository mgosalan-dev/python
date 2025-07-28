"""
Exercício 042 - Verifica e classifica triângulo
"""

def main():
    r1 = float(input("Primeiro segmento: "))
    r2 = float(input("Segundo segmento: "))
    r3 = float(input("Terceiro segmento: "))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print("Os segmentos PODEM formar um triângulo.")
        if r1 == r2 == r3:
            print("Triângulo Equilátero")
        elif r1 == r2 or r2 == r3 or r1 == r3:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print("Os segmentos NÃO podem formar um triângulo.")

if __name__ == "__main__":
    main()
