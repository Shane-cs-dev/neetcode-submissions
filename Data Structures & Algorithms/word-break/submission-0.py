class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Define a dfs function to go over string s
        memo = {}
        def dfs(idx: int) -> bool:
            # Base case:
            if idx == len(s):
                return True

            if idx in memo:
                return memo[idx]
            
            # Loop through the wordDict and check each value
            for word in wordDict:
                if idx + len(word) <= len(s):
                    if s[idx: idx + len(word)] == word:
                        if dfs(idx + len(word)):
                            memo[idx] = True
                            return True

            memo[idx] = False
            return memo[idx]

        return dfs(0)