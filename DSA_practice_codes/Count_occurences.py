def count_occurences(arr, x):
    count = 0
    for num in arr:
        
        print("checking: ", num)
        if num == x:
         count += 1
        return count
    
arr = [2, 5, 7, 8, 2, 9, 2, 2]
x = 2
print(f"{x} appears {count_occurences(arr, x)} times")
