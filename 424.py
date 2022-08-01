class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, longest, maxFreq = 0, 0, 0
        freqMap = {}
        for end in range(len(s)):
            curr = s[end]
            if curr not in freqMap:
                freqMap[curr] = 0
            freqMap[curr] += 1
            
            maxFreq = max(maxFreq, freqMap[curr])
            
            while end - start + 1 - maxFreq > k: # if we do not have a valid size, move window start
                start_char = s[start]
                freqMap[start_char] -= 1
                start += 1
            
            longest = max(longest, end - start + 1)
        return longest
                
def main():
    sol = Solution()
    print(sol.characterReplacement("AABABBA", 1))

main()