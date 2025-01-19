class ColorProblem:
    def __init__(self, adjMatrix, numcolors):
        self.n = len(adjMatrix)
        self.adjMatrix = adjMatrix
        self.numcolors = numcolors
        self.colors = [0 for _ in range(self.n)]

    def coloringProblem(self):
        if self.solve(0):
            self.show_result()
        else:
            print("There is no solution")

    def solve(self, node_index):
        if node_index == self.n:
            return True
        for color_index in range(1, self.numcolors + 1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                if self.solve(node_index + 1):
                    return True

        return False

    def is_color_valid(self, node_index, color_index):
        for i in range(self.n):
            if self.adjMatrix[node_index][i] == 1 and color_index == self.colors[i]:
                return False
        return True

    def show_result(self):
        for v, c in enumerate(self.colors):
            print("Vertex %d has color value %d" % (v, c))

if __name__ == "__main__":
    m = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    numofcolors = 3
    coloringproblem = ColorProblem(m, numofcolors)
    coloringproblem.coloringProblem()
