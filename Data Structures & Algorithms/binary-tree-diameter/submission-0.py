# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # Define a dfs function to find the longest route
        def dfs(node: Optional[TreeNode]) -> int:
            # Base case:
            if not node:
                return 0
            
            # Traverse the node
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the global diameter with path through current node
            self.res = max(self.res, left + right)
            max_len = max(left, right) + 1

            # Return height of current node to parent
            return max_len
        
        dfs(root)
        return self.res