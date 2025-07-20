# ex026 - Análise de frase
# Desenvolvido com amor e café ☕ por um dev animado!

# Contador de letras e posições de 'A'. Muito útil pra... sei lá, mas é legal!
frase = input("Digite uma frase: ").strip().lower()
print("Quantidade de 'a':", frase.count("a"))
print("Primeira posição de 'a':", frase.find("a") + 1)
print("Última posição de 'a':", frase.rfind("a") + 1)