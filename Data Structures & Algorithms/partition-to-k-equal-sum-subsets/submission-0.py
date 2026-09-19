class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Check if the sum of the array nums can be partition into k groups
        total = sum(nums)
        if total % k != 0:
            return False
        
        # Calculate the target number
        target = total // k
    
        # Create an array with size k
        groups = [0] * k
        
        # Create a method to calculate the sum of each group
        def dfs(idx : int) -> bool:
            # Base case:
            if idx == len(nums):
                return True
            
            # Loop through the groups
            for i in range(k):
                # Add the number if < target
                if groups[i] + nums[idx] <= target:
                    groups[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    groups[i] -= nums[idx]
                if groups[i] == 0:
                    break
            return False
        
        return dfs(0)