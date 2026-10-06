class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 0, 1
        if n == 1:
            return cur
        
        for i in range(n):
            temp = cur
            cur = prev + temp
            prev = temp
            print(cur)
        return cur
        
    def climbStairs_dp(self, n: int) -> int:
        # Create a array of size n + 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(n + 1):
            if i >= 2:
                dp[i] += dp[i - 1] + dp[i - 2]

        for i in dp:
            print(i)
        return dp[n]
            