class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create an array of size n for dynamic programming
        dp = [1] * len(nums)

        # Loop through the array nums
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)