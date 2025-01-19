# use only if the data structure is unsorted

# Practical 4.1
# linear search
import numpy as np

def linear_search(arr1, n):
    for i in range(np.shape(arr1)[0]):
        if arr1[i] == n:
            return i
    return -1

arr1 = np.array([6, 9, 8, 7, 2, 4, 5])
n = int(input("Enter a number: "))
result = linear_search(arr1, n)
if result == -1:
    print("Element not available.")
else:
    print("Element exists at index", result)


def linear_search(num, item):
    for i in range(len(num)):
        if num[i] == item:
            return i
    return -1

num = [5,4,7,8,9,2,3,5,4,1]
print(linear_search(num, 1))