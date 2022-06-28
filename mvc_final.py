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
mouseY = 200
mouseX = 200
circle_color = (255, 255, 255)
colour_of_X = (0, 0, 0)
empty_space = 55
width_of_cross = 25

# This is to start the display in the pygame setting the height and width to 600
Screen_board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" MAHMOUD TIC TAC TOE :)")
Screen_board.fill(Light_lila)


# Model
class Model:
    def __init__(self):
        self.board = np.zeros((internal_board_colm, internal_board_rows))

    def highlight_board(self, row, colm, Player):
        self.board[row][colm] = Player

    def is_square_available(self, row, colm):
        return self.board[row][colm] == 0

    def is_my_board_full(self):
        for row in range(internal_board_rows):
            for colm in range(internal_board_colm):
                if self.board[row][colm] == 0:
                    return False
        return True


# View
class View:

    def drawing_of_lines(self):
        Screen_board.fill(Light_lila)
        # drawing the 4 line of the game
        pygame.draw.line(Screen_board, colour_of_line, (0, 200), (600, 200), size_of_line)
        pygame.draw.line(Screen_board, colour_of_line, (0, 400), (600, 400), size_of_line)
        pygame.draw.line(Screen_board, colour_of_line, (200, 0), (200, 600), size_of_line)
        pygame.draw.line(Screen_board, colour_of_line, (400, 0), (400, 600), size_of_line)

    @staticmethod
    def sketching_figures(board):

        for row in range(internal_board_rows):
            for colm in range(internal_board_colm):
                if board[row][colm] == 1:
                    pygame.draw.circle(Screen_board, circle_color, (int(colm * 200 + 100), int(row * 200 + 100)),
                                       radios_of_circle, width_of_circle)

                elif board[row][colm] == 2:
                    pygame.draw.line(Screen_board, colour_of_X,
                                     (colm * 200 + empty_space, row * 200 + 200 - empty_space),
                                     (colm * 200 + 200 - empty_space, row * 200 + empty_space), width_of_cross)
                    pygame.draw.line(Screen_board, colour_of_X, (colm * 200 + empty_space, row * 200 + empty_space),
                                     (colm * 200 + 200 - empty_space, row * 200 + 200 - empty_space), width_of_cross)

    @staticmethod
    def sketch_vertical_line(colm, Player):
        position_X = colm * 200 + 100

        if Player == 1:
            colour = circle_color
        elif Player == 2:
            colour = colour_of_X
        pygame.draw.line(Screen_board, colour, (position_X, 15), (position_X, HEIGHT - 15), 15)

    @staticmethod
    def sketch_horizontal_line(row, Player):
        position_Y = row * 200 + 100
        if Player == 1:
            colour = circle_color

        elif Player == 2:
            colour = colour_of_X
        pygame.draw.line(Screen_board, colour, (15, position_Y), (WIDTH - 15, position_Y), 15)

    @staticmethod
    def top_down_line(Player):
        if Player == 1:
            colour = circle_color
        elif Player == 2:
            colour = colour_of_X

        pygame.draw.line(Screen_board, colour, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

    @staticmethod
    def down_up_line(Player):
        if Player == 1:
            colour = circle_color
        elif Player == 2:
            colour = colour_of_X

        pygame.draw.line(Screen_board, colour, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

    def restart_game(self, board):
        Screen_board.fill(Light_lila)
        self.drawing_of_lines()
        for row in range(internal_board_rows):
            for colm in range(internal_board_colm):
                board[row][colm] = 0


# controller
class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()


    def winner(self, Player):
        for colm in range(internal_board_colm):
            if self.model.board[0][colm] == Player and self.model.board[1][colm] == Player and self.model.board[2][colm] == Player:
                self.view.sketch_vertical_line(colm, Player)
                return True

        for row in range(internal_board_rows):
            if self.model.board[row][0] == Player and self.model.board[row][1] == Player and self.model.board[row][2] == Player:
                self.view.sketch_horizontal_line(row, Player)
                return True

        if self.model.board[2][0] == Player and self.model.board[1][1] == Player and self.model.board[0][2] == Player:
            self.view.top_down_line(Player)
            return True

        if self.model.board[0][0] == Player and self.model.board[1][1] == Player and self.model.board[2][2] == Player:
            self.view.down_up_line(Player)
            return True

        return False


def main_loop():
    Player = 1
    game2 = Controller()
    game2.view.drawing_of_lines()
    game_done = False
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_done:
                mouseX = event.pos[0]  # this is for the X axis
                mouseY = event.pos[1]  # this is for the Y axis

                row_clicked = int(mouseY // 200)
                colm_clicked = int(mouseX // 200)

                if game2.model.is_square_available(row_clicked, colm_clicked):

                    if Player == 1:
                        game2.model.highlight_board(row_clicked, colm_clicked, 1)
                        if game2.winner(Player):
                            game_done = True
                        Player = 2
                    elif Player == 2:
                        game2.model.highlight_board(row_clicked, colm_clicked, 2)
                        if game2.winner(Player):
                            game_done = True
                        Player = 1

                    game2.view.sketching_figures(game2.model.board)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game2.view.restart_game(game2.model.board)
                    game_done = False

                # If you would like to quite the whole game press (q)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()

        pygame.display.update()


if __name__ == "__main__":
    main_loop()
    
"PLease check README file for sources used throughout the project !!!"
