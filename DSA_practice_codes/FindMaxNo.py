numbers = [12, 5, 7, 3, 19, 1, 21, 8]

max = numbers[0]
min = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]



print("Max number is: ", max)
print("Min number is: ", min)

# This code finds the maximum and minimum numbers in a list of integers. 
# It initializes the max and min variables with the first element of the list and then iterates through the list to update these variables accordingly. 
# Finally, it prints the maximum and minimum numbers found in the list.
# The time complexity of this code is O(n), where n is the number of elements in the list,because it iterates through the list once.
# The space complexity is O(1) because it uses a constant amount of space for the max and min variables, regardless of the size of the input list.
# we make a total of 2(n-1) comparisons in the worst case, which is O(n) in terms of time complexity.