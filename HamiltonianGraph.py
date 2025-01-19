class Hamiltonian:
    def __init__(self, adj_matrix):
        self.n = len(adj_matrix)
        self.adj_matrix = adj_matrix
        self.path = [0]

    def hamiltonian(self):
        if self.solve(1):
            self.displayGraph()
        else:
            print("There is no solution to the problem")

    def solve(self, position):
        # Base case
        if position == self.n:
            return True

        for vertex in range(1, self.n):
            if self.feasible(vertex, position):
                # appending the vertex in the graph
                self.path.append(vertex)

                if self.solve(position + 1):
                    return True

                # BACKTRACKING
                # removing the last item from the graph to backtrack
                self.path.pop()

        # if we have considered all the vertices without a success
        return False

    # checking whether there is a connection between nodes
    def feasible(self, vertex, position):
        if self.adj_matrix[self.path[position - 1]][vertex] == 0:
            return False

        # checking whether we have included the given vertiex in the result
        for i in range(position):
            if self.path[i] == vertex:
                return False
        return True

    def displayGraph(self):
        for vertex in self.path:
            print(vertex)


if __name__ == "__main__":
    m = [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0],
    ]
    h = Hamiltonian(m)
    h.hamiltonian()
