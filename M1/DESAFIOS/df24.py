#df 24 verificar se a cidade se incia com Santo

def verificar_cidade() -> str:
    
    while True:
        cidade = input("Digite o nome da cidade: ").strip()
        if cidade == "":
            print("Erro: o campo não pode estar vazio.")
        else:
            return cidade


def verificar_santo(cidade: str) -> None:
    """Verifica se a cidade começa com 'Santo' (ignorando maiúsculas/minúsculas)."""
    if cidade.lower().startswith("santo"):
        print(f"A cidade começa com 'Santo': {cidade}")
    else:
        print(f"A cidade não começa com 'Santo': {cidade}")


def main():
    cidade = verificar_cidade()
    verificar_santo(cidade)


if __name__ == "__main__":
    main()
