# m - capacity of the knapsack, w - weights list, v - values list, n - number of items we consider
def solve_recursion(m, w, v, n):

        # base cases 
        if m == 0 or n == 0:
            return 0

        # the given item can NOT fit into the knapsack
        if w[n-1] > m:
            return solve_recursion(m, w, v, n-1)
        # else: given item can fit into the knapsack so we have 2 options (include, exclude)
        else:
            n_include = v[n-1] + solve_recursion(m-w[n-1], w, v, n-1)
            n_exclude = solve_recursion(m, w, v, n-1)
            return max(n_include, n_exclude)
    

if __name__ == "__main__":
    # this is the example we have seen in theory (result is $7)
    print(solve_recursion(6, [2, 3, 3], [1, 2, 5], 3))
