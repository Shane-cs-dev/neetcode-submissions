from typing import List, Optional
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Define a backtracking function to find all combinations
        self.res = []
        def dfs(idx: int, temp: List) -> None:
            # Base case:
            if len(temp) == k:
                self.res.append(temp[:])
                return
            
            for i in range(idx, n + 1, 1):
                temp.append(i)
                dfs(i + 1, temp)
                temp.pop()
            return
        
        dfs(1, [])
        return self.res