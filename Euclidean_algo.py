# recursive implementation
def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)

print(gcd(45, 99))

# using iterative implementation
def gcd_iter(a, b):

    while a % b != 0:
        a, b = b, a % b

    return b

print(gcd_iter(49, 70))
