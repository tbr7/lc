# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

# Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# You can start with any tree, but you can’t skip a tree once you have started.
# You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets

# Time complexity is O(N) because outer loop runs O(N) and the inner while will at max be O(N) as we only process each char once
# O(N + N) is equivalent to O(N)
def fruits_into_baskets(fruits):
    NUM_BASKETS = 2
    max_fruits, start = 0, 0
    freq = {}
    for end in range(len(fruits)):
        curr_fruit = fruits[end]
        if curr_fruit not in freq:
            freq[curr_fruit] = 0
        freq[curr_fruit] += 1

        while len(freq) > NUM_BASKETS:
            curr_fruit = fruits[start]
            freq[curr_fruit] -= 1
            if freq[curr_fruit] == 0:
                del freq[curr_fruit]
            start += 1

        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits

def main():
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))

main()