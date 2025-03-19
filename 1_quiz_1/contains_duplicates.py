def contains_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1, 1, 2, 3, 4, 5, 5, 6, 6, 1, 8]
print("The array contains duplicates:", contains_duplicates(nums))