# df32 verificar se um ano é bissexto

def verificar_ano_bissexto(ano: int) -> bool:
    """Verifica se o ano é bissexto"""
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def obter_ano() -> int:
    """Solicita um ano válido ao usuário"""
    while True:
        try:
            ano = int(input("Digite o ano que quer verificar: ").strip())
            if ano <= 0:
                print("❌ Ano inválido. Digite um valor positivo.")
                continue
            return ano
        except ValueError:
            print("❌ É permitido apenas números inteiros.")

def main():
    ano = obter_ano()
    if verificar_ano_bissexto(ano):
        print(f"✅ O ano de {ano} é **bissexto**.")
    else:
        print(f"❌ O ano de {ano} **não é bissexto**.")

if __name__ == "__main__":
    main()
