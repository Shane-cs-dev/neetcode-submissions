class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        # Define a function for dfs
        def dfs(idx: int, Alice: bool) -> int:
            # Base case:
            if idx == len(stoneValue):
                return 0
            if (idx, Alice) in dp:
                return dp[(idx, Alice)] 



            res = float("-inf") if Alice else float("inf")
            score = 0
            for i in range(idx, min(idx + 3, len(stoneValue))):
                if Alice: # Find the maximum of the res
                    score += stoneValue[i]
                    res = max(res, score + dfs(i + 1, not Alice))
                else:
                    score -= stoneValue[i]
                    res = min(res, score + dfs(i + 1, not Alice))

            dp[(idx, Alice)] = res
            return res
        
        ans = dfs(0, True)
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
