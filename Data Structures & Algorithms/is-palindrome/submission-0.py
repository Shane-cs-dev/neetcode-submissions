class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define the left and right pointer
        left, right = 0, len(s) - 1

        # loop through the string s and check 
        while left < right:
            if not s[left].isalnum():
                left += 1

            if not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True