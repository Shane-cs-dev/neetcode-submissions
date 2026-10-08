class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # First round of the maximum value from index 0 to n - 2
        rob1, rob2 = 0, 0
        for i in range(len(nums) - 1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        res1 = rob2

        # Second rounde of the maximum value from index 1 to n - 1
        rob1, rob2 = 0, 0
        for i in range(1, len(nums)):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return max(res1, rob2)