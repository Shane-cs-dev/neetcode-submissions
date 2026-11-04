class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Define the size of the grid
        row, col = len(board), len(board[0])

        # Define a function for dfs operation
        def dfs(r: int, c: int, visited: set) -> bool:
            # Base case:
            if (r <= 0 or c <= 0 or r >= row - 1 or c >= col - 1) and board[r][c] == 'O':
                return True
            if board[r][c] == 'X':
                return False
            if (r, c) in visited:
                return False
            
            # Mark this location as visited
            visited.add((r, c))

            # Exploration
            down = dfs(r + 1, c, visited)
            up = dfs(r - 1, c, visited)
            right = dfs(r, c + 1, visited)
            left = dfs(r, c - 1, visited)

            return (down or up or right or left)
        
        # Loop through the inner grid
        for i in range(1, row - 1, 1):
            for j in range(1, col - 1, 1):
                if board[i][j] == 'O':
                    visited = set()
                    if not dfs(i, j, visited):
                        for r, c in visited:
                            board[r][c] = 'X'
        
        return 

            