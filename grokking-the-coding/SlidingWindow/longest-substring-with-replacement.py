# Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, find the length of the longest substring having the same letters after replacement.

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

def length_of_longest_substring(str1, k):
    start, longest, max_repeat_letter = 0, 0, 0
    freq = {}
    for end in range(len(str1)):
        curr_char = str1[end]
        
        if curr_char not in freq:
            freq[curr_char] = 0
        freq[curr_char] += 1

        max_repeat_letter = max(max_repeat_letter, freq[curr_char]) # current char is the one we are checking for
        if end - start + 1 - max_repeat_letter > k:
            left_char = str1[start]
            freq[left_char] -= 1
            start += 1
        
        longest = max(longest, end - start + 1)
    return longest



def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))
main()