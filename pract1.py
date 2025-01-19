# code to create and write in a file 
file1 = open("txt1.txt", "w")
file1.write("This is write command ")

# code to append text in  a file 
file1 = open("txt1.txt", "a")
file1.write("this is append mode")

# code to read a file 
file1 = open("txt1.txt", "r")
read_content = file1.read()
print(read_content)

# close a file 
file1.close()

# with function in file handling 
with open("txt1.txt", "w") as f:
    f.write("this is write mode using with command ")
with open("txt1.txt", "r") as f:
    print(f.read())
f.close()