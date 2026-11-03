class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Define the size of the grid
        row, col = len(heights), len(heights[0])

        # Create a set for the river from Pacific or Atlantic
        Pacific, Atlantic = set(), set()

        # Create a function for dfs
        def dfs(r: int, c: int, prev_val: int, visited: set) -> None:
            # Base case:
            if r < 0 or c < 0 or r >= row or c >= col or (r, c) in visited or prev_val > heights[r][c]:
                return

            # Mark this location as reachable
            visited.add((r, c))

            # Exploration
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
            return

        # Start from Pacific side
        for i in range(row):
            # Pacific
            dfs(i, 0, heights[i][0], Pacific)
            # Atlantic
            dfs(i, col - 1, heights[i][col - 1], Atlantic)
        for j in range(col):
            # Pacific
            dfs(0, j, heights[0][j], Pacific)
            # Atlantic
            dfs(row - 1, j, heights[row - 1][j], Atlantic)
        
        ans = [[r, c] for r, c in Pacific if (r, c) in Atlantic]
        return ans
