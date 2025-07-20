# ex004 - Tipos primitivos
# Desenvolvido com amor e café ☕ por um dev animado!

# Vamos mostrar que Python sabe o tipo de cada coisa. Ele não julga, só classifica.
n = input("Digite algo: ")
print("É número?", n.isnumeric())
print("É alfabético?", n.isalpha())
print("É alfanumérico?", n.isalnum())
print("Está em maiúsculas?", n.isupper())