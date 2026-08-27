# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Define a dfs to traverse the tree and calculate the max value
        self.res = float('-inf')
        def dfs(node: Optional[TreeNode]) -> int:
            # Base case;
            if not node:
                return 0
            
            # Track the max value from left and right
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # Update value for left and right
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # Update res
            self.res = max(self.res, node.val + left_max + right_max)

            return node.val + left_max + right_max
        
        dfs(root)
        return self.res