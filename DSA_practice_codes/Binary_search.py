def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high )//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid -1)
    else:
        return recursive_binary_search(arr, target, mid +1, high)
    

arr = [2, 5, 6, 7, 8, 9, 10]
target = 8
result = recursive_binary_search(arr, target, 0, len(arr)-1)
if result != -1:
    print(f"Target{target} founnd at index {result}")
else:
    print(f"Target{target} not found in the array")