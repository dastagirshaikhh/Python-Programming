num1 = int(input("Enter a number: "))
oprtn = input("")
num2 = int(input("Enter a number: "))
def calculator(num1,num2,operation = 'all'):
    if operation == '+':
        return print(num1 + num2)
    elif operation == '-':
        return print(num1 - num2)
    elif operation == '*':
        return print(num1 * num2)
    elif operation == '/':
        return print(num1 / num2)
    elif operation == "all":
        return print({
            'Addition:',num1+num2,
            'Subtraction:',num1+num2,
            'Multiplication:',num1*num2,
            'Division:',num1/num2})
    else:
        print('Wrong / invalid format')
calculator(num1,num2,oprtn)