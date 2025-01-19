# Program to convert celsius to farenheit
def celtofer():
    degree = input("Enter the degree in which you want to convert the temperature : ")
    if degree == "f":
        f = int(input("Enter temperature in Celsius : "))
        fer = f * 1.8 + 32
        print(f, "degree Celsius is", fer, "degree Farenheit")
    if degree == "c":
        c = int(input("Enter temperature in Farenheit : "))
        cel = (c - 32) / 1.8
        print(c, "degree Farenheit is", cel, "degree Celsius")


celtofer()
