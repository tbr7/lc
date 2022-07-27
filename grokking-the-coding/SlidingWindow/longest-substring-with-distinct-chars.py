# Given a string, find the length of the longest substring, which has all distinct characters.

def non_repeat_substring(str):
    char_index_map = {}
    start, longest = 0, 0

    for end in range(len(str)):
        right_char = str[end]
        
        if right_char in char_index_map:
            # this is tricky; in the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            start = max(start, char_index_map[right_char] + 1) 
        
        char_index_map[right_char] = end
            
        longest = max(longest, end - start + 1)

    return longest

def main():
    print(non_repeat_substring("aabccbb"))
    print(non_repeat_substring("abbb"))
    print(non_repeat_substring("abccde"))

main()