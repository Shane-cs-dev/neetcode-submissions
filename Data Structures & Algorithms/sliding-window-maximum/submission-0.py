from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Loop through the array nums and append the value
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i+k]))
        return res
