class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Define a stack for calculation
        stack = []

        # Loop through the array operations
        for op in operations:
            if op == '+':
                num2, num1 = stack[-1], stack[-2]
                stack.append(num1 + num2)
            elif op == 'D':
                new_num = stack[-1] * 2
                stack.append(new_num)
            elif op == 'C':
                stack.pop()
            else:
                new_num = int(op)
                stack.append(new_num)
        print(stack)
        return sum(stack)