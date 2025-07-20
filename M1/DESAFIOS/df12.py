# 💸 Calcula o valor de um produto com 5% de desconto
from colorama import init, Fore, Style

# Inicializa o colorama (necessário no Windows)
init(autoreset=True)


def calcular_desconto(valor: float) -> float:
    """
    Calcula e retorna o valor com 5% de desconto.
    """
    return valor * 0.95


def solicitar_valor_produto() -> float:
    """
    Solicita ao usuário o valor do produto e valida a entrada.
    """
    while True:
        try:
            valor = float(input(Fore.CYAN + "Digite o valor do produto (€): "))
            if valor < 0:
                print(Fore.RED + "❌ O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Digite apenas números (use ponto para decimais).")


def main():
    print(Fore.YELLOW + Style.BRIGHT + "\n🧾 Calculadora de Desconto - 5% OFF\n" + Style.RESET_ALL)

    produto = solicitar_valor_produto()
    valor_com_desconto = calcular_desconto(produto)

    print(
        Fore.GREEN + f"\n💰 O produto que custava €{produto:.2f} agora custa €{valor_com_desconto:.2f} com 5% de desconto.\n"
    )


if __name__ == "__main__":
    main()
