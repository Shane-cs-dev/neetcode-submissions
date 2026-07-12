class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Create a stack for operation
        stack = []

        # Loop through the array asteriods and calculate collision
        for astr in asteroids:
            if not stack:
                stack.append(astr)
            
            else:
                prev_astr = stack[-1]
                # Condition for same direction
                if astr >= 0 and prev_astr >= 0:
                    stack.append(astr)
                elif astr < 0 and prev_astr < 0:
                    stack.append(astr)
                # Condition for different direction
                elif abs(astr) == abs(prev_astr):
                    stack.pop()
                elif abs(astr) > abs(prev_astr):
                    stack.pop()
                    stack.append(astr)
                else:
                    continue
        return stack
        