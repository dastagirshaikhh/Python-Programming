def binary_counter(n):
    i = 0
    while (n > 0):
        i += 1
        # left shift operator doubles the original value 
        # right shift operator divides the original value 
        n = n >> 1
    return i

if __name__ == "__main__":
    n = 24
    print(bin(n))
    print(binary_counter(n))