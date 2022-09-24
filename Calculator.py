#Write a program in python to calculate
x, y, z = input("Enter the operation : ").strip()
num1 = int(x)
oprtn = y
num2 = int(z)
def calculator(num1,num2,operation = 'all'):
    if oprtn == '+':
        print(num1 + num2)
    elif oprtn == '-':
        print(num1 - num2)
    elif oprtn == '*':
        print(num1 * num2)
    elif oprtn == '/':
        print(num1 / num2)
    elif oprtn == '//':
        print(num1 // num2)
    elif oprtn == '%':
        print(num1 % num2)
    elif oprtn == "all":
        print ("Addition :",num1+num2)
        print ("Subtraction :",num1-num2)
        print ("Multiplication :", num1*num2)
        print ("Division :",num1/num2)
        print ("Floor Division :",num1//num2)
        print ("Modulus :",num1%num2)
    elif oprtn == "":
        print ("Addition :",num1+num2)
        print ("Subtraction :",num1-num2)
        print ("Multiplication :", num1*num2)
        print ("Division :",num1/num2)
        print ("Floor Division :",num1//num2)
        print ("Modulus :",num1%num2)
    else:
        print('Wrong / invalid format')
calculator(num1,num2,oprtn)