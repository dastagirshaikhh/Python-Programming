a = int(input("Enter side ab : "))
b = int(input("Enter side ac : "))
c = int(input("Enter side bc : "))
if a == b == c:
    print("It is an Equilateral triangle.")
elif a == b or b == c or c == a:
    print("It is an Isosceles triangle.")
elif a != b != c:
    print("It is a scalene triangle.")
else:
    print("Invalid input")