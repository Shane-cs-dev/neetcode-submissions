class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Define two pointers left and right
        left, right = 0, len(s) - 1

        # Define boolean delete
        delete = False

        def helper(left: int, right: int) -> bool:
            return s[left] == s[right]

        # Loop through the string s
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # If the char is matched
            if s[left] != s[right]:
                if not delete:
                    # Calling helper function
                    if helper(left + 1, right):
                        left += 1
                    elif helper(left, right - 1):
                        right -= 1
                    else:
                        return False
                    delete = True
                elif delete:
                    return False
            elif s[left] == s[right]:
                left += 1
                right -= 1
        
        return True
                