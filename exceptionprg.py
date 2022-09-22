try:
    total = 0
    num1 = int(input('Enter a number '))
    num2 = int(input('Enter a number '))
    total = num1*num2
except Exception as e:
    print(e)
    print(type(e))
else:
    print(total)
finally:
    print("Code completed!")
