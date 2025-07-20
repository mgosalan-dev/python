from colorama import init, Fore, Style
from math import hypot

init(autoreset=True)

def ler_float(cor, mensagem):
    while True:
        try:
            return float(input(cor + mensagem))
        except ValueError:
            print(Fore.RED + "❌ Não pode ficar vazio ou conter letras.")

def ler_cateto_adjacente():
    return ler_float(Fore.MAGENTA, "Digite o valor do Cateto Adjacente: ")

def ler_cateto_oposto():
    return ler_float(Fore.CYAN, "Digite o valor do Cateto Oposto: ")

def calcular_hipotenusa(ca, co):
    return hypot(ca, co)

def main():
    ca = ler_cateto_adjacente()
    co = ler_cateto_oposto()

    print(Fore.MAGENTA + f"\nAnalisando o Cateto Adjacente: {ca}{Style.RESET_ALL}")
    print(Fore.CYAN + f"Analisando o Cateto Oposto: {co}{Style.RESET_ALL}")
    
    total = calcular_hipotenusa(ca, co)

    print(Fore.YELLOW + f"\nA hipotenusa calculada é: {Style.BRIGHT}{total:.2f}")

if __name__ == "__main__":
    main()
