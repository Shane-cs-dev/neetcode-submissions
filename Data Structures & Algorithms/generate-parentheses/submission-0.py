class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        # Define a function for backtracking
        temp = []
        def dfs(open_p: int, close_p: int) -> None:
            # Base case
            if open_p == close_p == n:
                self.res.append("".join(temp))
                return
            
            # Addint a open parenthesis
            if open_p < n:
                temp.append('(')
                dfs(open_p + 1, close_p)
                temp.pop()
            if open_p > close_p: #If adding a close parenthesis is valid
                temp.append(')')
                dfs(open_p, close_p + 1)
                temp.pop()
            
            return
        
        dfs(0, 0)
        return self.res
        


