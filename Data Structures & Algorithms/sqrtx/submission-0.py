class Solution:
    def mySqrt(self, x: int) -> int:
        # Corner case:
        if x == 1:
            return 1
        # define left and right pointer
        left, right = 0, x/2

        while left < right:
            # Calculate mid and its power
            mid = left + (right - left) // 2

            val = mid * mid

            if val == x:
                return int(mid)
            elif val > x:
                right = mid - 1
            else:
                left = mid
        
        return int(left)
