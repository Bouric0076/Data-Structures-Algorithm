numbers = [60, 58, 2, 4, 25, 56, 45]

max = numbers[0]

for num in numbers[1:]:
    if num > max:
        max = num
print("Max number is: ", max)

second_max = float('-inf')

for num in numbers:
    if num != max and num > second_max:
        second_max = num

print("Second max number is: ", second_max)

if second_max == float('-inf'):
    print("No second max number found - all numbers are equal.")
else:
    print("Second max number is: ", second_max)

    