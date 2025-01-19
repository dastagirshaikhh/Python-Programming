# # Addition of two matrices
# row = int(input("enter row number : "))
# col = int(input("enter column number : "))

# print("enter elements(rowwise) for matrix 1 :")
# matrix1 = [[int(input()) for i in range(col)] for j in range(row)]

# print("Matrix 1 :")
# for i in range(row):
#     for j in range(col):
#         print(format(matrix1[i][j], "<3"), end="")
#     print()

# print("enter elements(rowwise) for matrix 2 :")
# matrix2 = [[int(input()) for i in range(col)] for j in range(row)]

# print("Matrix 2 :")
# for i in range(row):
#     for j in range(col):
#         print(format(matrix2[i][j], "<3"), end="")
#     print()

# res = [[0 for i in range(col)] for j in range(col)]
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         res[i][j] = matrix1[i][j] + matrix2[i][j]

# print("Sum of Matrices :")
# for i in range(row):
#     for j in range(col):
#         print(format(res[i][j], "<3"), end="")
#     print()


# Multiplication of two matrices
print("*Rows of Matrix 1 and columns of Matrix 2 must be equal.*")

print("enter row and column of Matrix 1")
row1 = int(input("enter row number : "))
col1 = int(input("enter column number : "))

print("enter elements(rowwise) for matrix 1 :")
matrix1 = [[int(input()) for i in range(col1)] for j in range(row1)]

print("Matrix 1:")
for i in range(row1):
    for j in range(col1):
        print(format(matrix1[i][j],"<4"), end="")
    print()

print("enter row and column of Matrix 2")
row2 = int(input("enter row number : "))
col2 = int(input("enter column number : "))

if (col1 != row2):
    print("Invalid input rows and columns of matrix 1 & 2 are not equal")
else:
    print("enter elements(rowwise) for matrix 2 :")
    matrix2 = [[int(input()) for i in range(col2)] for j in range(row2)]

    print("Matrix 2 :")
    for i in range(row2):
        for j in range(col2):
            print(format(matrix2[i][j],"<4"), end="")
        print()

    res = [[0 for i in range(col2)] for j in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                res[i][j] = res[i][j] + matrix1[i][k] * matrix2[k][j]

    print("Multiplication of matrices :")
    for i in range(row1):
        for j in range(col2):
            print(format(res[i][j],"<4"), end="")
        print()