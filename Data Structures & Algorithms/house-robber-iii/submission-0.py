from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Define a node to traverse the tree
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int] | None:
            # Base case:
            if not node:
                return (0, 0) # (Take, skip)
            
            # Traverse the tree
            left_take, left_skip = dfs(node.left)
            right_take, right_skip = dfs(node.right)
            
            # Define the max of take this value and skip the value
            take = node.val + left_skip + right_skip
            skip = max(left_take, left_skip) + max(right_take, right_take)

            return (take, skip)
        
        max1, max2 = dfs(root)
        return max(max1, max2)
