# Um clássico das aulas de Python: descubra quem vem antes e quem vem depois!

from colorama import init, Fore, Style

init(autoreset=True)

def main():
    try:
        n = int(input(Fore.CYAN + "Digite um número inteiro: " + Style.RESET_ALL))
        antecessor = n - 1
        sucessor = n + 1

        print(
            f"\n{Fore.CYAN}Analisando o número {Fore.GREEN}{n}{Fore.CYAN}, "
            f"seu antecessor é {Fore.BLUE}{antecessor}{Fore.CYAN} e o sucessor é {Fore.MAGENTA}{sucessor}{Style.RESET_ALL}."
        )
    except ValueError:
        print(Fore.RED + "Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
