# Exercício 29 - Radar eletrônico


velocidade = float(input('Qual a velocidade do carro (km/h)? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! 💸 Valor da multa: R$ {multa:.2f}')
else:
    print('Velocidade dentro do limite. 👍')
