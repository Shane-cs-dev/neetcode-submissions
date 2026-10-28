class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Define the size of the grid
        row, col = len(grid), len(grid[0])

        # Define the value for land
        LAND = 2**31 - 1

        # Collect all treasure chest coordinates into a queue for multi-source BFS
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == LAND:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        
        return