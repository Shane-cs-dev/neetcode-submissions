class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Corner case
        if not nums:
            return 0

        # Loop through the array and check the duplicate
        # Define slow pointer
        k = 0 # Can think of the number of swapping
        for i in range(1, len(nums)):
            # Modify the nums when encounter unique num
            if nums[i] != nums[i - 1]:
                k += 1
                nums[k] = nums[i]
        return k + 1