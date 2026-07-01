class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Define the size of the array nums
        n = len(nums)

        # Create an array of size n to store prefix
        prefix = [1] * n

        # Calculate prefix
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        print(prefix)
        # Calculate the result
        res = [1] * n
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] = prefix[i] * suffix
            # update suffix for the next round
            suffix *= nums[i]
        
        return res
        
