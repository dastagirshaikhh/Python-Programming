#File handling

#Creating a file : Dastagir Shaikh.txt

#modes
#1 read (r) - Opens an existing file , if not there throws error
#2 write (w) - If file there opens up and write it if not there it creates one and overwrite it.
#3 append (a) - IF file there opens up and add content, if not create's one

#*********************************************************************************


# import os
# os.getcwd #(Command to check the current working directory)


# ***************************************************************************************

#creating a file and handling it.

f = open("Dastagir Shaikh.txt", 'r')
print ("File name : ",f.name)
print ("File mode : ",f.mode)
print ("File is readable : ",f.readable())
print ("File is writable : ",f.writable())
print ("File is closed :",f.closed)
f.close()
print ("File is closed : ",f.closed)

# ****************************************************

# adding content in the file

# Read only

f = open ("Dastagir Shaikh.txt", 'r')
f.write ('Dastagir is a student in bsc cs\n')
f.write ("Dastagir is learning Python\n")
f.close()

# Write only

f = open ("Dastagir Shaikh.txt", 'w')
f.write ('Dastagir is a Data Scientist\n')
f.write ('Dastagir has completed learning python\n')
f.close()

#Append

f = open("Dastagir Shaikh.txt", 'a')
f.write ("I am learning Data science and Machine Learning\n")
f.write ("I am learning python\n")
f.close()

#Printing the data of a txt file

f = open ("Dastagir Shaikh.txt",'r')
data = f.read()
print (data)
f.close()