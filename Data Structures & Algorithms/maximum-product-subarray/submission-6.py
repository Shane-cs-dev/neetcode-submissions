class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Corner case:
        if not nums:
            return 0
        
        # Define max_val and min_val to track the Maximun and mininmum array
        max_val, min_val = nums[0], nums[0]

        res = nums[0]
        for i in range(1, len(nums), 1):
            # print(f"Max: {max_val}, min: {min_val}")
            temp = max_val
            # Update max_val
            max_val = max(max_val * nums[i], min_val * nums[i], nums[i])
            
            # Update min_val
            min_val = min(temp * nums[i], min_val * nums[i], nums[i])
            
            # print(f"Update: Max: {max_val}, min: {min_val}")
            res = max(max_val, res)
            # print(res)
        
        return res

