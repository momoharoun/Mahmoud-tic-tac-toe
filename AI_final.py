import sys
import pygame
import numpy as np
import copy
import random


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
square_size = WIDTH // internal_board_colm
space = square_size // 3
# This is to start the display in the pygame setting the height and width to 600
Screen_board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" MAHMOUD TIC TAC TOE :)")
Screen_board.fill(Light_lila)


class Model:
    def __init__(self):
        self.boxes = np.zeros((internal_board_rows, internal_board_colm))
        self.empty_boxes = self.boxes  # boxes
        self.highlighted_boxes = 0

    def final_state(self, show=False):
        # This is for the vertical wins
        for col in range(internal_board_colm):
            if self.boxes[0][col] == self.boxes[1][col] == self.boxes[2][col] != 0:
                if show:
                    colour = circle_color if self.boxes[0][col] == 2 else colour_of_X
                    starting_position = (col * square_size + square_size // 2, 20)
                    ending_position = (col * square_size + square_size // 2, HEIGHT - 20)
                    pygame.draw.line(Screen_board, colour, starting_position, ending_position, size_of_line)
                return self.boxes[0][col]

        # This is for the horizontal wins
        for row in range(internal_board_rows):
            if self.boxes[row][0] == self.boxes[row][1] == self.boxes[row][2] != 0:
                if show:
                        colour = circle_color if self.boxes[row][0] == 2 else colour_of_X
                        starting_position = (20, row * square_size + square_size // 2)
                        ending_position = (WIDTH - 20, row * square_size + square_size // 2)
                        pygame.draw.line(Screen_board, colour, starting_position, ending_position, size_of_line)
                return self.boxes[row][0]

        # This is for the top down wins
        if self.boxes[0][0] == self.boxes[1][1] == self.boxes[2][2] != 0:
            if show:
                colour = circle_color if self.boxes[1][1] == 2 else colour_of_X
                starting_position = (20, 20)
                ending_position = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(Screen_board, colour, starting_position, ending_position, size_of_line)
                return self.boxes[1][1]

        # This is for the down up  wins
        if self.boxes[2][0] == self.boxes[1][1] == self.boxes[0][2] != 0:
                if show:
                    colour = circle_color if self.boxes[1][1] == 2 else colour_of_X
                    starting_position = (20, HEIGHT - 20)
                    ending_position = (WIDTH - 20, 20)
                    pygame.draw.line(Screen_board, colour, starting_position, ending_position, size_of_line)
                return self.boxes[1][1]

        return 0

    def mark_boxes(self, row, col, player):
        self.boxes[row][col] = player
        self.highlighted_boxes += 1

    def empty_box(self, row, col):
        return self.boxes[row][col] == 0

    def get_empty_boxes(self):
        empty_boxes = []
        for row in range(internal_board_rows):
            for col in range(internal_board_colm):
                if self.empty_box(row, col):
                    empty_boxes.append((row, col))

        return empty_boxes

    def board_full(self):
        return self.highlighted_boxes == 9

    def board_empty(self):
        return self.highlighted_boxes == 0


class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    # Random AI
    def random(self, board):
        empty_board = board.get_empty_boxes()
        idx = random.randrange(0, len(empty_board))

        return empty_board[idx]  # FOR (row, col)

    # Minimax AI
    def minimax_ai(self, board, maximizing):
        # terminal case
        case = board.final_state()

        # player 1 wins
        if case == 1:
            return 1, None  # evaluation, move
        # this is when player 2 wins (the AI)
        if case == 2:
            return -1, None
        # draw, when there is no winner found
        elif board.board_full():
            return 0, None

        if maximizing:
            max_evaluation = -100
            best_move = None
            empty_boxes = board.get_empty_boxes()

            for (row, col) in empty_boxes:
                temp_board = copy.deepcopy(board)
                temp_board.mark_boxes(row, col, 1)
                evaluation = self.minimax_ai(temp_board, False)[0]
                if evaluation > max_evaluation:
                    max_evaluation = evaluation
                    best_move = (row, col)

            return max_evaluation, best_move

        elif not maximizing:
            min_evaluation = 100
            best_move = None
            empty_board = board.get_empty_boxes()

            for (row, col) in empty_board:
                temp_board = copy.deepcopy(board)
                temp_board.mark_boxes(row, col, self.player)
                evaluation = self.minimax_ai(temp_board, True)[0]
                if evaluation < min_evaluation:
                    min_evaluation = evaluation
                    best_move = (row, col)

            return min_evaluation, best_move

    def evaluation(self, main_board):
        if self.level == 0:
            # The random choice
            evaluation = 'random'
            move = self.random(main_board)
        else:
            # The minimax algorithm choice
            evaluation, move = self.minimax_ai(main_board, False)

        print(f'AI has chosen to mark the square in position {move} with an evaluation of: {evaluation}')

        return move  # row, col


class View:
    @staticmethod
    def drawing_of_lines():
        Screen_board.fill(Light_lila)
        # drawing the 4 line of the game
        pygame.draw.line(Screen_board, colour_of_line, (0, 200), (600, 200), size_of_line)
        pygame.draw.line(Screen_board, colour_of_line, (0, 400), (600, 400), size_of_line)
        pygame.draw.line(Screen_board, colour_of_line, (200, 0), (200, 600), size_of_line)
        pygame.draw.line(Screen_board, colour_of_line, (400, 0), (400, 600), size_of_line)

    @staticmethod
    def draw_figures(row, col, player):
        if player == 1:
            # drawing of the X
            start_desc = (col * square_size + space, row * square_size + space)
            end_desc = (col * square_size + square_size - space, row * square_size + square_size - space)
            pygame.draw.line(Screen_board, colour_of_X, start_desc, end_desc, width_of_cross)
            # top down line
            start_asc = (col * square_size + space, row * square_size + square_size - space)
            end_asc = (col * square_size + square_size - space, row * square_size + space)
            pygame.draw.line(Screen_board, colour_of_X, start_asc, end_asc, width_of_cross)

        elif player == 2:
            # Drawing of the circle
            center = (col * square_size + square_size // 2, row * square_size + square_size // 2)
            pygame.draw.circle(Screen_board, circle_color, center, radios_of_circle, width_of_circle)


class Controller:
    def __init__(self):
        self.model = Model()
        self.ai = AI()
        self.view = View()
        self.player = 1  # player one is cross  # player two is circle
        self.gamemode = 'ai'  # player v player or ai mode
        self.running = True
        self.view.drawing_of_lines()

    def make_move(self, row, col):
        self.model.mark_boxes(row, col, self.player)
        self.view.draw_figures(row, col, self.player)
        self.next()

    def next(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def game_over(self):
        return self.model.final_state(show=True) != 0 or self.model.board_full()

    def restart(self):
        self.__init__()


def main():
    game = Controller()
    board = game.model
    ai = game.ai

    # This is the Mainloop!
    while True:
        # pygame events
        for event in pygame.event.get():

            # quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # (using keyboard key) keydown event
            if event.type == pygame.KEYDOWN:

                # press (P) to change to player v player
                if event.key == pygame.K_p:
                    game.change_gamemode()

                # restarting the whole game press (R)
                if event.key == pygame.K_r:
                    game.restart()
                    board = game.model
                    ai = game.ai

                # If you would like to quite the whole game press (q)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()

                # This is player vs random AI press (0)
                if event.key == pygame.K_0:
                    ai.level = 0

                # This is player vs unbeatable AI press (1)
                if event.key == pygame.K_1:
                    ai.level = 1

            # Using the mouse (click event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                row = position[1] // square_size
                col = position[0] // square_size

                # This is when player or human claims a move
                if board.empty_box(row, col) and game.running:
                    game.make_move(row, col)

                    if game.game_over():
                        game.running = False

        # AI initial call
        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            # This updates the screen/window
            pygame.display.update()

            # The evaluation
            row, col = ai.evaluation(board)
            game.make_move(row, col)

            if game.game_over():
                game.running = False

        pygame.display.update()


if __name__ == "__main__":
    main()

"PLease check README file for sources used throughout the project !!!"