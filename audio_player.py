import pygame
import time

files = ["test1.ogg", "test2.ogg"]

pygame.init()
pygame.mixer.init()
stepper = 0

#file loading
while stepper < len(files):
    pygame.mixer.music.load(files[stepper])
    print("Playing:",files[stepper])
    stepper += 1
    pygame.mixer.music.play()
#play and pause
    while pygame.mixer.music.get_busy():
        timer = pygame.mixer.music.get_pos()
        control = input()
        pygame.time.Clock().tick(10)
        if control == "pause":
            timee = pygame.mixer.music.get_pos()/1000.0
            pygame.mixer.music.stop()
        elif control == "play":
            pygame.mixer.music.play()
            pygame.mixer.music.set_pos(timee)
        elif control == "time":
            timer = pygame.mixer.music.get_pos()
            timer = timer/1000
            print(str(timer))

        else:
            continue
