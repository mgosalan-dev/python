# ex019 - Escolha aleatória
# Desenvolvido com amor e café ☕ por um dev animado!

# Quem vai apagar o quadro? Python decide por sorteio!
import random
nomes = [input("Nome 1: "), input("Nome 2: "), input("Nome 3: "), input("Nome 4: ")]
print("Escolhido:", random.choice(nomes))