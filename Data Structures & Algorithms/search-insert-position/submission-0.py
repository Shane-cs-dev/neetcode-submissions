class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Define left and right pointer
        left, right = 0, len(nums) - 1

        # Binary search to find the minimum max value
        while left < right:
            mid = left + (right - left) // 2
            print(f"This is mid value: {nums[mid]}")
            if nums[mid] < target:
                left = mid + 1
                print(nums[left])
            else:
                right = mid
                print(nums[right])
        print(f"This is final left: {nums[left]}")

        left = left if left < len(nums) - 1 else left + 1

        return left