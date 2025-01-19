import time
def recursion(n):
    if n == 0 or n == 1:
        return 1
    return recursion(n - 1) + recursion(n - 2)


def memoization(n, table):
    if n not in table:
        table[n] = memoization(n - 1, table) + memoization(n - 2, table)
    return table[n]

def tabulation(n, table):
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
        return table[n]

table = {0: 1, 1: 1}

print("finding fibonacci of 40 by using recursion and dynamic programming")

start = time.time()
print(recursion(40))
end = time.time()
print("Without using Dynamic programming",end - start,"seconds\n")

start = time.time()
print(memoization(40, table))
end = time.time()
print("By using Dynamic programming (memoization)",end - start,"seconds\n")

start = time.time()
print(tabulation(40, table))
end = time.time()
print("By using Dynamic programming (tabulation)",end - start,"seconds")
