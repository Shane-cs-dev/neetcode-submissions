from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Create an empty queue for bfs
        q = deque()
        q.append(root)

        # BFS operation
        res = []
        while q:
            times = len(q)

            for i in range(times):
                cur = q.popleft()
                if i == times - 1:
                    res.append(cur.val)
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res