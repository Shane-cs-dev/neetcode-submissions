class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the max_hour
        max_h = max(piles)

        # Define left and right pointer to find the minimum eating rate
        left, right = 1, max_h

        def finished_banana(rate):
            # Define a variable to track the hour
            hour_needed = 0

            for pile in piles:
                # Calculate the hour needed for this pile with given rate
                hour_needed += (pile + rate - 1) // rate

                # Check if the hour exceed the limit
                if hour_needed > h:
                    return False

            return True

        # Binary search
        while left < right:
            # Calculate mid eating rate
            mid = left + (right - left) // 2

            # Check if curr rate is able to eat all banana in given limitation
            finished = finished_banana(mid)

            # Update pointer
            if finished:
                right = mid
            else:
                left = mid + 1
        
        return left




