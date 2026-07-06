class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Define two pointers left and right
        left, right = 0, len(s) - 1

        # Define helper function to check validPalindrome after deletion
        def helper(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # Loop through the string s by two pointers
        while left < right:
            if s[left] != s[right]:
                return helper(left + 1, right) or helper(left, right - 1)
            left += 1
            right -= 1
        return True
                