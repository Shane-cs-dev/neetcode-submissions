class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check if the given num can be partition into two subsets
        target = sum(nums)
        if target % 2 != 0:
            return False
        target /= 2

        # Define a dfs function
        def dfs(idx: int, cur_sum: int) -> bool:
            # Base case:
            if cur_sum == target:
                return True

            # Loop through the index of the array nums from idx
            for i in range(idx, len(nums)):
                # Pruning
                if cur_sum + nums[i] > target:
                    continue
                # If we can choose this one
                if dfs(i + 1, cur_sum + nums[i]):
                    return True

            return False
            
        return dfs(0, 0)


        