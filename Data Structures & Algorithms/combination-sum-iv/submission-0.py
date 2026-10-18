class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Create an array of size target + 1
        dp = [0] * (target + 1)
        dp[0] = 1

        # Loop through the dp and nums to update the value
        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]