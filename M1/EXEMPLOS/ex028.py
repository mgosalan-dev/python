# Exercício 28 - Jogo da Adivinhação v1.0
# Resolução básica e didática

import random

print('Jogo da Adivinhação 🎲')
numero_sorteado = random.randint(0, 5)
palpite = int(input('Tente adivinhar o número de 0 a 5: '))

if palpite == numero_sorteado:
    print('Parabéns! Você acertou! 🎉')
else:
    print(f'Errou! O número era {numero_sorteado}. Tente de novo!')
