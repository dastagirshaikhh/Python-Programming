a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
for num in range(a,b + 1):
    if (num % 2 == 0):
        print(num, end =" ")