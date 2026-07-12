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
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    stack.append(num1 // num2)
                print(stack[-1])
        return stack[-1]
