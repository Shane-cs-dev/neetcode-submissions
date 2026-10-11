class Solution:
    """" Recursion solution """
    def numDecodings(self, s: str) -> int:
        # Create a memo and add a base case in it
        memo = {len(s) : 1}

        # Define a dfs function to go over the string s
        def dfs(idx: int) -> int:
            # Base case: 
            if idx in memo:
                return memo[idx]
            
            # Corner case
            if s[idx] == '0':
                return 0
            
            # Call the next one if this one is valid
            res = dfs(idx + 1)
            if idx + 1 < len(s) and (s[idx] == '1' or (s[idx] == '2' and s[idx + 1] in "0123456")):
                res += dfs(idx + 2)
            
            memo[idx] = res
            return memo[idx]
        
        return dfs(0)