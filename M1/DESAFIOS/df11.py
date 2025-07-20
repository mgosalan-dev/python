# 🧱 Programa para calcular área da parede e quantidade de tinta necessária

# Entrada de dados
largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

# Cálculo da área
area = largura * altura

# Cálculo da quantidade de tinta (1 litro para cada 2m²)
tinta = area / 2

# Saída dos resultados
print(f"\n✅ A parede tem {area:.2f}m² de área.")
print(f"🖌️ Você precisará de {tinta:.2f} litros de tinta para pintá-la.")
