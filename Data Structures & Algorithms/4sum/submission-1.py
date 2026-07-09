class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array in ascending order
        nums.sort()

        # Define helper function
        res = []
        def helper(i: int, j: int, target: int) -> None:
            # Define left and rihgt pointer
            left, right = j + 1, len(nums) - 1
            while left < right:
                # Calculate current value
                curr_val = nums[left] + nums[right]
                if curr_val == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_val > target:
                    right -= 1
                else:
                    left += 1



        # Loop through the nums from 0
        for i in range(len(nums)):
            # Skip duplicate num
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Find the next unique number from i
            for j in range(i + 1, len(nums)):
                # Skip duplicate
                # Still need to count the first one
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Calculate the rest value and call helper function to add validated combination into it 
                rest = target - nums[i] - nums[j]
                helper(i, j, rest)

        return res
