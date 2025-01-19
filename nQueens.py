# NQueens problem


class Queens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]

    def solve_n_queens(self):
        # starting with the first queen n = 0
        if self.solve(0):
            self.display()
        else:
            print("There is no solution to the problem")

    # base case of the problem (means problem solved)
    def solve(self, col_index):
        if col_index == self.n:
            return True

        # finding position for the queen in a column
        # r is row index
        for r in range(self.n):
            if self.is_place_valid(r, col_index):
                # 1 means that there is queen at the given location
                self.board[r][col_index] = 1

                # we call the same function with the column index + 1
                # to find a cell for the next queen (iterating over the board)
                if self.solve(col_index + 1):
                    return True

                # backtrack
                # print("BACKTRACKING...")
                self.board[r][col_index] = 0

        # when we have considered all the rows in the column and could'nt find a valid cell for a queen
        return False

    def is_place_valid(self, row_index, col_index):
        # checking the rows whether the queens can attack each other horizontally
        # it means that there a queen present in the column
        for i in range(self.n):
            if self.board[row_index][i] == 1:
                return False

        # we do not have to check the same column because we only place one queen in a single column
        # we have to check the diagonals from left to bottom right
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break

            if self.board[i][j] == 1:
                return False

            j -= 1

        # we do not have to check the same column because we only place one queen in a single column
        # we have to check the diagonals from left to bottom right
        j = col_index
        for i in range(row_index, self.n):
            if j < 0:
                break

            if self.board[i][j] == 1:
                return False

            j -= 1

        return True

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print(" Q ", end="")
                else:
                    print(" 0 ", end="")
            print("\n")


if __name__ == "__main__":
    queens = Queens(5)
    # queens.display()
    queens.solve_n_queens()
