class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Create an array to track the used cell for col, negative diagonal, and positive diagonal
        col = [False] * n
        neg_dia = [False] * (2 * n)
        pos_dia = [False] * (2 * n)

        # Define a method to do backtracking
        self.res = []
        temp = [["."] * n for row in range(n)]
        def backtrack(r: int) -> None:
            # Base case:
            if r == n:
                copy = ["".join(row) for row in temp]
                self.res.append(copy)
                return
            
            # Loop through the column
            for c in range(n):
                # If the col hasn't been place
                if col[c] or neg_dia[r - c + n] or pos_dia[r + c]:
                    continue
                
                # Else mark as visited
                col[c], neg_dia[r - c + n], pos_dia[r + c] = True, True, True
                temp[r][c] = 'Q'
                backtrack(r + 1)
                temp[r][c] = '.'
                col[c], neg_dia[r - c + n], pos_dia[r + c] = False, False, False
            return 
        
        backtrack(0)
        return self.res