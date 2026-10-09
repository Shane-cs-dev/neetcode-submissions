class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Define a function to find the longest Palindromic from this position of left and right 
        def helper(left: int, right: int) -> tuple[int, int]: # Return the left position and the length of this palindromic
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return (left + 1, right - left - 1)
        
        # Loop through every position in the string s
        res_idx, res_len = 0, 0
        for i in range(len(s)):
            odd_left, odd_len = helper(i, i)
            even_left, even_len = helper(i, i + 1)
            if odd_len > res_len:
                res_idx, res_len = odd_left, odd_len
            if even_len > res_len:
                res_idx, res_len = even_left, even_len
        
        return s[res_idx : res_idx + res_len]