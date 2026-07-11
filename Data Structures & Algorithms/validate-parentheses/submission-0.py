class Solution:
    def isValid(self, s: str) -> bool:
        # Define an empty stack
        stack = []

        # Define left parentheses
        left_p = ['(', '{', "["]

        # Loop throught the array s and check whether it is valid parentheses
        for op in s:
            if op in left_p:
                stack.append(op)
            else:
                if not stack:
                    return False
                # Check the condition
                prev_p = stack.pop()
                if op == ')':
                    if prev_p != '(':
                        return False
                elif op == '}':
                    if prev_p != '{':
                        return False
                else:
                    if prev_p != '[':
                        return False
                
        if stack: 
            return False
        return True

