# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur = root
        parent = None
        # Find the given node
        while cur and cur.val != key:
            parent = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right

        # If there's node with key
        if not cur:
            return root

        # Node with one child or not child
        if not cur.left or not cur.right:
            # Define the child
            child = cur.left if cur.left else cur.right
            # Check where should we update the tree
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        # Node with both childs
        else:
            delNode = cur
            cur = cur.right
            prev = None
            while cur.left: # Find the min-node in the right subtree
                prev = cur
                cur = cur.left
            
            if prev: # prev is the parent of the mini-node
                prev.left = cur.right
                cur.right = delNode.right
            
            cur.left = delNode.left

            if not parent: # If we are deleting root
                return cur
            
            # Check where we update the tree
            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur
        
        return root













