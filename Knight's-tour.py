class KnightsTour:
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.matrix = [
            [-1 for _ in range(self.boardsize)] for _ in range(self.boardsize)
        ]

    def solve_problem(self):
        self.matrix[0][0] = 0

        if self.solve(1, 0, 0):
            self.print_solution()
        else:
            print("There is no solution to the problem")

    def solve(self, step_counter, x, y):
        if step_counter == self.boardsize * self.boardsize:
            return True

        for move_index in range(len(self.x_moves)):
            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            if self.is_valid_move(next_x, next_y):
                self.matrix[next_x][next_y] = step_counter

                if self.solve(step_counter + 1, next_x, next_y):
                    return True

                self.matrix[next_x][next_y] = -1

        return False

    def is_valid_move(self, x, y):
        if x < 0 or x >= self.boardsize:
            return False
        if y < 0 or y >= self.boardsize:
            return False
        if self.matrix[x][y] > -1:
            return False
        return True

    def print_solution(self):
        for i in range(self.boardsize):
            for j in range(self.boardsize):
                print(self.matrix[i][j], end=" | ")
            print("\n")


if __name__ == "__main__":
    kt = KnightsTour(5)
    kt.solve_problem()
