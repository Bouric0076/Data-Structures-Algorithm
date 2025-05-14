numbers = [12, 5, 7, 3, 19, 1, 21, 8]

# Step 1: Initialize min and max
if numbers[0] > numbers[1]:
    max = numbers[0]
    min = numbers[1]
else:
    max = numbers[1]
    min = numbers[0]

# Step 2: Process the rest of the list in pairs
for i in range(2, len(numbers),2):
    if i + 1 < len(numbers): # Check if there is a pair to compare
        if numbers[i] < numbers [i + 1]:
            local_max = numbers[i + 1]
            local_min = numbers[i]
        else:
            local_max = numbers[i]
            local_min = numbers[i + 1]

        if local_max > max:
            max = local_max
        if local_min < min:
            min = local_min

    else: # If there is an odd number of elements, compare the last element with max and min
        if numbers[i] > max:
            max = numbers[i]
        elif numbers[i] < min:
            min = numbers[i]

print("Max number is: ", max)
print("Min number is: ", min)
# This code finds the maximum and minimum numbers in a list of integers using a tournament approach.
# total comparisons made in this approach is (3n/2) - 2, which is O(n) in terms of time complexity.
# The space complexity is O(1) because it uses a constant amount of space for the max and min variables, regardless of the size of the input list.