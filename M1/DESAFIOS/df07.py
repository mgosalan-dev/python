from colorama import init, Fore, Style

# Inicializa o colorama (para que as cores funcionem no terminal)
init(autoreset=True)

def obter_nota(periodo):
    while True:
        try:
            nota = float(input(Fore.CYAN + f"Digite a nota do {periodo}: " + Style.RESET_ALL))
            if 0 <= nota <= 20:
                return nota
            else:
                print(Fore.RED + "A nota deve estar entre 0 e 20.")
        except ValueError:
            print(Fore.RED + "Por favor, digite um número válido.")

def main():
    print(Fore.YELLOW + "\n📘 Cálculo de Média Final (Ensino Secundário - Portugal)\n" + Style.RESET_ALL)

    notas = [
        obter_nota("1.º Período"),
        obter_nota("2.º Período"),
        obter_nota("3.º Período")
    ]

    media = sum(notas) / len(notas)

    print(f"\n{Fore.GREEN}Notas informadas: {notas}")
    print(f"{Fore.BLUE}Média final: {media:.2f}")

    if media >= 18:
        print(Fore.GREEN + "🎉 Excelente! Aprovado com distinção!")
    elif media >= 10:
        print(Fore.YELLOW + "✅ Aprovado! Bom trabalho.")
    else:
        print(Fore.RED + "❌ Reprovado. Não desanimes, continua a tentar!")

if __name__ == "__main__":
    main()
