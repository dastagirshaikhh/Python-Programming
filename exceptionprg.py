# try:
#     total = 0
#     num1 = int(input('Enter a number '))
#     num2 = int(input('Enter a number '))
#     total = num1*num2
# except Exception as e:
#     print(e)
#     print(type(e))
# else:
#     print(total)
# finally:
#     print("Code completed!")

try:
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
except Exception as e:
    print(e)

# except ValueError:
#     print("Invalid input")

finally:
    print("The finally part of code is always executed.")