class Solution:
    def remove_duplicates(self, arr):
        print(arr)
        next_non_dupe = 1
        i = 0
        while i < len(arr):
            if arr[next_non_dupe - 1] != arr[i]:
                arr[next_non_dupe] = arr[i]
                next_non_dupe += 1
            i += 1
        
        
        return arr[:next_non_dupe]
def main():
    sol = Solution()
    print(sol.remove_duplicates([2,3,3,3,6,9,9]))
main()