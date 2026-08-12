class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window
        left = 0
        min_len = float('inf')
        cur_sum = 0
        for i in range(len(nums)):
            # Adding current num into cur_sum
            cur_sum += nums[i]

            while cur_sum >= target:
                min_len = min(min_len, i - left + 1)
                cur_sum -= nums[left]
                left += 1
        
        min_len = 0 if min_len == float('inf') else min_len

        return min_len