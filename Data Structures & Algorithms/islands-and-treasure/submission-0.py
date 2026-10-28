class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Define the size of the grid
        row, col = len(grid), len(grid[0])

        # Define the value for land
        LAND = 2**31 - 1

        # Define a dfs to update the distance for land
        def dfs(r: int, c: int, dis: int) -> None:
            # Base case:
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == -1:
                return
            
            if grid[r][c] < dis:
                return
            
            # Update the distance for this land and do exploration
            grid[r][c] = dis

            dfs(r + 1, c, dis + 1)
            dfs(r, c + 1, dis + 1)
            dfs(r - 1, c, dis + 1)
            dfs(r, c - 1, dis + 1)
            return
        
        # Loop through every cell in the grid and do dfs if there's a treasure
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    dfs(i + 1, j, 1)
                    dfs(i - 1, j, 1)
                    dfs(i, j + 1, 1)
                    dfs(i, j - 1, 1)
        
        return