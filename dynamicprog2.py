#  Function to find the length of the longest increasing subsequence ?

from __future__ import annotations
def longest_subsequence(array: list[int]) -> list[int]:
    array_length = len(array)
    if array_length <= 1:
        return array
        # Else
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq: list[int] = []
    while not is_found and i < array_length:
        if array[i] < pivot:
            is_found = True
            temp_array = [element for element in array[i:] if element >= array[i]]
            temp_array = longest_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1
    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#  Function to find the length of the longest increasing subsequence
def lis(arr):
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"The length of the longest increasing subsequence is {lis(arr)}")

