class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create stack and store speed and position into it
        stack = [(i, v) for i, v in zip(position, speed)]
        stack.sort()

        # Pop from stack and check the number of the car fleet
        res = 0
        prev_time = 0
        while stack:
            # Pop current one and check the time to reach the target position from its position
            pos, s = stack.pop()

            # Calculation
            curr_time = (target - pos) / s

            # If the time needed to reach the target is larger than previous time, add one car fleet
            if curr_time > prev_time:
                res += 1
                prev_time = curr_time
            
        return res