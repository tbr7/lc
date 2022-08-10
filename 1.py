from typing import List
# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            if target - num in sums:
                return [sums[target-num], i]
            else:
                sums[num] = i
        return [-1, -1]
        
def main():
    sol = Solution()
    print(sol.twoSum([1, 2, 3, 4, 6], 6))
    print(sol.twoSum([1, 2, 3, 4, 6], 6))
main()