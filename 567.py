class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern_map = {}
        for c in s1:
            if c in pattern_map:
                pattern_map[c] += 1
            else:
                pattern_map[c] = 1

        start = 0
        freq = {}
        for end in range(len(s2)):
            curr = s2[end]

            # if not in the pattern, move everything
            if curr not in pattern_map:
                freq = {}
                start = end + 1
                continue

            if curr not in freq:
                freq[curr] = 0
            freq[curr] += 1

            while freq[curr] > pattern_map[curr]:
                freq[s2[start]] -= 1
                start += 1

            if end - start + 1 == len(s1): 
                return True
                
        return False
                
def main():
    sol = Solution()
    print(sol.checkInclusion("bcdxabcdy", "bcdyabcdx"))
    print(sol.checkInclusion("oidbcaf", "abc"))
    print(sol.checkInclusion("odicf", "dc"))
    print(sol.checkInclusion("aaacb", "abc"))



main()