# program to test whether a number is within 100 of 1000 or 2000
a = int(input("Enter a number : "))
if a <= 100:
    print("The number is in the range of 100.")
elif a >= 1000 and a <= 2000:
    print("The number is in the range of 1000 and 2000")