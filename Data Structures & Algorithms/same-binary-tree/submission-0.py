class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Define a dfs function to traverse the tree
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            # Null node
            if not node1 and not node2:
                return True

            # Base case: Different node
            if not node1 or not node2:
                return False
            # Base case:
            if node1.val != node2.val:
                return False
            
            # Traverse the tree
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            if not left or not right:
                return False
            
            return left and right
        
        return dfs(p, q)