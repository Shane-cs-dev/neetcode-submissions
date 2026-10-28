class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Define the size of the grid
        row, col = len(grid), len(grid[0])

        # Define the value for land
        LAND = 2**31 - 1

        # Multi-source BFS
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        # BFS operation
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dis = 1
        while queue:
            # Define the size of the current layer
            size = len(queue)

            for item in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == LAND:
                        grid[nr][nc] = dis
                        queue.append((nr, nc))
            dis += 1
        
        return
