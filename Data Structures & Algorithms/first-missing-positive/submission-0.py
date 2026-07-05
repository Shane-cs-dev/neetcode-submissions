class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Define the size of the array nums
        n = len(nums)

        # Create an truth table to check if the num is being visited
        seen = [False] * n

        # Loop through the array nums and mark as seen if the num is within the scope
        for num in nums:
            if 0 < num <= n:
                seen[num - 1] = True
        
        # Loop through the length of the array nums
        for i in range(1, n + 1):
            if not seen[i - 1]:
                return i

        return n + 1