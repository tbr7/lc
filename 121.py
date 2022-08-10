from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        smallest = 10001
        
        for p in prices:
            best_profit = max(best_profit, p - smallest)
            smallest = min(smallest, p)
        
        return best_profit
def main():
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
main()