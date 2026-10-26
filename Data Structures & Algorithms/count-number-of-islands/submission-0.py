class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define the size of the grid
        row, col = len(grid), len(grid[0])

        # Define a function to find all the land
        def dfs(r: int, c: int) -> None:
            # Base case:
            if r >= row or c >= col or r < 0 or c < 0 or grid[r][c] == "0":
                return
            
            # The location is island -> mark as visited
            grid[r][c] = "0"

            # Explore the whole island
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            return
        
        # Loop through evey cells and update the island num
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        
        return res