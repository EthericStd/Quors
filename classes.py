import pygame
from pygame.locals import *
from constants import *
import os

pygame.init()

#z-index with tag (order of the add of tag)














class KeyMice:
    def __init__(self, perso):
        self.perso = perso

    def processing(self, event):
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.perso.add_velocity(0, -5)
            elif event.key == K_a:
                self.perso.add_velocity(-5, 0)
            elif event.key == K_s:
                self.perso.add_velocity(0, 5)
            elif event.key == K_d:
                self.perso.add_velocity(5, 0)
        if event.type == MOUSEBUTTONDOWN:
            pass

class Fonts:
    def __init__(self):
        self.list=[os.path.join("fonts",file) for file in os.listdir("fonts")]

    def get_class(self, index, size):
        return pygame.font.Font(self.list[index], size)
