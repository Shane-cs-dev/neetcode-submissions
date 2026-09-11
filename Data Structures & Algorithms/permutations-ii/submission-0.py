from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Define a function to do dfs
        self.res = []
        def dfs(idx: int) -> None:
            # Base case:
            if idx == len(nums):
                self.res.append(nums[:])
                return
            
            for i in range(idx, len(nums), 1):
                # Skip the duplicated
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                # Swap the index with idx
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
            return
        
        dfs(0)
        return self.res