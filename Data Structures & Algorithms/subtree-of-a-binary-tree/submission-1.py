# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Define a dfs function to traverse the tree until we find the root of the subtree
        def findSubroot(node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> Optional[TreeNode]:
            # Base case:
            if not node:
                return None
            if node.val == subRoot.val:
                return node

            # Traverse the tree
            left = findSubroot(node.left, subRoot)
            right = findSubroot(node.right, subRoot)

            if left:
                return left
            elif right:
                return right
            
            return None
        
        main_node = findSubroot(root, subRoot)
        if not main_node:
            return False
        print(main_node.val)

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
        
        return sameTree(main_node, subRoot)


















        
