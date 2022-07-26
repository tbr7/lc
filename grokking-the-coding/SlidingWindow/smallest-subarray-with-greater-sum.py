# Given an array of positive integers and a number 'S', 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'.
#  Return 0 if no such subarray exists.

import math

def smallest_subarray_sum(s, arr):
    smallest = math.inf
    _sum, window_start = 0, 0
    for i in range(len(arr)):
        _sum += arr[i]
        while _sum >= s:
            smallest = min(smallest, i - window_start + 1)
            _sum -= arr[window_start]
            window_start += 1
    return smallest if smallest < math.inf else 0

def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


# Time Complexity
# O(N + N) or O(N) because outer for loop runs for all elements and the inner while loop processes each element only once

main()