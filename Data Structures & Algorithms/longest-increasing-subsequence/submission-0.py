class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create an empty dict
        num_dict = {} # Store the num and the earliest index

        # Create an array of size n for dynamic programming
        dp = [0] * len(nums)
        dp[0] = 1

        # Loop through the array nums
        for i in range(1, len(nums)):
            # If the number is equal to previous one
            if nums[i - 1] == nums[i]:
                dp[i] = dp[i - 1]
            # If the number is greater than previous one
            elif nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1
            else: # Smaller than previous one
                # Check the index in the num_dict
                for prev_num, key in num_dict.items():
                    if prev_num < nums[i]:
                        dp[i] = max(dp[i], key + 1)
            
            # Add current number into the dict if there's no previous one
            if nums[i] not in num_dict:
                num_dict[nums[i]] = i
        
        return dp[len(nums) - 1]
