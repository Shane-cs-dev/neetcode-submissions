class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Define left and right pointer for binary search
        left, right = 0, len(nums) - 1

        # Binary search
        while left <= right:
            mid = left + (right - left) // 2    

            # If mid matches the target value
            if nums[mid] == target:
                return True

            # Corner case: if left, mid, right has the same value
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                continue
            
            # If the left side is sorted
            if nums[left] <= nums[mid]:
                # If the target is not within the range
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            # If the right side is sorted
            else:
                # If the target is not within the range
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return nums[left] == target