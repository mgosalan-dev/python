# ex018 - Seno, cosseno e tangente
# Desenvolvido com amor e café ☕ por um dev animado!

# Trigonometria, baby! Python resolve com a calculadora embutida.
from math import radians, sin, cos, tan
ang = float(input("Ângulo: "))
rad = radians(ang)
print(f"Seno: {sin(rad):.2f}")
print(f"Cosseno: {cos(rad):.2f}")
print(f"Tangente: {tan(rad):.2f}")