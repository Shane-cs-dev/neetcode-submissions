class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Define the size of the grid
        row, col = len(grid), len(grid[0])

        # Find the rotten fruit and add the location into queue for BFS operation
        queue = deque()
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # BFS calculation and count the minutes
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans = 0
        while queue and fresh > 0:
            # Count the number of the queue to loop to
            size = len(queue)
            for i in range(size):
                # Get the first one
                cur_r, cur_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    # Boundry check and make sure it is nearby fresh fruit
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] == 2
                        queue.append((nr, nc))
            ans += 1
        
        return ans if fresh == 0 else -1