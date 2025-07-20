# ex006 - Crie um Algoritimo que leia um número e mostre seu dobro, triplo e a sua raiz quadrada

from colorama import init, Fore, Style
from math import sqrt

# Inicializa o colorama (para dar cores no terminal do Windows/macOS/Linux)
init(autoreset=True)

def main():
    try:
        numero = float(input(Fore.CYAN + "Digite um número: " + Style.RESET_ALL))

        dobro = numero * 2
        triplo = numero * 3
        raiz = sqrt(numero)

        print(f"\n{Fore.YELLOW}Resultados para o número {Fore.GREEN}{numero}{Fore.YELLOW}:")
        print(f"➡ Dobro: {Fore.BLUE}{dobro}")
        print(f"➡ Triplo: {Fore.MAGENTA}{triplo}")
        print(f"➡ Raiz Quadrada: {Fore.RED}{raiz:.2f}")

    except ValueError:
        print(Fore.RED + "Epa! Isso não parece um número válido. Tenta de novo 😉")

if __name__ == "__main__":
    main()
