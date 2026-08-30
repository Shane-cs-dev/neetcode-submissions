# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Define a function to transform a tree into string
        self.res = []
        def dfs(node: Optional[TreeNode]) -> None: 
            # Base case:
            if not node:
                self.res.append("N")
                return 
            
            # Traverse the tree
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        # print(",".join(self.res))
        return ",".join(self.res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Corner case
        if not data:
            return None
        
        self.vals = data.split(",")
        # print(self.vals)
        # Define a dfs function to traverse the data
        self.index = 0
        def dfs():
            # Base case:
            if self.vals[self.index] == "N":
                self.index += 1
                return None
            
            # Else if the node has value
            cur_node = TreeNode(int(self.vals[self.index]))
            self.index += 1
            # Traverse the tree
            cur_node.left = dfs()
            cur_node.right = dfs()

            return cur_node
        
        return dfs()
