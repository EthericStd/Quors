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
    cav = Canvas(root, 0, 0, 1200, 675)


    #character
    cav.add_rectangle(root_width//2, root_height//2, 50, 100, "character", (255,128,0))

    #wall
    cav.add_rectangle(root_width//2-100, root_height//2, 70, 70, "wall", (0,128,255))


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

            root.refresh()

pygame.quit()
