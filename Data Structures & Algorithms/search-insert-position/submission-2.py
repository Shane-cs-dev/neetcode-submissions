class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Define left and right pointer
        left, right = 0, len(nums)

        # Binary search to find the minimum max value
        while left < right:
            mid = left + (right - left) // 2
            print(f"This is mid value: {nums[mid]}")
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        # Report the final location
        if left < len(nums):
            print(f"This is final left: {nums[left]}")

        return left
