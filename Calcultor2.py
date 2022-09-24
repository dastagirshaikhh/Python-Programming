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
    # elif oprtn == '//':
    #     print(num1 // num2)
    elif oprtn == '%':
        print(num1 % num2)
    else:
        print('Wrong / invalid format')
calculator(num1,num2,oprtn)