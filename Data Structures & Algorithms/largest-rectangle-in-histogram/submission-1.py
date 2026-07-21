class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Create a stack to store heights (height, index)
        stack = []

        # Add 0 to array heights to trigger the calculation
        heights.append(0)

        # Loop through the edited array heights and do calculation
        max_area = 0
        for i, height in enumerate(heights):
            # Calculate max_area if we encounter height that is smaller than last one in the stack
            while stack and stack[-1][0] > height:
                # Get current height
                curr_h, curr_i = stack.pop()

                width = i if not stack else i - stack[-1][1] - 1

                max_area = max(max_area, curr_h * width)
                print(f"curr_h: {curr_h}, width: {width}, current area: {curr_h * width}")
            
            stack.append((height, i))

        return max_area
