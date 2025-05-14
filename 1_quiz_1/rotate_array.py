def rotate_array(arr, n):
    l = len(arr)
    n = n % l
    arr[:] = arr[-n:] + arr[:-n]

arr = [1, 2, 3, 4, 5, 6, 7]
n = 3
rotate_array(arr, n)

print("The array after rotating is:", arr)