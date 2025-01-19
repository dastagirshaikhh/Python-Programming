# creating a function using 'def' and naming the function
a = input("Enter 1 to check if a number is a plindrome or enter 2 to check if a number is prime : ")

def palindrome(): #creating a function
    number = int(input("Enter a number : ")) 
    temp = number
    reverse = 0
    while (number>0):
        dig = number % 10
        reverse = reverse * 10 + dig
        number = number // 10
    if temp == reverse:
        print ("Entered number is a Palindrome")
    else:
        print ("Entered number is not a Palindrome")


def prime():
    number = int(input("Enter a number to check whether it is a prime number or not : "))
    for nums in range(2,number):
        if number % nums == 0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")

if a == "1":
    palindrome() #calling a function
elif a == "2":
    prime()
else:
    print("Invalid input")