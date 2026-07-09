class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create two pointers to swap the array
        left = k - 1
        right = len(nums) - 1
        while left >= 0:
            nums[left], nums[right] = nums[right], nums[left]
            left -= 1
            right -= 1
        return