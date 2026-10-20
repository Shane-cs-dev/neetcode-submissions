class Solution:
    def numSquares(self, n: int) -> int:
        # Find the num that num * num <= n
        target = 0
        for i in range(n):
            if i * i <= n:
                target = i
            else:
                break
        
        # Create an array of size n + 1
        dp = [n] * (n + 1)
        dp[0] = 0

        # loop through the dp and check the base case
        for i in range(1, len(dp)):
            for j in range(1, target + 1):
                if i - j * j >= 0:
                    dp[i] = min(dp[i - j * j] + 1, dp[i])
        
        return dp[n]

        