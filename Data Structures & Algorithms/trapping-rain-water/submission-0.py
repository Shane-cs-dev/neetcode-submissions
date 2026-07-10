class Solution:
    def trap(self, height: List[int]) -> int:
        # Define left and right pointer
        left, right = 0, len(height) - 1

        # Define max_left and max_right for trapped water calculation
        max_left = height[left]
        max_right = height[right]

        # Traverse the array height
        res = 0
        while left <= right:
            # Check which side will leak the water
            if height[left] <= height[right]:
                # Udpate the max_left value
                max_left = max(height[left], max_left)
                res += max_left - height[left]
                left += 1
            else:
                # Update the max_right value
                max_right = max(height[right], max_right)
                res += max_right - height[right]
                right -= 1
        return res
