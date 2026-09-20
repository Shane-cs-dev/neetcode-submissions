class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        # Calculate the target number
        target = total // k

        # Create an array of size len(nums) to track the used num
        used = [False] * len(nums)

        # Create a method to track to do partition
        def dfs(idx: int, temp: int, groups: int) -> bool:
            # Base case:
            if groups == 0:
                return True
            if temp == target:
                return dfs(0, 0, groups - 1)
            
            # Loop through the array nums from given idx
            for i in range(idx, len(nums), 1):
                # Prunning: If adding this num exceed the target
                if nums[i] + temp > target or used[i]:
                    continue
                if not used[i]: # If the num has not been used
                    used[i] = True
                    if dfs(i + 1, temp + nums[i], groups):
                        return True
                    used[i] = False
                # Prunning: If there's nothing can be added into the this 
                if temp == 0:
                    break
            return False
        
        return dfs(0, 0, k)
        








    # This is the method with time complexity: O(k^n)
    def canPartitionKSubsets_1(self, nums: List[int], k: int) -> bool:
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