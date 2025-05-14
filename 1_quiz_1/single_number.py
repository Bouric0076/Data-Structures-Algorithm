def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

#Example
nums = [4,1,2,1,2]
print("The single number in the array is:", single_number(nums))
