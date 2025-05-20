def find_kth_smallest(arr, n):
    arr.sort()
    return arr[n-1]

arr = [2,8,7,3,5,9]
print(find_kth_smallest(arr, 6))