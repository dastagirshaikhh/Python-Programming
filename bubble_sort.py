# print( )

# # Practical 5.1
# # Bubble sort
# def bubbleSort(array):
#     for i in range(len(array)):
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp

# data = [56, 5, 11, 24, -5, 17, 25, 32]
# bubbleSort(data)
# print("Sorted array in Ascending Order:", data)

# print( )


# Recursive Implementation
def bubble_sort_recursive(arr, n):
    # Base case
    if n == 1:
        return arr
    # One pass of bubble sort
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    # Recursively sort the remaining elements
    bubble_sort_recursive(arr, n-1)
    return arr
arr = [5, 3, 8, 6, 7, 2]
n = len(arr)
print(bubble_sort_recursive(arr, n))
