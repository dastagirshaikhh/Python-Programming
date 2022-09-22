# Important algorithms

# factorial algorithm 1
def fact(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
    return f


# factorial algorithm 2 using recursion
def fact_recursion(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


# fib series
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(n)
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


# prime number algorithm
def prime(n):
    flag = 1
    for i in range(2, n):
        if n % i == 0:
            flag = 0
        i = +i

    if flag == 0:
        return 'not prime'
    else:
        return 'prime'


# even-odd algorithm
def even_odd(n):
    while n > 2:
        n = n - 2
    if n == 2:
        return 'even'
    else:
        return 'odd'


# swap numbers
def swap(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b
