class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # Define an array for dynamic programming
        dp = [float("-inf")] * (n + 1)
        dp[n] = 0

        # Loop through the array backward and check the max value
        for i in range(n - 1, -1, -1):
            score = 0
            for j in range(i, min(i + 3, n)):
                score += stoneValue[j]
                dp[i] = max(dp[i], score - dp[j + 1])
        
        if dp[0] == 0:
            return "Tie"
        return "Alice" if dp[0] > 0 else "Bob"
