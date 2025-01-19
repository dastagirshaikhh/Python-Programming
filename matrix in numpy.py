import numpy as np

sales = (4875, 8374, 3938, 3883, 2933)
profits_Ind = (5262, 2763, 3682, 3286, 2683)
profits_us = (3682, 2862, 4268, 2362, 2729)
profits_eu = (3567, 5486, 2464, 2486, 9659)

profit_matrix = np.array([profits_Ind, profits_eu, profits_us])
sales_array = np.array(sales)

print("\nMatrix \n", profit_matrix)
print("\nMatrix shape", profit_matrix.shape)

print("\nDivision of the matrix \n", profit_matrix/sales_array)

print("\nMultiplication of the matrix \n", profit_matrix*sales_array)

print("\nAddition of the matrix \n", profit_matrix+sales_array)

print("\nSubtraction of the matrix \n", profit_matrix-sales_array)

print("\nTranspose of the matrix \n", profit_matrix.T)

print("\nMean of the matrix", np.mean(profit_matrix))
