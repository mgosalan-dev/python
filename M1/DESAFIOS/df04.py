# crie um Script que leia um valor um mostre todas as informações sobre ele 



from colorama import init, Fore, Style

# Inicializa o colorama no Windows
init(autoreset=True)

valor = input(f"{Fore.CYAN}Digite algo: ")

print(Fore.YELLOW + "-" * 50)
print(f"{Fore.GREEN}Tipo primitivo: {Fore.WHITE}{type(valor)}")
print(f"{Fore.GREEN}Só tem espaços? {Fore.WHITE}{valor.isspace()}")
print(f"{Fore.GREEN}É um número? {Fore.WHITE}{valor.isnumeric()}")
print(f"{Fore.GREEN}É alfabético? {Fore.WHITE}{valor.isalpha()}")
print(f"{Fore.GREEN}É alfanumérico? {Fore.WHITE}{valor.isalnum()}")
print(f"{Fore.GREEN}Está em maiúsculas? {Fore.WHITE}{valor.isupper()}")
print(f"{Fore.GREEN}Está em minúsculas? {Fore.WHITE}{valor.islower()}")
print(f"{Fore.GREEN}Está capitalizado? {Fore.WHITE}{valor.istitle()}")
print(Fore.YELLOW + "-" * 50)

print(Style.DIM + Fore.MAGENTA + "Análise finalizada com sucesso! 🚀")
