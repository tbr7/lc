# Given a sorted array, create a new array containing squares of all the numbers
#  of the input array in the sorted order.
class Solution:
    def make_squares(self, arr):
        squares = []
        if len(arr) == 0: return squares

        l = 0
        r = len(arr) - 1
        print(arr)
        while l <= r:
            l_val = arr[l]*arr[l]
            r_val = arr[r]*arr[r]
            print(l, r, l_val, r_val)
            if l_val >= r_val:
                squares.insert(0, l_val)
                l += 1
            else:
                squares.insert(0, r_val)
                r -= 1

        return squares
def main():
    s = Solution()
    print(s.make_squares([-2, -1, 0, 2, 3])) # => [0, 1, 4, 4, 9]
    print(s.make_squares([-7, 4])) # => [16,49]

main()
