class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Define a function to do backtracking
        self.res = []
        temp = []
        def backtrack(idx: int) -> None:
            # Base case:
            if idx == len(nums):
                self.res.append(temp[:])
                return
            
            # Backtracking
            temp.append(nums[idx])
            backtrack(idx + 1)
            temp.pop()
            backtrack(idx + 1)
            return

        backtrack(0)
        return self.res
