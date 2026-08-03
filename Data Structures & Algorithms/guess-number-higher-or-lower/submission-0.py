# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Define left and right pointer for binary search
        left, right = 0, n

        # Binary search
        while left <= right:
            # Calculate mid
            mid = left + (right - left) // 2

            val = guess(mid)

            if val == 0:
                return mid
            elif val == -1:
                right = mid - 1
            elif val == 1:
                left = mid + 1
        
        return left