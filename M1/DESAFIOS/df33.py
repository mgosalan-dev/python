# df 33 verificação de maior e de menor 

def ler_numero(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def main():
    a = ler_numero("Digite o primeiro número: ")
    b = ler_numero("Digite o segundo número: ")
    c = ler_numero("Digite o terceiro número: ")

    maior = max(a, b, c)
    menor = min(a, b, c)

    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

if __name__ == "__main__":
    main()
