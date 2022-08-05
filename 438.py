# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result_indexes = []

        pmap = {}
        # add a counter to keep track of pattern char counts
        # {a:1, b:1, c:1} for 'abc'
        for c in p:
            if c not in pmap:
                pmap[c] = 0
            pmap[c] += 1

        
        start = 0
        freq = {}
        for end in range(len(s)):
            curr = s[end]
            # if letter not in pattern then skip forward to next letter and throw away this window
            if curr not in pmap:
                start = end + 1
                freq = {}
                continue

            if curr not in freq:
                freq[curr] = 0
            freq[curr] += 1

            while freq[curr] > pmap[curr]:
                freq[s[start]] -= 1
                start += 1
            
            if end - start + 1 == len(p):
                result_indexes.append(start)

        return result_indexes


def main():
    sol = Solution()
    print(sol.findAnagrams("ppqp", "pq"))
    print(sol.findAnagrams("abbcabc", "abc"))
    print(sol.findAnagrams("cbaebabacd", "abc"))
    print(sol.findAnagrams("abab", "ab"))



main()
