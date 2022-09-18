game_start_cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
matrix_rows = [game_start_cells[x:x + 3] for x in range(0, len(game_start_cells), 3)]
matrix = []


def game_move():
    marks = ["X", "O"]
    turn_iter = 0
    while True:
        global matrix
        try:
            x_coordinate, y_coordinate = map(int, input().split(" "))
        except ValueError:
            print("You should enter numbers!")
        else:
            if 0 < x_coordinate > 3 or 0 < y_coordinate > 3:
                print("Coordinates should be from 1 to 3!")
            elif matrix_rows[x_coordinate - 1][y_coordinate - 1] == "X" or matrix_rows[x_coordinate - 1][y_coordinate -
                                                                                                         1] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                matrix_rows[x_coordinate - 1][y_coordinate - 1] = marks[turn_iter % 2]
                matrix = [[matrix_rows[0][0], matrix_rows[0][1], matrix_rows[0][2]],
                          [matrix_rows[0][0], matrix_rows[1][0], matrix_rows[2][0]],
                          [matrix_rows[0][1], matrix_rows[1][1], matrix_rows[2][1]],
                          [matrix_rows[0][2], matrix_rows[1][2], matrix_rows[2][2]],
                          [matrix_rows[0][0], matrix_rows[1][1], matrix_rows[2][2]],
                          [matrix_rows[0][2], matrix_rows[1][1], matrix_rows[2][0]]]
                print_grid()
                if x_win():
                    print("X wins")
                    break
                elif o_win():
                    print("O wins")
                    break
                else:
                    if draw_status():
                        print("Draw")
                        break
                    turn_iter += 1
                continue


def print_grid():
    print("---------" + "\n" +
          "| {0} {1} {2} |".format(matrix_rows[0][0], matrix_rows[0][1], matrix_rows[0][2]) + "\n" +
          "| {0} {1} {2} |".format(matrix_rows[1][0], matrix_rows[1][1], matrix_rows[1][2]) + "\n" +
          "| {0} {1} {2} |".format(matrix_rows[2][0], matrix_rows[2][1], matrix_rows[2][2]) + "\n" +
          "---------")


def o_win():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i].count("O") == 3:
                return True


def x_win():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i].count("X") == 3:
                return True


def draw_status():
    if not o_win() and not x_win():
        for i in range(len(matrix)):
            if sum(x.count(" ") for x in matrix) == 0:
                return True
            else:
                return False


print_grid()

game_move()

