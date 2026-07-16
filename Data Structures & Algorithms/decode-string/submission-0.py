class Solution:
    def decodeString(self, s: str) -> str:
        # Create a stack to store string
        string_stack = []

        # Create another stack to store count
        count_stack = []

        # Create empty string to store current string all the way to result
        curr = ""
        times = 0
        
        # Loop through the string 
        for char in s:
            # Store the count to variable times
            if char.isdigit():
                times = times* 10 + int(char)
            elif char == '[':
                string_stack.append(curr)
                count_stack.append(times)
                # Reset the  
                curr = ""
                times = 0
            elif char == ']':
                temp = curr
                curr = string_stack.pop()
                count = count_stack.pop()
                curr += temp * count
            else:
                curr += char
        
        return curr

