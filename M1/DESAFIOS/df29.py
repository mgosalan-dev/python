#29 calcular multar de transito

def calcular_multa(velocidade: int) -> float:
    LIMITE = 60
    return (velocidade - LIMITE) * 7 if velocidade > LIMITE else 0.0


def solicitar_velocidade() -> int:
    while True:
        try:
            return int(input("Qual é a sua velocidade? "))
        except ValueError:
            print("⚠️ Digite apenas números inteiros, por favor.")


def main():
    velocidade = solicitar_velocidade()
    multa = calcular_multa(velocidade)

    if multa > 0:
        print(f"🚨 Você foi multado! Valor da multa: {multa:.2f}€")
    else:
        print("✅ Velocidade dentro do limite. Dirija com segurança!")


if __name__ == "__main__":
    main()
