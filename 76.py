#Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
# every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        smallest = ""
        start, missing = 0, len(t)
        

        for end in range(len(s)):
            curr = s[end]
            # If we see a required letter, decrease the total missing letter count
            if freq[curr] > 0:
                missing -= 1  

            # Decrease the letter count for the current letter
            # If the letter is not a target letter, the count just becomes negative
            freq[curr] -= 1

            while missing == 0:
                if smallest == "" or end - start + 1 < len(smallest):
                    smallest = s[start:end+1]
                
                freq[s[start]] += 1
                # If all required letters have been seen and now, a required letter is seen with count > 0
				# Increase the required length to be found. This will break out of the loop
                if freq[s[start]] > 0:
                    missing += 1
                start += 1
    
        return smallest

def main():
    sol = Solution()
    print(sol.minWindow("cabwefgewcwaefgcf", "cae"))
main()

