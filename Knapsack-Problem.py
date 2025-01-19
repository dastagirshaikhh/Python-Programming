from time import time


class KnapSack:
    def __init__(self, n, m, w, v):
        self.m = m
        self.w = w
        self.v = v
        self.n = n
        self.S = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    def solve(self):
        for i in range(self.n + 1):
            for w in range(self.m + 1):
                not_taking_item = self.S[i - 1][w]
                taking_item = 0

                if self.w[i] <= w:
                    taking_item = self.v[i] + self.S[i - 1][w - self.w[i]]

                self.S[i][w] = max(not_taking_item, taking_item)

    def show_result(self):
        print("total benifit: %d" % self.S[self.n][self.m])

        w = self.m
        for n in range(self.n, 0, -1):
            if self.S[n][w] != 0 and self.S[n][w] != self.S[n - 1][w]:
                print("we take item number %d" % n)
                w = w - self.w[n]


if __name__ == "__main__":
    items = 4
    KnapSack_capacity = 7
    weights = [0, 1, 3, 4, 5]
    profits = [0, 1, 4, 5, 7]
    start = time()
    satchel = KnapSack(items, KnapSack_capacity, weights, profits)
    satchel.solve()
    satchel.show_result()
    end = time()
    print(end - start)