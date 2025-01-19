# Practical 10.2
# program for implementing Stassen’s Matrix multiplication using
# Divide and Conquer method
import numpy as np
def strassen_matrix_multiplication(A, B):
    n = len(A)
    if n == 1:
        return A * B
    A11 = A[:n//2, :n//2]
    A12 = A[:n//2, n//2:]
    A21 = A[n//2:, :n//2]
    A22 = A[n//2:, n//2:]
    B11 = B[:n//2, :n//2]
    B12 = B[:n//2, n//2:]
    B21 = B[n//2:, :n//2]
    B22 = B[n//2:, n//2:]
    S1 = strassen_matrix_multiplication(B12 - B22, A11 + A12)
    S2 = strassen_matrix_multiplication(A11 + A22, B11 + B22)
    S3 = strassen_matrix_multiplication(A21 + A22, B11)
    S4 = strassen_matrix_multiplication(A11 - A21, B11 + B12)
    S5 = strassen_matrix_multiplication(A12 - A22, B21 + B22)
    S6 = strassen_matrix_multiplication(A11 - A22, B11 + B22)
    S7 = strassen_matrix_multiplication(A21 - A11, B11 + B12)
    C11 = S1 + S2 - S4 + S6
    C12 = S4 + S5
    C21 = S3 + S4
    C22 = S1 - S3 + S5 - S7
    C_top = np.concatenate((C11, C12), axis=1)
    C_bottom = np.concatenate((C21, C22), axis=1)
    return np.concatenate((C_top, C_bottom), axis=0)
A = np.array([[1, 3], [7, 5]])
B = np.array([[6, 8], [4, 2]])
print(f"Result :\n{strassen_matrix_multiplication(A,B)}")