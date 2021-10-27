import pygame
import time

files = ["test1.ogg", "test2.ogg"]
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("test1.ogg")
stop_point = 0.0
stop = stop_point
onplay = True
while onplay:
    player_input = input("> ")
    if player_input == "pause":
        stop_point += pygame.mixer.music.get_pos() / 1000.0 - 0.1
        print(stop_point)
        stop = stop_point
        pygame.mixer.music.stop()
    elif player_input == "play":
        pygame.mixer.music.play()
        pygame.mixer.music.set_pos(stop)
        print(stop_point)
    elif player_input == "stop":
        pygame.mixer.music.stop()
        onplay = False

