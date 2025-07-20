# ex023 - Separar dígitos de um número
# Desenvolvido com amor e café ☕ por um dev animado!

# Quebrando o número em unidades, dezenas, centenas...
num = int(input("Digite um número entre 0 e 9999: "))
print("Unidade:", num % 10)
print("Dezena:", (num // 10) % 10)
print("Centena:", (num // 100) % 10)
print("Milhar:", (num // 1000) % 10)