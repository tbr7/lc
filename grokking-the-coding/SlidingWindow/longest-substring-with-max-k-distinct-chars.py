# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# Time complexity is O(N) because outer loop runs O(N) and the inner while will at max be O(N) as we only process each char once
# O(N + N) is equivalent to O(N)

def longest_substring_with_k_distinct(str1, k):
    freq = {}
    start, longest = 0, 0

    for end in range(len(str1)): # it's nice to use end instead of i here because it reminds us of the window
        right_char = str1[end]
        if right_char not in freq: # insert char into map until we have K chars
            freq[right_char] = 0
        freq[right_char] += 1 # keep track of how many of chars in the list

        while len(freq) > k: # if we now have MORE than k distinct chars then we need to shrink the window
            left_char = str1[start]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char] # remove from dictionary and we don't have to worry about order since we have window start
            start += 1
        longest = max(longest, end - start + 1)
    return longest

def main():
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))
    print(longest_substring_with_k_distinct("cbbebi", 10))

main()