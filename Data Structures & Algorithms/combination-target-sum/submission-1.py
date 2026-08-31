class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        temp = []
        # Define a function to do backtracking
        def dfs(idx: int, cur_sum: int) -> None:
            # Base case:
            if idx >= len(nums) or cur_sum > target:
                # print(temp)
                return
            # If the sum is matching the target
            if cur_sum == target:
                self.res.append(temp[:])
                return
            
            # Bactracking
            temp.append(nums[idx])
            dfs(idx, cur_sum + nums[idx]) # Pick this num
            temp.pop()
            dfs(idx + 1, cur_sum) # Skip this one

            return
        
        dfs(0, 0)
        return self.res
        
