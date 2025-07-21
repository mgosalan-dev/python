# ex018 - Seno, Cosseno e Tangente

from math import radians, sin, cos, tan
from colorama import init, Fore, Style

init(autoreset=True)

def obter_angulo():
    while True:
        try:
            return float(input(Fore.CYAN + "Digite o ângulo em graus: "))
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Por favor, digite um número válido.")

def mostrar_trigonometria(angulo):
    rad = radians(angulo)
    seno = sin(rad)
    cosseno = cos(rad)
    tangente = tan(rad)

    print(Style.BRIGHT + Fore.MAGENTA + f"\nAnalisando o ângulo de {angulo}°:")
    print(Fore.GREEN + f"Seno:     {seno:.2f}")
    print(Fore.BLUE + f"Cosseno:  {cosseno:.2f}")
    print(Fore.YELLOW + f"Tangente: {tangente:.2f}")

def main():
    angulo = obter_angulo()
    mostrar_trigonometria(angulo)

if __name__ == "__main__":
    main()
