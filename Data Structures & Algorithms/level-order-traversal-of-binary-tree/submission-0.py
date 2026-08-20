from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Corner case:
        if not root:
            return []
        # create empty queue for bfs operations
        q = deque()

        # initialization
        q.append(root)

        # BFS operations
        res = []
        while q:
            # Calculate the number of the item for this layer
            times = len(q)

            # Loop through this whole layer
            temp = []
            for _ in range(times):
                cur = q.popleft()
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(temp)

        return res