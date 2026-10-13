class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a array of size n + 1
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # Loop through the dp array
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]




    def wordBreak_dfs(self, s: str, wordDict: List[str]) -> bool:
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