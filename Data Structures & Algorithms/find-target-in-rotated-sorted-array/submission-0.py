class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Define left and right pointer
        left, right = 0, len(nums) - 1

        # Binary search
        while left <= right:
            # Calculate mid
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # If the left side is sorted
            if nums[left] < nums[mid]:
                # If the target is not within the range
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                # If the target is within the range
                else:
                    right = mid - 1
            # If the right side is sorted
            else:   
                # If the target is not within the range
                if nums[mid] > target or target > nums[right]:
                    right = mid - 1
                # If the target is within the range
                else:
                    left = mid + 1
        return -1