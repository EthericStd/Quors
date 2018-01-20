import pygame.display
from constants import *

pygame.init()
class Display:
    def __init__(self, width, height):
        self.root = pygame.display.set_mode( (width, height) )
        self.canvas = []

    def addCanvas(self, canvas):
        self.canvas += [canvas]

    def display(self):
        for canvas in self.canvas:
            canvas.blitAll()
            self.root.blit(canvas.surface, (canvas.x, canvas.y) )
        pygame.display.flip()
