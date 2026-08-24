class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1
        self.cnt = 0
        def dfs(node):
            if not node or self.res != -1:
                return
            
            dfs(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
            dfs(node.right)
            
            return
        
        dfs(root)
        return self.res