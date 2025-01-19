# program to find if a number is even or odd using bit manipulation
# XOR operator increments the value by 1 for even numbers
# and for odd number it decrements by 1 but in this case we are only incrementing it by 1
# as we are checking if a number as even as the corner condition

def is_even(n):
    if n ^ 1 == n+1:
        return True
    return False

if __name__ == "__main__":
    n = 155
    if is_even(n):
        print("the number is even")
    else:
        print("the number is odd")