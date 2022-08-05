# Given a string and a pattern, find all anagrams of the pattern in the given string.

class Solution:
    def find_string_anagrams(self, str1, pattern):
        result_indexes = []
        # TODO: Write your code here

        pmap = {}
        # add a counter to keep track of pattern char counts
        # {a:1, b:1, c:1} for 'abc'
        for p in pattern:
            if p not in pmap:
                pmap[p] = 0
            pmap[p] += 1

        
        start = 0
        freq = {}
        for end in range(len(str1)):
            curr = str1[end]
            # if letter not in pattern then skip forward to next letter and throw away this window
            if curr not in pmap:
                start = end + 1
                freq = {}
                continue

            if curr not in freq:
                freq[curr] = 0
            freq[curr] += 1

            while freq[curr] > pmap[curr]:
                freq[str1[start]] -= 1
                start += 1
            
            if end - start + 1 == len(pattern):
                result_indexes.append(start)

        return result_indexes


def main():
    sol = Solution()
    print(sol.find_string_anagrams("ppqp", "pq"))
    print(sol.find_string_anagrams("abbcabc", "abc"))

main()
