def medianofmedian(nums, k):

    # we have to split the list of chunks into 5
    chunks = [nums[i:i+5] for i in range(0, len(nums), 5)]
    # print("Divided chunks :",chunks)
    # print( )
    # the median is the middle item of sorted order
    # Note : the median of the medians is just approximately the median of original data structure(array)
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
    # print("Medians of above divided chunks :",medians)
    # print( )
    pivot = sorted(medians)[len(medians)//2]
    # print("Pivot value :",pivot)

    # partition phase
    right_subarray = [i for i in nums if i > pivot]
    left_subarray = [j for j in nums if j < pivot]
    # print("Right subarray :",right_subarray)
    # print("Left subarray :",left_subarray)

    pivot_index = len(left_subarray)

    if k < pivot_index:
        # we have to consider left subarray because we are looking for smaller items 
        return medianofmedian(left_subarray, k)
    elif k > pivot_index:
        # here we have to consider right subarray because we are looking for larger items and we have to
        # update the value of k because a new data structure(array) is created for right subarray
        return medianofmedian(right_subarray, k-len(left_subarray)-1)
    else:
        return pivot

def select(nums,k):
    return medianofmedian(nums, k-1)

nums = [-5,7,-9,6,-2,4,15,-42,1,0,46,-21,92]
arr = [-5,7,-9,6,-2,4,15,-42,1,0,46,-21,92]
arr.sort()
print("Raw array :", nums)
print("Sorted array :",arr)
print("Element of entered value from the array :",select(nums, 1)) # this will return smallest element from the array
# As the entered value will increase greater value will be returned
print("Element of entered value from the array :",select(nums, 2)) 
print("Element of entered value from the array :",select(nums, 3)) 
print("Element of entered value from the array :",select(nums, 4)) 
print("Element of entered value from the array :",select(nums, 5)) 