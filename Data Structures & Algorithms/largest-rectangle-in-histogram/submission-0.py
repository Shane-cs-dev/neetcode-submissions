class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Create an empty list as stack
        stack = []

        # Append 0 to the array heights to force calculation
        heights.append(0)

        # Define max area and loop through the array heights
        max_area = 0
        for i, height in enumerate(heights):
            while stack and stack[-1][0] > height:
                # Get the last one
                curr_height, curr_idx = stack.pop()

                # If there's no item left in the stack
                width = 1
                if not stack:
                    width = i
                else:
                    width = i - stack[-1][1] - 1

                # Update max value
                max_area = max(max_area, curr_height * width)
                
            stack.append((height, i))
                 
        return max_area
                    