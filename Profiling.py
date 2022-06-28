import timeit
import AI_final


def generate_board(n):
    ai = AI_final.AI()
    board = AI_final.Model()
    for i in range(n):
        row, col = ai.random(board)
        board.boxes(row, col, ai.player)
        ai.player = ai.player ^ 3
    return board


if __name__ == '__main__':
    n = 9
    repeat = 100
    random_list = []
    minimax_list = []
    for i in range(n):
        ai = AI_final.AI()
        total_time = 0
        total_time1 = 0
        for j in range(repeat):
            board = generate_board(i)
            total_time += timeit.timeit(stmt="ai.random(model)", number=10000, globals=globals()) / 10000
            total_time1 += timeit.timeit(stmt="ai.minimax_ai(model, -100)", number=100, globals=globals()) / 100
        random_list.append(round(total_time / repeat * 1000, 6))
        minimax_list.append(round(total_time1 / repeat * 1000, 6))
    print(random_list)
    print(minimax_list)

"PLease check README file for sources used throughout the project !!!"

"This code was a referenced and learned from Ivan and his profiling code and it has helped me better understand " \
"the task overall :)"