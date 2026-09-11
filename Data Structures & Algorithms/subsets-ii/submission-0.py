from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the array in ascending order
        nums.sort()
        # Define a dfs to find all subset
        self.res = []
        def dfs(i: int, temp: List) -> None:
            # Base case:
            if i == len(nums):
                self.res.append(temp.copy())
                return
                
            # Add this num
            temp.append(nums[i])
            dfs(i + 1, temp)
            temp.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, temp)
            return
        
        dfs(0, [])
        return self.res
