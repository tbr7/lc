from typing import List
class Solution():
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        smaller_triplets = 0
        nums.sort()
        for i in range(len(nums)):
            new_target = target - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < new_target:
                    smaller_triplets += r - l
                    l += 1
                else:
                    r -= 1

        return smaller_triplets
def main():
    s = Solution()
    print(s.threeSumSmaller([-2,0,1,3], 2))
main()