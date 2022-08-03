class Solution:
    def find_permutation(self, str1: str, pattern: str) -> bool:
        pattern_map = {}
        for c in pattern:
            if c in pattern_map:
                pattern_map[c] += 1
            else:
                pattern_map[c] = 1
        print(pattern_map)

        start = 0
        freq = {}
        for end in range(len(str1)):
            curr = str1[end]

            # if not in the pattern, move everything
            if curr not in pattern_map:
                freq = {}
                start = end + 1
                continue

            if curr not in freq:
                freq[curr] = 0
            freq[curr] += 1

            while freq[curr] > pattern_map[curr]:
                freq[str1[start]] -= 1
                start += 1

            # print(freq, start, end)
            if end - start + 1 == len(pattern): 
                return True
                


        return False
                
def main():
    sol = Solution()
    print(sol.find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(sol.find_permutation("oidbcaf", "abc"))
    print(sol.find_permutation("odicf", "dc"))
    print(sol.find_permutation("aaacb", "abc"))


# The above algorithm’s time complexity will be O(N + M)
# O(N+M)
# where ‘N’ and ‘M’ are the number of characters in the input string and the pattern, respectively.
main()