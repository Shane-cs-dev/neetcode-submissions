class Solution:
    def countSubstrings(self, s: str) -> int:
        # Define a helper function to find the valid Palindrome and return the count of valid one
        def helper(left: int, right: int) -> int:
            count = 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        # Loop through every position in s and calculate the valid palindrome
        res = 0
        for i in range(len(s)):
            odd_count = helper(i, i)
            even_count = helper(i, i + 1)
            res += odd_count + even_count
        
        return res