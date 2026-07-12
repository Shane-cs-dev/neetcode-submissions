class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create an empty stack for operation
        stack = [] ## Storing [value, index]

        res = [0] * len(temperatures)
        # Loop through the array temperatures
        for i, tem in enumerate(temperatures):
            while stack and tem > stack[-1][0]:
                # Udpate the index
                val, idx = stack.pop()
                res[idx] = i - idx
            stack.append([tem, i])
        return res

