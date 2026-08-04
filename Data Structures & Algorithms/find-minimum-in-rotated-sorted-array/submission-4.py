class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Define left and right pointer
        left, right = 0, len(nums) - 1

        # Binary search
        while left < right:
            mid = left + (right - left) // 2

            # If right side is sorted
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        
        return nums[left]
