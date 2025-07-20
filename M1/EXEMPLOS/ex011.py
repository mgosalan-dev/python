# ex011 - Tinta para parede
# Desenvolvido com amor e café ☕ por um dev animado!

# Calculadora de pintura! Cada litro cobre 2m². Não erre nas contas!
larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
tinta = area / 2
print(f"Sua parede tem {area}m² e vai precisar de {tinta}L de tinta")