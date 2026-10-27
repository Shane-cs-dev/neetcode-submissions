"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Check the corner case:
        if not node:
            return None
        
        # Create an dummy node point to node
        dummy = node

        # Create a hash map to track the copied node
        clone_map = {node: Node(node.val)}

        # Create a queue to store node's neighbor
        queue = deque()
        queue.append(node)

        # BFS operation
        while queue:
            # Get the first one
            cur_node = queue.popleft()

            # Loop through the neighbor and 
            # update the clone map and neighbor for this node
            if cur_node.neighbors:
                for nei in cur_node.neighbors:
                    # Check if the node exist in the clone map -> Create one if not
                    if nei not in clone_map:
                        queue.append(nei)
                        clone_map[nei] = Node(nei.val)
                    # Update the nei for the clone cur_node
                    clone_map[cur_node].neighbors.append(clone_map[nei])
        
        return clone_map[dummy]
                    
                    











