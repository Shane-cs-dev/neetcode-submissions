class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Define the size of the grid
        row, col = len(grid), len(grid[0])

        # Define a function to do dfs if encounter a island
        def dfs(r, c) -> int:
            # Base case: reach the edge or water
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:
                return 1
            
            if grid[r][c] == 2:
                return 0
            # Mark this location as visited
            grid[r][c] = 2

            # Exploration
            res = 0
            res += dfs(r + 1, c)
            res += dfs(r, c + 1)
            res += dfs(r - 1, c)
            res += dfs(r, c - 1)

            return res
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
        