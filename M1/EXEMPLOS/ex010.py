# ex010 - Conversor de moedas
# Desenvolvido com amor e café ☕ por um dev animado!

# De euro para real, dólar, bitcoin... mas aqui vamos usar um valor fixo só pra brincar.
real = float(input("Quanto você tem em R$? "))
dolar = real / 5.20
print(f"Com R${real:.2f}, você pode comprar US${dolar:.2f}")