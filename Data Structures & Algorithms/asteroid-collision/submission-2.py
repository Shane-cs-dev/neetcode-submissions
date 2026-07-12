class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Create a stack for operation
        stack = []

        # Loop through the array asteriods and calculate collision
        for astr in asteroids:
            # Condition of collision
            while stack and astr < 0 and stack[-1] > 0:
                temp = astr + stack[-1]
                # Equal size
                if temp == 0:
                    stack.pop()
                    astr = 0
                # If the astr is bigger
                elif temp < 0:
                    stack.pop()
                # If the astr in stack is bigger
                else:
                    astr = 0

            if astr:
                stack.append(astr)
        return stack
                    
        
