#df 28 escolha de numero aleatorio

import random

def sortear_numero():
    return random.randint(0, 5)

def validar_escolha(maquina):
    while True:
        try:
            jogador = int(input("Escolha um valor de 0 a 5: "))
        except ValueError:
            print("⚠️ Digite apenas números, amigão!")
            continue

        if jogador < 0 or jogador > 5:
            print("❌ Valor inválido! Escolha entre 0 e 5.")
            continue
        break

    if jogador == maquina:
        print("🎉 Parabéns! Você acertou!!!")
    else:
        print(f"😢 Você errou! O número certo era {maquina}.")

def main():
    while True:
        aleatorio = sortear_numero()
        validar_escolha(aleatorio)

if __name__ == "__main__":
    main()
