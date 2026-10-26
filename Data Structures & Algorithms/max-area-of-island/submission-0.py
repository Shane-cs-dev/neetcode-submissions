class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Define the size of the grid
        row, col = len(grid), len(grid[0])

        # Define a function for dfs to calculate the area of the island
        def dfs(r: int, c: int) -> int:
            # Base case:
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:
                return 0
            
            # If this is a island 
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
        

        # Loop thrrough every cell and calculate the area
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res
