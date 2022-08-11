from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_non_dupe = 1
        i = 0
        while i < len(nums):
            if nums[next_non_dupe - 1] != nums[i]:
                nums[next_non_dupe] = nums[i]
                next_non_dupe += 1
            i += 1
        print(nums[:next_non_dupe])
        return next_non_dupe
def main():
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
main()