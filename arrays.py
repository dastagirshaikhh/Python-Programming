# Practical 1.1
# Program to store details of student and printing their details by entering roll no
import numpy as np
name = np.array(["Dastagir","Saud","Vishnu","Ayush"])
roll_no = np.array([60,88,72,69])
add = np.array(["Bandra","Bandra","Bhayandar","Khar"])

a = input("Enter student's name or Roll No : ")

if a == name[0] or a == "60":
    print("Name of student :",name[0],"\nRoll No of student :",
            roll_no[0], "\nAddress of student :",add[0])
elif a == name[1] or a == "88":
    print("Name of student :",name[1],"\nRoll No of student :",
            roll_no[1], "\nAddress of student :",add[1])
elif a == name[2] or a == "72":
    print("Name of student :",name[2],"\nRoll No of student :",
            roll_no[2], "\nAddress of student :",add[2])
elif a == name[3] or a == "69":
    print("Name of student :",name[3],"\nRoll No of student :"
            ,roll_no[3], "\nAddress of student :",add[3])

print()


# Practical 1.2
# Adding and Multiplying all the elements of a 1D array 
import numpy as np

arr = np.array([35, 48, 65, 98, 5])
# adding 1D array
sum1 = 0
for i in arr:
    sum1 += i
print("Value after Adding a 1D array :", sum1)

# multiplying 1D array
mult = 1
for i in arr:
    mult *= i
print("Value after Multiplying a 1D array :", mult)

print()

# <<<<<<---------------------------------->>>>>>>

# Practical 1.3
# printing total number of even and odd numbers from a user defined array
import numpy as np
num = []
a = int(input("Enter the number of elements you want : "))
for i in range(0, a):
    elements = int(input())
    num.append(elements)
num = np.array(num)
print("User defined array :", num)
even, odd = 0, 0
for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Total number of even numbers :", even)
print("Total number of odd numbers :", odd)

print()


# # <<<<<<---------------------------------->>>>>>>


# Practical 2.1
# Adding and Multiplying all the elements of a 2D array 
import numpy as np
array_1 = np.array([[6, 8, 9, 6], [3, 6, 8, 4]])
print(array_1)
# adding a 2D array
add = 0
for i in array_1:
    for i in i:
        add += i
print("Value after Adding a 2D array :", add)

# Multiplication of 2D array 
mul = 1
for i in array_1:
    for i in i:
        mul *= i
print("Value after Multiplying a 2D array :", mul)

print()