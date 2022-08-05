from collections import Counter
class Solution:
    def find_substring(self, str1, pattern):

        c = Counter(pattern)
        smallest = ""
        required = len(pattern)
        start = 0


        for end in range(len(str1)):
            curr = str1[end]
            # If we see a required letter, decrease the total target letter count
            if c[curr] > 0:
                required -= 1  

            # Decrease the letter count for the current letter
            # If the letter is not a target letter, the count just becomes -ve
            c[curr] -= 1
            print(c)

            while required == 0:
                if smallest == "" or end - start + 1 < len(smallest):
                    smallest = str1[start:end+1]
                
                c[str1[start]] += 1
                # If all required letters have been seen and now, a required letter is seen with count > 0
				# Increase the required length to be found. This will break out of the loop
                if c[str1[start]] > 0:
                    required += 1
                start += 1
    

        return smallest


def main():
    sol = Solution()
    # print(sol.find_substring("aabdec", "abc")) # abdec
    # print(sol.find_substring("aabdec", "abac")) # aabdec
    # print(sol.find_substring("abdbca", "abc")) # bca
    # print(sol.find_substring("adcad", "abc")) # ""
    print(sol.find_substring("cabwefgewcwaefgcf", "cae"))
main()

