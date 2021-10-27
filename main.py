import pygame
from const import *

pygame.init()

pygame.display.set_caption("titre de l'app")
WIN = pygame.display.set_mode((WIN_LENGHT, WIN_HEIGHT), pygame.RESIZABLE)

RUNNING = True
pygame.mixer.init()
sound = pygame.mixer.music.load("test1.WAV")
pygame.mixer.music.play()
noise = pygame.mixer.Sound("test2.WAV")
noise.play().set_volume(0.0 , 1.0)
noise.play()
# boucle principale
while RUNNING:

    for event in pygame.event.get():

        # fermeture de la fenêtre
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()