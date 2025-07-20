# ex020 - Ordem aleatória
# Desenvolvido com amor e café ☕ por um dev animado!

# Aleatoriedade total. Quem apresenta primeiro?
import random
nomes = [input("Nome 1: "), input("Nome 2: "), input("Nome 3: "), input("Nome 4: ")]
random.shuffle(nomes)
print("Ordem de apresentação:", nomes)