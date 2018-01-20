import pygame
from pygame.locals import *
from constants import *
from Display import *
from Canvas import *
###CONSTANTS###


###FUNCTIONS###

###TESTS###
if __name__=="__main__":
    #init
    pygame.init()
    
    #classes
    root = Display(root_width, root_height)
    cav = Canvas(root, 0, 0, 600, 675)
    cav2 = Canvas(root, 600, 0, 600, 675)

    #background
    background = pygame.Surface( (root_width, root_height) )
    background.fill((230,230,230))
    cav.add(background, 0 ,0, "background")

    #character
    character = pygame.Surface( (50,100) )
    character.fill((255,128,0))
    cav.add(character, root_width//2, root_height//2, "character")

    #wall
    wall = pygame.Surface( (70,70) )
    wall.fill((0,128,255))
    cav.add(wall, root_width//2-100, root_height//2, "wall")


    #key repeat
    pygame.key.set_repeat(1,16)

    #variables
    position = "game"
    principal_loop = True

    while principal_loop:
        while position == "game":
            pygame.time.Clock().tick(timer_clock)
            for event in pygame.event.get():
                if event.type == QUIT:
                    principal_loop = False
                    position = None

            root.display()

pygame.quit()
