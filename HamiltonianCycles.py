class HamiltonianProblem:

    # adjancecy matrix - so matrix representation of the G(V,E) graph
    def __init__(self, adjacency_matrix):
        # number of V vertices in the graph
        self.n = len(adjacency_matrix)
        # the adjacency mtrix itself
        self.adjacency_matrix = adjacency_matrix
        # we store the vertices in a list (this is how we track the hamiltionian cycle )
        # note: first item is the same as the last item (because it is a cycle)
        self.hamiltonian_path = [0]

    def hamiltonian_cycle(self):
        if self.solve(1):
        # we start with first vertex (index 0)
            if self.adjacency_matrix[self.hamiltonian_path[-1]][0] == 1:
                self.hamiltonian_path.append(0)
                self.show_cycle()
            else:
                print("There is not Hamiltonian cycle in the graph")
        else:
            print("There is not Hamiltonian cycle in the graph")

    def solve(self, position):
        # this is the backtracking algorithm implementation
        # PRINT THE hamiltonian_path WHEN IT IS FOUND !!! (this is how I can check the solution automatically :) )
        if position == self.n:
            return self.adjacency_matrix[self.hamiltonian_path[-1]][0] == 1
        
        for vertex in range(1, self.n):
            if self.is_feasible(vertex, position):
                self.hamiltonian_path.append(vertex)

                if self.solve(position + 1):
                    return True
                
                self.hamiltonian_path.pop()
            
        return False
   

    def is_feasible(self, vertex, actual_position):
        # check whether the given vertex is feasible (can be included in the cycle or not)
        if self.adjacency_matrix[self.hamiltonian_path[actual_position - 1]][vertex] == 0:
            return False
        
        for i in range(actual_position):
            if self.hamiltonian_path[i] == vertex:
                return False
        return True
    
    def show_cycle(self):
        print(self.hamiltonian_path)
        


if __name__ == "__main__":

    # this is a small example
    m = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]

    hamiltonian = HamiltonianProblem(m)
    hamiltonian.hamiltonian_cycle()