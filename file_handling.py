#File handling

# Modes in file
# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist.
#           This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
#            If there is some sontent in the file it will overwrite the existing conttent fo the file with new one.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
#             If there is some content in a file it will not overwrite the previous content.
#             It will add content at the end.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): t mode is used to handle text files. t refers to the text mode.
#           There is no difference between r and rt or w and wt since text mode is the default.
#           The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc)


import os # import os is a library which allows us to print, set or change working directories
os.chdir("C:\My Programs\Python") # to set or change working directory 
print(os.getcwd()) #(Command to print the current working directory)


# ***************************************************************************************

# creating a file and checking whether it is open, closed, readable or writable
# and printing the name and mode of a file

f = open("myfile.txt","x") # creating a file

f = open("myfile.txt", "r") # opening a file in read mode
print ("File name :",f.name) # printing the name of a file
print ("File mode :",f.mode) # printing the mode of a file
print ("File is readable :",f.readable()) # checking if a file is readable or not
print ("File is writable :",f.writable()) # checking if a file is writable or not
print ("File is closed :",f.closed) # checking if a file is closed or not
f.close() # closing a file
print ("File is closed :",f.closed)

# ****************************************************

# reading content from a file
# Read mode

f = open ("myfile.txt",'r') # opening a file in read mode
print(f.read()) # printing the content of a file
f.close() # closing the file

# Write mode

f = open ("myfile.txt", 'w') # opening a file in write mode
# Adding content to in a file
f.write ("This is Dastagir I own a laptop with a powerful chip which has great graphics and better display\n")
f.write ("So long suckers!")
f.close() # closing the file

# Append mode

f = open("myfile.txt", 'a') # opening file using append mode
# Adding content in a file using write function {write()} in append mode
f.write ("\nWeeknd will soon cross 100 Million+ Monthly Listeners on Spotify\n")
f.write ('''Alabama, Arkansas
I do love my ma and pa
Not the way that do love you
Holy moley, me oh my
You're the apple of my eye
Girl, l've never loved one like you
Man, oh man, you're my best friend
scream it to the nothingness
There ain't nothing that I need
Well, hot and heavy, pumpkin pie
Chocolate candy, Jesus Christ
Ain't nothing please me more than you
Ah, home, let me go home
Home is wherever I'm with you\n''')
f.close()

# printing content of a file line-by-line using for loop
file = open("myfile.txt","r")
for lines in file:
    print(lines)
file.close()

# printing content of a file line-by-line using while loop

file = open("myfile.txt","r")
while file:
    lines = file.readline()
    print(lines)
    if lines == "":
        break
file.close()
