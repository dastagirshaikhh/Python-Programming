# # python program to print factorial using dynamic programming ?
# # Factorial of a number using memoization

from functools import lru_cache


@lru_cache
def factorial(num: int) -> int:
    
    if num < 0:
        raise ValueError("Number should not be negative.")

    return 1 if num in (0, 1) else num * factorial(num - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# factorial using dynamic programming
def factorial(n):
    cache = [0] * (n + 1)
    cache[0] = 1

    for i in range(1, n + 1):
        cache[i] = i * cache[i - 1]

    return cache[n]

n = 5
print(f"The factorial of {n} is {factorial(n)}")