from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        squares = []
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                squares.insert(0, nums[r]**2)
                r -= 1
            else:
                squares.insert(0, nums[l]**2)
                l += 1
        return squares
def main():
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
main()