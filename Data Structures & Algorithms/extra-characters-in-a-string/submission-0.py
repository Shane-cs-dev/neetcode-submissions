
class Solution:
    # This is the method of general dynamic programming
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Define the size of the string s
        n = len(s)
        # Create an array
        dp = [0] * (n + 1)

        # Loop from the last char in the s
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1 # This should be the extra char if there is not match from this char
            # Loop through the dict
            for word in dictionary:
                if i + len(word) <= n and s[i:i + len(word)] == word:
                    dp[i] = min(dp[i + len(word)], dp[i])
        
        return dp[0]