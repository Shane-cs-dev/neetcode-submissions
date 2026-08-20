"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Define a function to recursively build the QuadTree
        def dfs(n, r, c):
            # Base case:
            if n == 1:
                return Node(grid[r][c] == 1, True) # This should be leaf node when the n == 1
            
            # Udpate the mid size
            mid = n // 2

            # Traverse all location
            top_left = dfs(mid, r, c)
            top_right = dfs(mid, r, c + mid)
            bottom_left = dfs(mid, r + mid, c)
            bottom_right = dfs(mid, r + mid, c + mid)

            if (top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and 
                top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True)
            else:
                return Node(0, False, top_left, top_right, bottom_left, bottom_right)
        
        return dfs(len(grid), 0, 0)
