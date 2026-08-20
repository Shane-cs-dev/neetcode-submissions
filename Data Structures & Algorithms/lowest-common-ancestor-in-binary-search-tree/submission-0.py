# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Define a dfs to find a tree that the value of the node is in between the value of p and q
        self.LCA = None
        def dfs(node: Optional[TreeNode]):
            if self.LCA:
                return
            # Base case
            if not node:
                return 

            # Traverse the tree
            if p.val <= node.val < q.val and not self.LCA:
                self.LCA = node
                return

            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        print(self.LCA.val)
        return self.LCA


