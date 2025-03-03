print( )

# Practical 5.3
# Insertion Sort
def InsertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

data = [9, 5, 1, 4, 3]
InsertionSort(data)
print("Sorted Array in Ascending order:", data)

print( )