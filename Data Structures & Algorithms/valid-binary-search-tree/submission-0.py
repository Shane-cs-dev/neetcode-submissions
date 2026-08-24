from typing import Tuple
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Define a function to traverse the tree with tuple as a range
        def dfs(node: Optional[TreeNode], range: Tuple[int, int]) -> bool:
            # Base case:
            if not node:
                return True
            if node.val > range[1] or node.val < range[0]:
                return False
            
            # Traverse the tree
            left = dfs(node.left, (range[0], node.val))
            right = dfs(node.right, (node.val, range[1]))

            if not left or not right:
                return False
            
            return True
        
        return dfs(root, (float("-inf"), float("inf")))

