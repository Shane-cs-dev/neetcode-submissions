class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Define a dfs function to do backtracking
        self.res = []
        def dfs(idx: int) -> None:
            # Base case:
            if idx == len(nums):
                self.res.append(nums[:])
                return
            
            # Loop through the nums
            for i in range(idx, len(nums), 1):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
            return
        
        dfs(0)
        return self.res