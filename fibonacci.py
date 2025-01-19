n = int(input("Enter the number of terms: "))
# first two terms
num1, num2 = 0, 1
count = 0
# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while n > count:
       print(num1)
       nth = num1 + num2
       # update values
       num1 = num2
       num2 = nth
       count += 1
