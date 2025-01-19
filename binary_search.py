# use only if the data structure is sorted

# Practical 4.2
# Binary Search
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = [65, 85, 14, 2, 5, 32, 12, 5, 8, 4, 11]
arr.sort()
x = 32
result = binarySearch(arr, 0, len(arr) - 1, x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)


# Recursive implementation of Binary Search
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40, 45, 48, 49, 50, 51, 56, 58, 59, 62, 63, 64, 68, 78, 79]
x = 78
result = binarySearch(arr, 0, len(arr) - 1, x)
if result == -1:
    print("Element not present")
else:
    print("Element is present at index", result)

print( )



def binary_search(container, item, left, right):
    if right < left:
        return -1
    
    middle_index = (left + right) // 2

    if container[middle_index] == item:
        return middle_index
    
    elif container[middle_index] > item:
        return binary_search(container, item, left, middle_index-1)
    
    elif container[middle_index] < item:
        return binary_search(container, item, middle_index+1, right)

num = [ 50, 51, 56, 58, 52, 3, 4, 10, 40, 45, 48, 49,9, 62, 63, 64, 68, 78, 79]

print(binary_search(num, 500, 0, len(num)-1))



