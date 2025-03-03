def Kadane(nums):
    local_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        local_max = max(nums[i], local_max + nums[i])

        if local_max > global_max:
            global_max = local_max

    return global_max


print(Kadane([1, -2, -3, -4, 8]))
print(Kadane([1, 2, -3, 4, 8]))
print(Kadane([1, -2, 3, -4, 8]))
print(Kadane([1, 2, -3, -4, -8]))