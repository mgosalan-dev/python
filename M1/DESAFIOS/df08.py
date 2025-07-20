# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

from colorama import init, Fore, Style

# Inicializa o colorama para que as cores funcionem no terminal
init(autoreset=True)

def obter_valor(valor):
    while True:
        try:
            return float(input(Fore.CYAN + f"Digite um valor em {valor}: "))
        except ValueError:
            print(Fore.RED + "🚫 Digite um valor numérico válido!")

def main():
    print(Fore.YELLOW + "\n📏 Conversor de Unidades de Comprimento (Sistema Métrico)\n")

    metros = obter_valor("metros")  

    # Conversões
    milimetros = metros * 1_000
    centimetros = metros * 100
    decimetros = metros * 10
    decametros = metros / 10
    hectometros = metros / 100
    quilometros = metros / 1_000
    miriametros = metros / 10_000

    micrometros = metros * 1_000_000
    nanometros = metros * 1_000_000_000
    picometros = metros * 1_000_000_000_000

    print(f"\n👉 {Fore.MAGENTA}{metros}{Style.RESET_ALL} metro(s) equivale a:\n")

    print(f"📎 {Fore.YELLOW}{milimetros:.2f}{Style.RESET_ALL} milímetros (mm)")
    print(f"📎 {Fore.YELLOW}{centimetros:.2f}{Style.RESET_ALL} centímetros (cm)")
    print(f"📎 {Fore.YELLOW}{decimetros:.2f}{Style.RESET_ALL} decímetros (dm)")
    print(f"📎 {Fore.YELLOW}{decametros:.5f}{Style.RESET_ALL} decâmetros (dam)")
    print(f"📎 {Fore.YELLOW}{hectometros:.5f}{Style.RESET_ALL} hectômetros (hm)")
    print(f"📎 {Fore.YELLOW}{quilometros:.5f}{Style.RESET_ALL} quilômetros (km)")
    print(f"📎 {Fore.YELLOW}{miriametros:.5f}{Style.RESET_ALL} miriametros (mam)\n")

    print("🔬 Medidas menores que o metro:\n")
    print(f"📎 {Fore.CYAN}{micrometros:.0f}{Style.RESET_ALL} micrômetros (µm)")
    print(f"📎 {Fore.CYAN}{nanometros:.0f}{Style.RESET_ALL} nanômetros (nm)")
    print(f"📎 {Fore.CYAN}{picometros:.0f}{Style.RESET_ALL} picômetros (pm)\n")

    print(Fore.GREEN + "✅ Conversão concluída com sucesso!\n")

if __name__ == "__main__":
    main()
