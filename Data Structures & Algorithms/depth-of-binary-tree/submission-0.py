# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Define a dfs function to count the max depth
        def dfs(node: Optional[TreeNode]) -> int:
            # Base case
            if not node:
                return 0
            
            # Define left and right node
            left = dfs(node.left)
            right = dfs(node.right)

            return max(left, right) + 1
        
        return dfs(root)
