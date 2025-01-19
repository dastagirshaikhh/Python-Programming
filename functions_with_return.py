num1 = int(input("Enter a number: "))
oprtn = input("")
num2 = int(input("Enter a number: "))
def calculator(num1,num2,operation = 'all'):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    elif operation == "all":
        print(outcome)
    else:
        print('Wrong / invalid format')

outcome = {"Addition": num1 + num2,
           "Subtraction": num1 - num2,
           "Multiplication": num1 * num2,
           "Division": num1 / num2}
calculator(num1,num2,oprtn)