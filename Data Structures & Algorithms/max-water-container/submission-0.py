class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Define left and right pointer
        left, right = 0, len(heights) - 1

        # Check area for every locations
        res = 0
        while left < right:
            # Find the min edge and calculate the area
            edge = min(heights[left], heights[right])

            # Define the width for this round
            width = right - left

            # update the area
            res = max(edge * width, res)

            # update the pointer
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res
        