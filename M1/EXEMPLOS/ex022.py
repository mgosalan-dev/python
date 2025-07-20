# ex022 - Manipulação de strings (nome)
# Desenvolvido com amor e café ☕ por um dev animado!

# Análise de nome com carinho: maiúsculo, minúsculo, tamanho...
nome = input("Digite seu nome completo: ").strip()
print("Maiúsculas:", nome.upper())
print("Minúsculas:", nome.lower())
print("Total de letras:", len(nome.replace(" ", "")))
print("Primeiro nome:", nome.split()[0])