def remove_duplicates(nums):
    if not nums:
        return 0
    
    unique_index = 0

    for i in range(1, len(nums)):

        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1


nums = [1, 1, 2, 3, 4, 5, 5, 6, 6]
new_length = remove_duplicates(nums)
print("The new length of the array is:", new_length)
print("The array after removing duplicates is:", nums[:new_length])


