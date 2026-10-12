class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Corner case:
        if not nums:
            return 0
        
        # Define max_val and min_val to track the Maximun and mininmum array
        max_val, min_val = nums[0], nums[0]

        res = nums[0]
        for i in range(1, len(nums), 1):
            temp = max_val
            # Update max_val
            if nums[i] * max_val > max_val:
                max_val *= nums[i]
            elif nums[i] * min_val > max_val:
                max_val = min_val * nums[i]
            else:
                max_val = nums[i]
            
            # Update min_val
            if nums[i] * min_val < min_val:
                min_val *= nums[i]
            elif nums[i] * max_val < min_val:
                min_val = max_val * nums[i]
            else:
                min_val = nums[i]
            
            res = max(max_val, res)
        
        return res

