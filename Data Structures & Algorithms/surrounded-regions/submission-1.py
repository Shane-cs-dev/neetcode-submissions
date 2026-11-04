class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Define the size of the grid
        row, col = len(board), len(board[0])

        # Define a function for dfs operation
        visited = set()
        def dfs(r: int, c: int) -> None:
            # Base case:
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] == 'X':
                return
            # If this cell is within the grid and is 'O'
            visited.add((r, c))

            # Exploration
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        

        # Loop through the edge and store cells that connect to the edge into the set
        visited = set()
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][col - 1] == 'O':
                dfs(i, col - 1)
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[row - 1][j] == 'O':
                dfs(row - 1, j)
        
        for i in range(1, row -1, 1):
            for j in range(1, col - 1, 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'

        return 

            