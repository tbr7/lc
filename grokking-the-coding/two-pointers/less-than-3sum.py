# Given an array arr of unsorted numbers and a target sum, 
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
# Write a function to return the count of such triplets.

class Solution:
    def triplet_with_smaller_sum(self, arr, target):
        arr.sort()
        res = set()
        smaller_triplets = 0
        print(arr)
        for i in range(len(arr)):
            l, r = i + 1, len(arr) - 1
            total = target - arr[i]
            while l < r:
                if arr[l] + arr[r] < total:
                    #  arr[r] >= arr[l] so we can replace arr[r] by any number between
                    smaller_triplets += r - l
                    l += 1
                else:
                    r -= 1
        return smaller_triplets
def main():
    s = Solution()
    print(s.triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print()
    # print(s.triplet_with_smaller_sum([-1, 0, 2, 3], 3))

main()