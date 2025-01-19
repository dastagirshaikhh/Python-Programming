from random import shuffle


def MergeSort(nums):
    if len(nums) == 1:
        return

    middle_index = len(nums) // 2
    left_subarray = nums[:middle_index]
    right_subarray = nums[middle_index:]

    MergeSort(left_subarray)
    MergeSort(right_subarray)

    i, j, k = 0, 0, 0

    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] > right_subarray[j]:
            nums[k] = left_subarray[i]
            i += 1
        else:
            nums[k] = right_subarray[j]
            j += 1

        k += 1

    while i < len(left_subarray):
        nums[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        nums[k] = right_subarray[j]
        j += 1
        k += 1


if __name__ == "__main__":
    nums = []
    
    for i in range(-11, 11):
        nums.append(i)

    shuffle(nums)
    print(nums)
    print("\nlist after sorting elements using merge sort:")
    MergeSort(nums)
    print(nums)

