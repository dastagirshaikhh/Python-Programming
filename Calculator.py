def calculator():
    while True:
        print('''\nChoose the operation (type any one value from the brackets below to choose an operation)
    1.Calculator (cal / 1)
    2.Calculate Area (calA / 2)
    3.Calculate Volume (calV / 3)
    4.To check if number is Palindrome (pal / 4)
    5.Operaton in matrix (mat / 5)
    6.Print Table (table / 6)
    Type 'exit' to cancel''')
        oprn = input("Operation : ")
        if oprn == "exit":
            break
        else:
            # Calculator
            if oprn == "cal" or oprn == "1":
                print("\nBelow is the list of the operations you can perform")
                list1 = ["Addition", "Subtraction",
                         "Multiplication", "Division", "Modulus"]
                for i in list1:
                    print(i)
                print("Enter the first number, operation and second number if you want to calculate everything type 'all' in place of operations")

                x, y, z = input("Input : ").split()
                x = int(x)
                z = int(z)

                add = x+z
                sub = x/z
                mul = x*z
                div = x/z
                mod = x % z
                all = (add, sub, mul, div, mod)

                if y == "+":
                    print(add)
                elif y == "-":
                    print(sub)
                elif y == "*":
                    print(mul)
                elif y == "/":
                    print(div)
                elif y == "%":
                    print(mod)
                elif y == "all":
                    for o in all:
                        print(o)
                else:
                    print("Invalid input")

            # Area of shapes
            elif oprn == "calA" or oprn == "2":
                print("\nBelow is the list of the shapes you can find the area of")
                shapes = ["1.Circle", "2.Triangle", "3.Square", "4.Rectangle",
                          "5.Trapezium", "6.Parallelogram", "7.Ellipse"]
                for s in shapes:
                    print(s)

                while True:
                    shape = input(
                        "Enter the name of shape or type 'exit' to cancel : ")
                    shape = shape.lower()
                    if shape == "exit":
                        break
                    else:

                        # Circle
                        pie = 22/7
                        if shape == "circle" or shape == "1":
                            s1 = int(input("Enter radius : "))
                            s2 = pie*(s1*s1)
                            print("Area of circle : ", s2)

                            # Triangle
                        elif shape == "triangle" or shape == "2":
                            t1 = int(input("Enter height : "))
                            t2 = int(input("Enter base : "))
                            t3 = (t1*t2)/2
                            print("Area of Triangle : ", t3)

                            # Square
                        elif shape == "square" or shape == "3":
                            s3 = int(input("Enter the length : "))
                            s4 = s3*s3
                            print("Area of Square : ", s4)

                            # Rectangle
                        elif shape == "rectangle" or shape == "4":
                            r1 = int(input("Enter length : "))
                            r2 = int(input("Enter breadth : "))
                            r3 = r1*r2
                            print("Area of Rectangle", r3)

                            # Trapezium
                        elif shape == "trapezium" or shape == "4":
                            tr1 = int(input("Enter length of base 1 : "))
                            tr2 = int(input("Enter length of base 2 : "))
                            tr3 = int(input("Enter height : "))
                            tr4 = tr1+tr2
                            print("Area of Trapezium : ", tr4)

                            # Parallelogram
                        elif shape == "parallelogram" or shape == "5":
                            p1 = int(input("Enter length : "))
                            p2 = int(input("Enter breadth : "))
                            p3 = p1*p2
                            print("Area of Parallelogram : ", p3)

                            # Ellipse
                        elif shape == "ellipse" or shape == "7":
                            e1 = int(input("Enter length of axis 1 : "))
                            e2 = int(input("Enter length of axis 2 : "))
                            e3 = pie*(e1*e2)
                            print("Area of Ellpise : ", e3)
                        else:
                            print("Invalid input")

            # Volume of shapes
            elif oprn == "calV" or oprn == "3":
                print("\nBelow is the list of the shapes you can find volume of")
                Vol = ["1.Cube", "2.Cuboid", "3.Pyramid", "4.Sphere", "5.Cone",
                       "6.Cylinder", "7.Prism", "8.Ellipsoid", "9.Tetrahedron\n"]
                for v in Vol:
                    print(v)

                while True:
                    shape = input(
                        "Enter name of shape or type 'exit' to cancel : ")
                    shape = shape.lower()
                    if shape == "exit":
                        break
                    else:

                        # Cube
                        pie = 22/7
                        if shape == "cube" or shape == "1":
                            c1 = int(input("Enter length of the side : "))
                            c2 = c1**3
                            print("Volume of cube :", c2)

                            # Cuboid
                        elif shape == "cuboid" or shape == "2":
                            cb1 = int(input("Enter length : "))
                            cb2 = int(input("Enter breadth : "))
                            cb3 = int(input("Enter height : "))
                            cb4 = cb1*cb2*cb3
                            print("Volume of cuboid :", cb4)

                            # Pyramid
                        elif shape == "pyramid" or shape == "Pyramid":
                            p1 = int(input("Enter base : "))
                            p2 = int(input("Enter height : "))
                            p3 = 1/2*(p1*p2)
                            print("Volume of Pyramid :", p3)

                            # Sphere
                        elif shape == "sphere" or shape == "4":
                            s1 = int(input("Enter radius : "))
                            s2 = 4/3 * pie * 4/3 * (s1**3)
                            print("Volume of sphere :", s2)

                            # Cone
                        elif shape == "cone" or shape == "5":
                            c1 = int(input("Enter radius : "))
                            c2 = int(input("Enter height : "))
                            c3 = pie * (c1**2) * c2/3
                            print("Volume of cone : ", c3)

                            # Cyilnder
                        elif shape == "Cylinder" or shape == "6":
                            cl1 = int(input("Enter radius : "))
                            cl2 = int(input("Enter height : "))
                            cl3 = pie * (cl1*cl1*cl2)
                            print("Volume of cylinder :", cl3)

                            # Prism
                        elif shape == "prism" or shape == "7":
                            pr1 = int(input("Enter breadth : "))
                            pr2 = int(input("Enter height : "))
                            pr3 = pr1*pr2
                            print("Volume of prism :", pr3)

                            # Ellipsod
                        elif shape == "ellipsoid" or shape == "8":
                            e1 = int(input("Enter length of axis 1 : "))
                            e2 = int(input("Enter length of axis 2 : "))
                            e3 = int(input("Enter length of axis 3 : "))
                            e4 = 4/3*(pie)*(e1*e2*e3)
                            print("Volume of ellipsoid : ", e4)

                            # Tetrahedron
                        elif shape == "tetrahedron" or shape == "9":
                            import math
                            te1 = int(input("Enter the length of the edge : "))
                            te2 = te1**3/(6*math.sqrt(2))
                            print("Volume of tetrahedron :", te2)
                        else:
                            print("Invalid input")

            # Palindrome numbers
            elif oprn == "pal" or oprn == "4":
                def palindrome():
                    number = int(
                        input("Enter a number to check if it is a palindrome : "))
                    temp = number
                    reverse = 0
                    while (number > 0):
                        dig = number % 10
                        reverse = reverse * 10 + dig
                        number = number // 10
                    if temp == reverse:
                        print(temp, "is a Palindrome")
                    else:
                        print(temp, "is not a Palindrome")
                palindrome()

            # Matrix
            elif oprn == "mat" or oprn == "5":

                # Creating Matrix
                print("\nCreate a matrix to perform operations on it")
                r = int(input("Enter number of rows : "))
                c = int(input("Enter number of columns : "))
                print("Enter elements row vise ")
                mtrx = [[int(input()) for i in range(c)] for j in range(r)]
                print("\nMatrix : ")
                for i in range(r):
                    for j in range(c):
                        matrix1 = (format(mtrx[i][j], "<4"))
                        print(matrix1, end="")
                    print()

                # Operations of Matrix
                print(
                    "\nBelow are the operations you can perform if want to perform all type 'all'")
                matrix = ["1.Transpose", "2.Inverse", "3.Addition",
                          "4.Subtraction", "5.Multiplication"]
                for i in matrix:
                    print(i)
                m = input(
                    "\nEnter operation you want to perform on above Matrix : ")

                # Transpose of a matrix
                if m == "Transpose" or m == "1":
                    for i in range(r):
                        for j in range(c):
                            print(format(mtrx[i][j], "<4"), end="")
                        print()
                    result = [[0 for i in range(r)] for j in range(c)]
                    for i in range(c):
                        for j in range(r):
                            result[i][j] = mtrx[j][i]
                    print("Transpose of a matrix :")
                    for i in range(c):
                        for j in range(r):
                            print(format(result[i][j], "<4"), end="")
                        print()

                # Inverse
                if m == "Inverse" or m == "2":
                    import numpy as np
                    Invmtrx = np.array(mtrx)
                    print("\nInverse of above Matrix")
                    print(np.linalg.inv(Invmtrx))

                # Addition
                elif m == "add" or m == "3":
                    import numpy as np
                    addmtrx = np.array(mtrx)
                    print("\nTo add matrixes please create another matrix below")
                    r1 = int(input("Enter number of rows : "))
                    c1 = int(input("Enter number of columns : "))
                    print("Enter elements row vise ")
                    mtrx1 = [[int(input()) for i in range(c1)]
                             for j in range(r1)]
                    print("\nMatrix 2 : ")
                    for i in range(r1):
                        for j in range(c1):
                            mtrx1 = (format(mtrx1[i][j], "<4"))
                            print(mtrx1, end="")
                            # print()
                    print("Addition of 2 matrix\n")
                    # mtrx1 = int(mtrx1)
                    # addmtrx = mtrx1 + matrix1
                    # print(addmtrx, end="")

        # Program to print tables
            elif oprn == "table" or oprn == "6":
                # from datetime import datetime
                # start_time = datetime.now()
                num = input("Enter a number or type exit to cancel : ")
                n = int(input("Enter number : "))
                while True:
                    if num == "exit":
                        break
                    else:
                        num = int(num)
                        for i in range(1, n+1):
                            print(num, "x", i, "=", num*i)
                        break
                # end_time = datetime.now()
                # print('Duration: {}'.format(end_time - start_time))


calculator()
