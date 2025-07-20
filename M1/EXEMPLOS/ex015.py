# ex015 - Aluguel de carros
# Desenvolvido com amor e café ☕ por um dev animado!

# Táxi ou carro alugado? Vamos ver quanto custou.
dias = int(input("Quantos dias alugado? "))
km = float(input("Quantos km rodados? "))
total = dias * 60 + km * 0.15
print(f"O total a pagar é R${total:.2f}")