from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Define a dfs to traverse the tree and delete node if the node has target value and is leaf node
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # Base case:
            if not node:
                return None
            
            # traverse the tree
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # Condition check
            if node.val == target and not node.left and not node.right:
                return None
            
            return node
        
        return dfs(root)