def reverse_array(arr):
    reverse_arr =[]
    for i in range(len(arr) -1, -1, -1):
        reverse_arr.append(arr[i])
    return reverse_arr


arr = [10,20,30,40,50]
print(reverse_array(arr))