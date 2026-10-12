class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create an array of size amount + 1
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # Base case

        for i in range(len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        
        return dp[-1] if dp[-1] != float('inf') else -1