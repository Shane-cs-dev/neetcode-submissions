class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Define the top floor 
        n = len(cost)

        # Create a array of size n + 1
        dp = [0] * (n + 1)

        # Loop through the dp from index 2
        for i in range(2, n + 1, 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]

