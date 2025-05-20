def find_the_kth_largest(arr, k):
    arr.sort(reverse = True)
    return arr[k - 1]

arr =[3, 4, 5, 7, 9, 2]
print(find_the_kth_largest(arr, 1))