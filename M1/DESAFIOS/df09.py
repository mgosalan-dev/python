# Faça um programa que leia um numero interio qualquer e mostre a sua tábuada

from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

def obter_valor():
    while True:
        try:
            return int(input(Fore.CYAN + "Digite um número inteiro para ver sua tabuada: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Por favor, digite um número inteiro.")

def main():
    valor = obter_valor()
    
    print(Fore.YELLOW + f"\n📘 Tabuada do {valor}\n" + Style.RESET_ALL)
    
    for i in range(1, 11):
        print(Fore.GREEN + f"{valor} x {i} = {valor * i}")

if __name__ == "__main__":
    main()