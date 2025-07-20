# ex021 - Reproduzir áudio com pygame
# Desenvolvido com amor e café ☕ por um dev animado!

# DJ Python na área. Toque seu som!
import pygame
pygame.init()
pygame.mixer.music.load("seuarquivo.mp3")
pygame.mixer.music.play()
input("Pressione enter para parar...")