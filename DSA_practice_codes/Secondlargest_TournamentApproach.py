def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    # Initialize first and second largest
    players = [(num, []) for num in arr]

    while len(players) > 1:
        next_round = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):

                a_val, a_beaten = players[i]
                b_val, b_beaten = players[i + 1]
                if a_val > b_val:
                    next_round.append((a_val, a_beaten + [b_val]))
                else:
                    next_round.append((b_val, b_beaten + [a_val]))
            else:
                 next_round.append(players[i])
        players = next_round
    # The winner is the first element in the list

    max_player = players[0]
    if not max_player[1]:
        return None
    
    return max(max_player[1])

print(find_second_largest([60, 58, 2, 4, 25, 56, 45])) # Output: 58
print(find_second_largest([1, 2, 3, 4, 5])) # Output: 4
print(find_second_largest([5, 5])) # Output: None
print(find_second_largest([1])) # Output: None