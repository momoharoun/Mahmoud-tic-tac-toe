import sys

import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
# RGB = which means red green and blue // this colour came with trial & error
Light_lila = (190, 191, 255)

# This is to start the display in the pygame setting the height and width to 500
Screen_board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" MAHMOUD TIC TAC TOE :)")
Screen_board.fill(Light_lila)

# What this does are it allows the window to stay open instead of closing when running the code
# This is also the main loop !!
while True:
    for game in pygame.event.get():
        if game.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
