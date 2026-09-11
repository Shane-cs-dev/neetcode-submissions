from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the array in ascending order
        candidates.sort(reverse=False)

        # Define a backtracking function
        self.res = []
        def dfs(idx: int, target: int, temp: List) -> None:
            # Base case:
            if target == 0:
                self.res.append(temp[:])
            if idx == len(candidates):
                return

            for i in range(idx, len(candidates), 1):
                # Skip duplicated
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                # Prunning
                if target - candidates[i] < 0:
                    break # The rest of the number are higher than current one
                
                # Backtrack
                temp.append(candidates[i])
                dfs(i + 1, target - candidates[i], temp)
                temp.pop()
            return
        
        dfs(0, target, [])
        return self.res


