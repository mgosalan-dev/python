# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

from colorama import init, Fore, Style

init(autoreset=True)

def celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def solicitar_temperatura() -> float:
    while True:
        try:
            return float(input(Fore.CYAN + "Informe a temperatura em °C: "))
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida! Por favor, digite um número válido.")

def main():
    print(Fore.YELLOW + Style.BRIGHT + "\n🌡️ Conversor de Temperatura - Celsius para Fahrenheit\n")
    celsius = solicitar_temperatura()
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(Fore.GREEN + f"\n{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F\n")

if __name__ == "__main__":
    main()
