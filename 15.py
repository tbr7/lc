# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
from typing import List
class Solution:
    def threeSum_bruteforce(self, nums: List[int]) -> List[List[int]]:
        m = {}
        sols = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l = sorted((nums[i], nums[j], nums[k]))
                        if l not in sols:
                            sols.append(l)
        return sols

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            target = 0 - nums[i] - nums[j]
            if target in seen:
                res.append([nums[i], nums[j], target])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]: # Increment j while the next value is the same as before to avoid duplicates in the result.
                    j += 1
            seen.add(nums[j])
            j += 1


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            print(i, nums[i])
            if nums[i] > 0: 
                break # If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums, i, res)
        return res


    def threeSum_nosort(self, nums: List[int]) -> List[List[int]]:
        res, dupes = set(), set()
        seen = {}
        for i, n_i in enumerate(nums):
            if n_i not in dupes:
                dupes.add(n_i)
                print()
                for j, n_j in enumerate(nums[i+1:]):
                    target = 0 - n_i - n_j
                    print([n_i, n_j], target, seen)
                    if target in seen and seen[target] == i:
                        res.add(tuple(sorted((n_i, n_j, target))))
                    seen[n_j] = i
        return res



def main():
    sol = Solution()
    # print(sol.threeSum_bruteforce([-1,0,1,2,-1,-4]))
    # print(sol.threeSum([0, 1, 1]))
    # print(sol.threeSum([0,0,0,0]))
    print(sol.threeSum_nosort([-1,0,1,2,-1,-4]))
main()