# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # Define dfs function to inorderly traverse the tree
        def dfs(node: Optional[TreeNode]):
            # Base case:
            if not node:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

            return
        
        dfs(root)

        return res
