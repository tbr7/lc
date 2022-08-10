# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

import enum


class Solution:
    def pair_with_targetsum(self, arr, target_sum):
        l, r = 0, len(arr) - 1
        while l < r:
            curr_sum = arr[l] + arr[r]
            if curr_sum == target_sum:
                return [l,r]
            elif curr_sum < target_sum:
                l += 1
            else:
                r -= 1
        return [-1, -1]


    def pair_with_targetsum_hm(self, arr, target_sum):
        sums = {}
        for i, num in enumerate(arr):
            if target_sum - num in sums:
                return [sums[target_sum-num], i]
            else:
                sums[num] = i
        return [-1, -1]

def main():
    sol = Solution()
    print(sol.pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(sol.pair_with_targetsum([2, 5, 9, 11], 11))

    print("####")

    print(sol.pair_with_targetsum_hm([1, 2, 3, 4, 6], 6))
    print(sol.pair_with_targetsum_hm([2, 5, 9, 11], 11))
main()