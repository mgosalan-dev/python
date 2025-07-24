def verificar_frase() -> str:
    
    while True:
        frase = input("Digite algo no teclado: ").strip()
        if frase == "":
            print("O campo não pode estar vazio.")
        else:
            return frase


def verificar_a(frase: str) -> None:
    
    frase_lower = frase.lower()
    
    if "a" in frase_lower:
        print(f"\nFrase: {frase}")
        print(f"Quantidade de 'a': {frase_lower.count('a')}")
        print(f"Primeira posição de 'a': {frase_lower.find('a') + 1}")
        print(f"Última posição de 'a': {frase_lower.rfind('a') + 1}")
    else:
        print("\nA letra 'a' não foi encontrada na frase.")


def main():
    frase = verificar_frase()
    verificar_a(frase)


if __name__ == "__main__":
    main()
