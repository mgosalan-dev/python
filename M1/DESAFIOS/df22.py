# df022 - Manipulação de strings (nome)

def verificar_nome():
    while True:
        nome = input("Digite seu nome: ").strip()
        if nome == "":
            print("⚠️ Nome inválido. Tente novamente.")
        else:
            return nome

def exibir_informacoes(nome):
    
    print(f"\n✅ O seu nome é: {nome}")
    print("🔠 Maiúsculas:", nome.upper())
    print("🔡 Minúsculas:", nome.lower())
    print("🔢 Total de letras (sem espaços):", len(nome.replace(" ", "")))
    print("👤 Primeiro nome:", nome.split()[0])

def main():
    
    nome = verificar_nome()
    exibir_informacoes(nome)

if __name__ == "__main__":
    main()
