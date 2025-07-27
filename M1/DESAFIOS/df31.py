# df31 - Cálculo do custo da viagem

def calcular_valor_viagem(km: float) -> float:
    """Calcula o valor da viagem com base nos km rodados."""
    if km >= 200:
        return km * 0.50
    else:
        return km * 0.45

def obter_kilometragem() -> float:
    """Solicita ao usuário a quantidade de km com validação."""
    while True:
        try:
            km = float(input("Digite os kms rodados: ").strip())
            if km < 0:
                print("❌ A quilometragem não pode ser negativa. Tente novamente.")
                continue
            return km
        except ValueError:
            print("❌ Entrada inválida! Digite um número válido.")

def main():
    km_rodados = obter_kilometragem()
    valor = calcular_valor_viagem(km_rodados)
    print(f"💸 O valor da viagem é de R$ {valor:.2f}")

if __name__ == "__main__":
    main()
