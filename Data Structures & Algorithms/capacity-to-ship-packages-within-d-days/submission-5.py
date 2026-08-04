class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Find the max number in the weights
        max_weight = max(weights)

        # Define left and right pointer
        left, right = max_weight, sum(weights)

        def helper(mid) -> bool:
            day, package = 1, 0
            # Loop through the weights to check the package
            for wei in weights:
                # If adding this one exceed the limit
                if package + wei > mid:
                    # Reset the package
                    package = 0
                    day += 1
                    if day > days:
                        return False
                package += wei

            return day <= days

        # Binary search
        while left < right:
            # Calculate mid val
            mid = left + (right - left) // 2

            if helper(mid):
                right = mid
            else:
                left = mid + 1
        
        return left














