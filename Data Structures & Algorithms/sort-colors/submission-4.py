import copy
class Solution:
    # This is Dutch National Flag Algorithm
    def sortColors(self, nums: List[int]) -> None:
        # Define pointers for comparison
        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            # If mid is equal to 0 -> swap with left 
            if nums[mid] == 0:
                # Swaping left and mid
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        
        return nums

    # This should be counting sort since it has limited number of num in array nums
    def sortColors_countingSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        
        # Update the frequency for all 
        for num in nums:
            colors[num] += 1
        
        # Accumulate the freq
        accu_colors = copy.deepcopy(colors)
        for i in range(1, len(accu_colors)):
            accu_colors[i] += accu_colors[i - 1]
        
        # Counting sort
        output_nums = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            # Define current value and check its index
            curr_val = nums[i]
            accu_colors[curr_val] -= 1
            output_nums[accu_colors[curr_val]] = curr_val

        # Copy back to nums
        nums[:] = output_nums
        return

