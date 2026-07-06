class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Define two pointers left and right
        left, right = 0, len(s) - 1

        # Define boolean delete
        delete = False

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # Loop through the string s
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # If the char is matched
            if s[left] != s[right]:
                # Calling helper function
                # Check if skipping left OR skipping right results in a palindrome
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            
            if s[left] == s[right]:
                left += 1
                right -= 1
        
        return True
                