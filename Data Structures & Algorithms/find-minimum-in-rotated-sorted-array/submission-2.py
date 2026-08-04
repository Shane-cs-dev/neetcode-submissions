class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Define left and right pointer
        left, right = 0, len(nums) - 1

        # Binary search
        res = float('inf')
        while left < right:
            mid = left + (right - left) // 2

            # If left side is sorted
            if nums[left] < nums[mid]:
                res = min(res, nums[left])
                left = mid + 1
            else:
                res = min(res, nums[mid])
                right = mid - 1
        
        return res

