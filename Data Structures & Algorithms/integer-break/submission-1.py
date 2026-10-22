class Solution:
    def integerBreak(self, n: int) -> int:
        # Create an array of size n + 1 for dynamic programming
        dp = [0] * (n + 1)
        dp[1] = 1

        # Loop through the dp
        for i in range(2, len(dp)):
            dp[i] = 0 if i == n else i
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        
        return dp[n]
             





