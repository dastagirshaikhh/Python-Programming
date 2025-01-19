s = input("Enter a str or int : ")
# if str1.isnumeric:
#     print(str1,"is an int")
# else:
#     print(str1,"is a str")


isInt = True
try:
    int(s)
except ValueError:
    isInt = False
if isInt:
    print(s,"is an int")
else:
    print(s,"is a str")