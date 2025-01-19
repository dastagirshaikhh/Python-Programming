# Regular Expression
import re

strg1 = "Hii my name is Dastagir"
print(re.findall("[a-r]", strg1)) # set of characters

strg2 = "I am 18 years old"
print(re.findall("[0-9]",strg2)) # set of numbers

strg3 = "hello world"
print(re.findall("he...o", strg3)) # any character

a = re.findall("^hello",strg3) # check if a string starts with a particular character
if a:
    print("The string starts with",a)
else:
    print("The string does not starts with hello")

b = re.findall("world$", strg3) # check if a string ends with a particular character
if b:
    print("The string ends with",b)
else:
    print("The string does not ends with world")

print(re.findall("h.*o",strg3)) # zero or more occurence

print(re.findall("h.+o",strg3)) # one or more occurence

print(re.findall("hel.?o",strg3)) # zero or one occurence

print(re.findall("he.{2}o",strg3)) # Exactly the specified number of occurence

strg4 = "The rain mainly falls in Spain" # Either / or 
c = re.findall("falls|stay",strg4)
if c:
    print("one match found")
else:
    print("no matches found")