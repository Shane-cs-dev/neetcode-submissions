import copy
class Solution:
    # This should be counting sort since it has limited number of num in array nums
    def sortColors(self, nums: List[int]) -> None:
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
        for i in range(len(colors) - 1, -1, -1):
            # In-place update array nums
            while colors[i] > 0:
                # Update the index
                accu_colors[i] -= 1
                nums[accu_colors[i]] = i
                colors[i] -= 1
        
        return nums

