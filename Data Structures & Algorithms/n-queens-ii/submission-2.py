class Solution:
    def totalNQueens(self, n: int) -> int:
        # Define sets to track the cols, and diagonal for both direction
        cols, neg_dia, pos_dia = set(), set(), set()

        # Create a board for calculation
        temp = [['.'] * n for row in range(n)]

        # Define a method to find valid board using backtracking
        self.res = 0
        def backtrack(r: int) -> None:
            # Base case:
            if r == n:
                self.res += 1
                return
            
            # Loop through the col
            for c in range(n):
                # If there's a queen there in either same column or diagonal
                if c in cols or r - c in neg_dia or r + c in pos_dia:
                    continue
                
                # If this is a valid spot
                cols.add(c)
                neg_dia.add(r - c)
                pos_dia.add(r + c)
                temp[r][c] = 'Q'
                backtrack(r + 1)
                temp[r][c] = '.'
                cols.remove(c)
                neg_dia.remove(r - c)
                pos_dia.remove(r + c)
            return
        
        backtrack(0)
        return self.res

        