class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Define a dfs function to do backtracking
        def backtrack(idx: int, cur_sum: int) -> int:
            # Base case:
            if idx == len(nums):
                return cur_sum
            
            # Define the value of take it or not take it
            take_it = backtrack(idx + 1, cur_sum ^ nums[idx])
            skip_it = backtrack(idx + 1, cur_sum)

            return take_it + skip_it
        
        return backtrack(0, 0)