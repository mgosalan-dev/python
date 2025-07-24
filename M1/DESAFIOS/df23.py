# Df23 
def verificar_numero() -> int:
    
    while True:
        num = input("Digite um número inteiro de 0 a 9999: ").strip()

        if not num:
            print("Erro: o campo não pode estar vazio. Tente novamente.")
            continue

        if not num.isdigit():
            print("Erro: digite apenas números inteiros positivos.")
            continue

        return int(num)


def separador(num: int) -> None:
    """Exibe os dígitos de milhar, centena, dezena e unidade de um número."""
    print(f"Unidade: {num % 10}")
    print(f"Dezena: {(num // 10) % 10}")
    print(f"Centena: {(num // 100) % 10}")
    print(f"Milhar: {(num // 1000) % 10}")


def main():
    
    numero = verificar_numero()
    print("\n== Dígitos separados ==")
    separador(numero)


if __name__ == "__main__":
    main()
