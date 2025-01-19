# Practical 11.1
# program to print fibonacci series using dynamic programming
class Fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]

    def get(self, index: int) -> list:
        """
        Get the Fibonacci number of `index`. If the number does not exist,
        calculate all missing numbers leading up to the number of `index`.

        >>> Fibonacci().get(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> Fibonacci().get(5)
        [0, 1, 1, 2, 3]
        """
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


def main():
    print(
        "Fibonacci Series Using Dynamic Programming\n",
        "Enter the index of the Fibonacci number you want to calculate ",
        "in the prompt below. (To exit enter exit or Ctrl-C)\n",
        sep="",
    )
    fibonacci = Fibonacci()

    while True:
        prompt: str = input(">> ")
        if prompt in {"exit", "quit"}:
            break

        try:
            index: int = int(prompt)
        except ValueError:
            print("Enter a number or 'exit'")
            continue

        print(fibonacci.get(index))


if __name__ == "__main__":
    main()

# fibonacci series using dynamic programming
class Fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]
    def get(self, index: int) -> list:
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]
def main():
    print(
        "Fibonacci Series Using Dynamic Programming\n",
        "Enter the index of Fibonacci number ",
        "in the prompt below. (To exit enter exit or Ctrl-C)\n",
        sep="",
    )
    fibonacci = Fibonacci()
    while True:
        prompt: str = input(">> ")
        if prompt in {"exit", "quit"}:
            break
        try:
            index: int = int(prompt)
        except ValueError:
            print("Enter a number or 'exit'")
            continue
        print(fibonacci.get(index))
if __name__ == "__main__":
    main()

# Practical 11.1
# fibonacci series using dynamic programming
def fibonacci(n):
    # Returns the nth number in the Fibonacci series.

    # Use dynamic programming to cache results and avoid redundant calculations
    cache = [0, 1]
    for i in range(2, n + 1):
        cache.append(cache[i-1] + cache[i-2])
    return cache[n]

def print_fibonacci_series(n):
    # Prints the Fibonacci series up to the nth number.

    # Use dynamic programming to cache results and avoid redundant calculations
    cache = [0, 1]
    for i in range(2, n + 1):
        cache.append(cache[i-1] + cache[i-2])
    for i in range(n + 1):
        print(cache[i])

# Example usage
print_fibonacci_series(10)
