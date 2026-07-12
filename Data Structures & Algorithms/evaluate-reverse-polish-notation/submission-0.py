class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack for operation
        stack = []

        # Define list for operand
        op = ['+', '-', '*', '/']

        for token in tokens:
            if token not in op:
                stack.append(token)
            else:
                num1, num2 = int(stack[-2]), int(stack[-1])
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif toke == '/':
                    stack.append(num1 / num2)
        return stack[-1]
