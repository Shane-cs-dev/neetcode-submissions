class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            # Calculate the maximum for the next one
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    # def rob_dp(self, nums: List[int]) -> int:
    #     # Corner case:
    #     if len(nums) == 1:
    #         return nums[0]
    #     if len(nums) < 3:
    #         return max(nums[0], nums[1])

    #     # Create an array for dynamic programming
    #     dp = [0] * len(nums)
    #     dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    #     for i in range(2, len(nums)):
    #         dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    #     return dp[-1]