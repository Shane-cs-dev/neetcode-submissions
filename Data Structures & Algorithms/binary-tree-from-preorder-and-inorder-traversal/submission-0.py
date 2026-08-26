# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hash map to quickly find the index in inorder list
        self.look_up = {val: idx for idx, val in enumerate(inorder)}

        # Define a function to build the binary tree
        self.node_idx = 0
        def dfs(left: int, right: int):
            # Base case
            if left > right:
                return None
            
            # Create a root node for this side of the tree
            node_val = preorder[self.node_idx]
            self.node_idx += 1
            cur_node = TreeNode(node_val)

            # Find the cur_node index in inorder array
            mid = self.look_up[node_val] # return the index of curret node in inorder array

            cur_node.left = dfs(left, mid - 1)
            cur_node.right = dfs(mid + 1, right)

            return cur_node
        
        return dfs(0, len(preorder) - 1)

