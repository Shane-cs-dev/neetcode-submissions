from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Define a dfs function to traverse the tree
        def dfs(node: Optional[TreeNode], max_val: int) -> int:
            if not node:
                return 0
            
            # Count if current node is greater or equal to the max_val
            count = 0
            if node.val >= max_val:
                count = 1

            max_val = max(max_val, node.val)

            # Traverse the tree
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count
        
        return dfs(root, root.val)