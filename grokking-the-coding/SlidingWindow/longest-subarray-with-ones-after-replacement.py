
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
#  find the length of the longest contiguous subarray having all 1s.

def length_of_longest_substring(arr, k):
    start, longest, max_ones_count = 0, 0, 0
    for end in range(len(arr)):
        if arr[end] == 1:
            max_ones_count += 1
        
        if end - start + 1 - max_ones_count > k:
            if arr[start] == 1:
                max_ones_count -= 1
            start += 1
        longest = max(longest, end - start + 1)

    return longest
def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
main()
