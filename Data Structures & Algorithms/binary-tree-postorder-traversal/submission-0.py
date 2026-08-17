# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # Define a dfs function to do postorder traversal
        def dfs(node: Optional[TreeNode])->None:
            # Base case:
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
            return 
        
        dfs(root)
        return res