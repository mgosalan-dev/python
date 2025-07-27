# Exercício 31 - Custo da Viagem
# Resolução básica e didática

distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço da passagem é R$ {preco:.2f}')
