import pygame
import sys
import numpy as np

# from pygame import event

pygame.init()

WIDTH = 600
HEIGHT = 600
# RGB = which means red green and blue // this colour came with trial & error
Light_lila = (190, 191, 255)
colour_of_line = (255, 255, 255)
size_of_line = 10
internal_board_rows = 3
internal_board_colm = 3
radios_of_circle = 70
width_of_circle = 12
circle_color = (255, 255, 255)
colour_of_X = (0, 0, 0)
empty_space = 55
width_of_cross = 25
square_size = WIDTH // internal_board_colm

# This is to start the display in the pygame setting the height and width to 600
Screen_board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" MAHMOUD TIC TAC TOE :)")
Screen_board.fill(Light_lila)

# Internal board numpy logic
board = np.zeros((internal_board_colm, internal_board_rows))


# print(board)

def drawing_of_lines():
    # drawing the 4 line of the game
    pygame.draw.line(Screen_board, colour_of_line, (square_size, 0), (square_size, HEIGHT), size_of_line)
    pygame.draw.line(Screen_board, colour_of_line, (2 * square_size, 0), (2 * square_size, HEIGHT), size_of_line)
    pygame.draw.line(Screen_board, colour_of_line, (0, square_size), (WIDTH, square_size), size_of_line)
    pygame.draw.line(Screen_board, colour_of_line, (0, 2 * square_size), (WIDTH, 2 * square_size), size_of_line)


def highlight_board(row, colm, Player):
    board[row][colm] = Player


def is_square_available(row, colm):
    return board[row][colm] == 0


def sketching_figures():
    for row in range(internal_board_rows):
        for colm in range(internal_board_colm):
            if board[row][colm] == 1:
                pygame.draw.circle(Screen_board, circle_color, (int(colm * square_size + square_size // 2), int(row * square_size + square_size // 2)),
                                   radios_of_circle, width_of_circle)

            elif board[row][colm] == 2:
                pygame.draw.line(Screen_board, colour_of_X, (colm * square_size + empty_space, row * square_size + square_size - empty_space),
                                 (colm * square_size + square_size - empty_space, row * square_size + empty_space), width_of_cross)
                pygame.draw.line(Screen_board, colour_of_X, (colm * square_size + empty_space, row * square_size + empty_space),
                                 (colm * square_size + square_size - empty_space, row * square_size + square_size - empty_space), width_of_cross)


def winner(Player):
    # the logic behind this is looping between the colm and rows and checking for the winner!
    for colm in range(internal_board_colm):
        if board[0][colm] == Player and board[1][colm] == Player and board[2][colm] == Player:
            sketch_vertical_line(colm, Player)
            return True

    for row in range(internal_board_rows):
        if board[row][0] == Player and board[row][1] == Player and board[row][2] == Player:
            sketch_horizontal_line(row, Player)
            return True

    if board[2][0] == Player and board[1][1] == Player and board[0][2] == Player:
        top_down_line(Player)
        return True

    if board[0][0] == Player and board[1][1] == Player and board[2][2] == Player:
        down_up_line(Player)
        return True

    return False


def sketch_vertical_line(colm, PLayer):
    position_X = colm * square_size + square_size // 2

    if PLayer == 1:
        colour = circle_color
    elif PLayer == 2:
        colour = colour_of_X
    pygame.draw.line(Screen_board, colour, (position_X, 15), (position_X, HEIGHT - 15), 15)


def sketch_horizontal_line(row, Player):
    position_Y = row * square_size + square_size // 2
    if Player == 1:
        colour = circle_color

    elif Player == 2:
        colour = colour_of_X
    pygame.draw.line(Screen_board, colour, (15, position_Y), (WIDTH - 15, position_Y), 15)


def top_down_line(Player):
    if Player == 1:
        colour = circle_color
    elif Player == 2:
        colour = colour_of_X

    pygame.draw.line(Screen_board, colour, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def down_up_line(Player):
    if Player == 1:
        colour = circle_color
    elif Player == 2:
        colour = colour_of_X

    pygame.draw.line(Screen_board, colour, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def is_my_board_full():
    for row in range(internal_board_rows):
        for colm in range(internal_board_colm):
            if board[row][colm] == 0:
                return False

        return True


def helper_function(row, colm):
    if board[row][colm] == 0:
        return True
    else:
        return False


print(helper_function(1, 1))


def restart_game():
    Screen_board.fill(Light_lila)
    drawing_of_lines()

    for row in range(internal_board_rows):
        for colm in range(internal_board_colm):
            board[row][colm] = 0


# this is for the positions taken by player 1 and 2 and empty take 0
drawing_of_lines()
Player = 1
game_done = False

# What this does are it allows the window to stay open instead of closing when running the code
# THIS IS ALSO THE MAIN LOOP :)

while True:
    for game in pygame.event.get():
        if game.type == pygame.QUIT:
            sys.exit()

        if game.type == pygame.MOUSEBUTTONDOWN and not game_done:
            mouseX = game.pos[0]  # this is for the X axis
            mouseY = game.pos[1]  # this is for the Y axis

            row_clicked = int(mouseY // square_size)
            colm_clicked = int(mouseX // square_size)

            if is_square_available(row_clicked, colm_clicked):
                if Player == 1:
                    highlight_board(row_clicked, colm_clicked, 1)
                    if winner(Player):
                        game_done = True
                    Player = 2
                elif Player == 2:
                    highlight_board(row_clicked, colm_clicked, 2)
                    if winner(Player):
                        game_done = True
                    Player = 1

                sketching_figures()

        if game.type == pygame.KEYDOWN:
            game_done = False
            if game.key == pygame.K_r:
                restart_game()

        # If you would like to quite the whole game press (q)
        if game.type == pygame.KEYDOWN:
            if game.key == pygame.K_q:
                quit()

    pygame.display.update()

# Quick side note if we win the game and want to restart the game I added the game_done = false However if we want
# the game not to restart after winning then we need to remove the and not game_done in the if statement,
# this depends on preference But I made it that you can restart the game as many times as you want without closing
# and opening the game from beginning which makes life easier.

"PLease check README file for sources used throughout the project !!!"
