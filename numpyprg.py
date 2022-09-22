import numpy as np

sales = [4875, 8374, 3938, 3883, 2933]
profit = [458, 622, 458, 488, 264]

sales_array = np.array(sales)
profit_array = np.array(profit)
total = sales_array/profit_array

print(sales_array)
print(profit_array)
print(total)
