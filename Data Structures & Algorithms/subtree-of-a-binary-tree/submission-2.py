# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Define a fucntion check of this is the same tree
        def sameTree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            # Base case:
            # Reach the end of the tree
            if not node1 and not node2:
                return True
            # One node reaches the end but the other not
            if not node1 or not node2:
                return False
            # Not the same val
            if node1.val != node2.val:
                return False
            
            left = sameTree(node1.left, node2.left)
            right = sameTree(node1.right, node2.right)

            # Condition check
            if not left or not right:
                return False
            
            return left and right
        
        self.res = False
        # Traverse the tree and check if the subRoot is the same tree
        def traverse(node: Optional[TreeNode]) -> bool:
            # Base case:
            if not node:
                return
            # If the node has the same value as subRoot
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    self.res = True
                    return 
            
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.res
















        
