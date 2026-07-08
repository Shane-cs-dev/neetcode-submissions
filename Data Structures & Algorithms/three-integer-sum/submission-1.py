class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Define a list for result
        res = []

        # Sort the array in ascending order
        nums.sort()

        def helper(idx: int, target: int) -> None:
            # Define two pointers
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                # Define current value
                curr_val = nums[left] + nums[right]
                if curr_val == target:
                    print([idx, left, right])
                    res.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif curr_val > target:
                    right -= 1
                else:
                    left += 1


        # Loop through the array and check the valid result
        for i, num in enumerate(nums):
            # Calculate the rest of the value
            rest = 0 - num

            if not i == 0 and nums[i] == nums[i - 1]:
                continue
            # Calling helper function to check the value
            helper(i, rest)
        
        return res